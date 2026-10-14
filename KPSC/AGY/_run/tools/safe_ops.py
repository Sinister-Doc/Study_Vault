"""
safe_ops.py - Strict write-boundary and file operation guards for KPSC KAS Vault Run.
All file creations, edits, writes, appends, directory creations and deletions
MUST pass through these safe functions.
"""

import os
import sys
import stat
import shutil
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
import hashlib
import urllib.request
import urllib.error


ROOT_DIR = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\KPSC\AGY"
RUN_DIR = os.path.join(ROOT_DIR, "_run")
ACTIONS_LOG = os.path.join(RUN_DIR, "actions.log")
PROMPT_FILE = os.path.join(RUN_DIR, "PROMPT.md")
PROMPT_R2_FILE = os.path.join(RUN_DIR, "PROMPT_R2.md")
PROMPT_R3_FILE = os.path.join(RUN_DIR, "PROMPT_R3.md")
MAGAZINES_DIR = os.path.join(ROOT_DIR, "_sources", "magazines")


# Win32 API for canonical long paths
_kernel32 = ctypes.windll.kernel32
_GetLongPathNameW = _kernel32.GetLongPathNameW
_GetLongPathNameW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD]
_GetLongPathNameW.restype = wintypes.DWORD

def get_long_path(p: str) -> str:
    """Resolve 8.3 short paths to long paths if path exists or resolve closest ancestor."""
    try:
        buf = ctypes.create_unicode_buffer(2048)
        needed = _GetLongPathNameW(p, buf, 2048)
        if 0 < needed < 2048:
            return buf.value
        elif needed >= 2048:
            buf = ctypes.create_unicode_buffer(needed + 1)
            _GetLongPathNameW(p, buf, needed + 1)
            return buf.value
    except Exception:
        pass
    return p

def canonicalize_path(p: str) -> str:
    """
    Canonically resolve path:
    - strip \\?\\ prefixes
    - resolve relative segments & '..'
    - resolve symlinks/junctions via os.path.realpath
    - resolve 8.3 short names
    - check for Alternate Data Streams (':')
    - normalize case and separators
    """
    if not p or not isinstance(p, str):
        raise ValueError("Invalid path")
    
    clean_p = p.strip()
    if clean_p.startswith(r"\\?\UNC\\"):
        clean_p = r"\\" + clean_p[8:]
    elif clean_p.startswith(r"\\?\\"):
        clean_p = clean_p[4:]
    
    # Check alternate data streams (e.g. file.txt:stream)
    # Drive letter colon (C:\) is allowed at index 1 only.
    rest_of_path = clean_p[2:] if len(clean_p) > 2 and clean_p[1] == ':' else clean_p
    if ':' in rest_of_path:
        raise ValueError(f"Alternate data streams not permitted: {p}")
    
    # Resolve realpath (resolves symlinks, junctions, ..)
    abs_p = os.path.abspath(clean_p)
    real_p = os.path.realpath(abs_p)
    long_p = get_long_path(real_p)
    norm_p = os.path.normpath(long_p)
    return norm_p

# Canonical ROOT reference
CANONICAL_ROOT = canonicalize_path(ROOT_DIR).lower()
if not CANONICAL_ROOT.endswith(os.sep):
    CANONICAL_ROOT_WITH_SEP = CANONICAL_ROOT + os.sep
else:
    CANONICAL_ROOT_WITH_SEP = CANONICAL_ROOT

def log_action(entry_type: str, details: str):
    """Append-only action logger."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{now_str}] [{entry_type}] {details}\n"
    try:
        os.makedirs(os.path.dirname(ACTIONS_LOG), exist_ok=True)
        with open(ACTIONS_LOG, "a", encoding="utf-8") as f:
            f.write(msg)
    except Exception as e:
        sys.stderr.write(f"Failed to log action: {e}\n")

def is_strictly_inside_root(path_str: str) -> bool:
    """Verify target canonical path is strictly inside ROOT directory."""
    try:
        c_path = canonicalize_path(path_str).lower()
        # Must start with CANONICAL_ROOT_WITH_SEP and not be equal to CANONICAL_ROOT
        if c_path == CANONICAL_ROOT:
            return False
        return c_path.startswith(CANONICAL_ROOT_WITH_SEP)
    except Exception:
        return False

def verify_target(path_str: str, for_delete: bool = False) -> str:
    """Verify target path against safety fence. Returns canonical path on success."""
    if any(c in path_str for c in ['*', '?']):
        log_action("GUARD_EVENT", f"REFUSED wildcard path: {path_str}")
        raise PermissionError(f"Wildcards not allowed: {path_str}")
    
    # Trailing dots/spaces check
    stripped = path_str.rstrip()
    if path_str.endswith(" ") or path_str.endswith("."):
        log_action("GUARD_EVENT", f"REFUSED trailing dot/space path: {path_str}")
        raise PermissionError(f"Trailing dots/spaces not allowed: {path_str}")

    try:
        c_path = canonicalize_path(path_str)
    except Exception as e:
        log_action("GUARD_EVENT", f"REFUSED invalid path '{path_str}': {e}")
        raise PermissionError(f"Path canonicalization error: {e}")
    
    c_lower = c_path.lower()
    
    if c_lower == CANONICAL_ROOT or not c_lower.startswith(CANONICAL_ROOT_WITH_SEP):
        log_action("GUARD_EVENT", f"REFUSED outside-ROOT target: {path_str} -> {c_path}")
        raise PermissionError(f"Target '{path_str}' is outside ROOT: {ROOT_DIR}")
    
    if for_delete:
        # Check forbidden files
        canonical_actions = canonicalize_path(ACTIONS_LOG).lower()
        canonical_prompt = canonicalize_path(PROMPT_FILE).lower()
        canonical_prompt_r2 = canonicalize_path(PROMPT_R2_FILE).lower()
        canonical_prompt_r3 = canonicalize_path(PROMPT_R3_FILE).lower()
        if c_lower == canonical_actions:
            log_action("GUARD_EVENT", f"REFUSED deletion of protected file: {ACTIONS_LOG}")
            raise PermissionError("Deleting actions.log is strictly forbidden")
        if c_lower == canonical_prompt:
            log_action("GUARD_EVENT", f"REFUSED deletion of protected file: {PROMPT_FILE}")
            raise PermissionError("Deleting PROMPT.md is strictly forbidden")
        if c_lower == canonical_prompt_r2:
            log_action("GUARD_EVENT", f"REFUSED deletion of protected file: {PROMPT_R2_FILE}")
            raise PermissionError("Deleting PROMPT_R2.md is strictly forbidden")
        if c_lower == canonical_prompt_r3:
            log_action("GUARD_EVENT", f"REFUSED deletion of protected file: {PROMPT_R3_FILE}")
            raise PermissionError("Deleting PROMPT_R3.md is strictly forbidden")

        
        # Check reparse point / symlink / junction
        if os.path.islink(c_path):
            log_action("GUARD_EVENT", f"REFUSED deletion of symlink/junction: {c_path}")
            raise PermissionError("Deleting symlinks/junctions is strictly forbidden")
        
        try:
            if os.path.exists(c_path):
                attrs = ctypes.windll.kernel32.GetFileAttributesW(c_path)
                if attrs != -1 and (attrs & 0x400):  # FILE_ATTRIBUTE_REPARSE_POINT
                    log_action("GUARD_EVENT", f"REFUSED deletion of reparse point: {c_path}")
                    raise PermissionError("Deleting reparse points is strictly forbidden")
        except Exception:
            pass

    return c_path

def safe_mkdir(target_path: str) -> str:
    """Safely create directories strictly inside ROOT."""
    canon = verify_target(target_path, for_delete=False)
    os.makedirs(canon, exist_ok=True)
    log_action("SAFE_MKDIR", canon)
    return canon

def safe_write(target_path: str, content: str, encoding: str = 'utf-8') -> str:
    """Safely write content to a file strictly inside ROOT."""
    canon = verify_target(target_path, for_delete=False)
    parent = os.path.dirname(canon)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(canon, "w", encoding=encoding) as f:
        f.write(content)
    log_action("SAFE_WRITE", f"{canon} ({len(content)} chars)")
    return canon

def safe_append(target_path: str, content: str, encoding: str = 'utf-8') -> str:
    """Safely append content to a file strictly inside ROOT."""
    canon = verify_target(target_path, for_delete=False)
    parent = os.path.dirname(canon)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(canon, "a", encoding=encoding) as f:
        f.write(content)
    log_action("SAFE_APPEND", f"{canon} ({len(content)} chars)")
    return canon

def safe_copy(src_path: str, dst_path: str) -> str:
    """Safely copy from read-only source (e.g. input PDF) to dst strictly inside ROOT."""
    dst_canon = verify_target(dst_path, for_delete=False)
    parent = os.path.dirname(dst_canon)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copy2(src_path, dst_canon)
    log_action("SAFE_COPY", f"{src_path} -> {dst_canon}")
    return dst_canon

def safe_move(src_path: str, dst_path: str) -> str:
    """Safely move a file or directory where source and destination are both strictly inside ROOT."""
    src_canon = verify_target(src_path, for_delete=True)
    if not os.path.exists(src_canon):
        log_action("GUARD_EVENT", f"REFUSED move of non-existent source: {src_path}")
        raise FileNotFoundError(f"Source path does not exist: {src_path}")
    
    dst_canon = verify_target(dst_path, for_delete=False)
    parent = os.path.dirname(dst_canon)
    if parent:
        os.makedirs(parent, exist_ok=True)
    
    shutil.move(src_canon, dst_canon)
    log_action("SAFE_MOVE", f"{src_canon} -> {dst_canon}")
    return dst_canon

def safe_delete(target_path: str) -> str:
    """Safely delete a file or directory strictly inside ROOT."""
    canon = verify_target(target_path, for_delete=True)
    if not os.path.exists(canon):
        log_action("SAFE_DELETE_NOOP", f"Path does not exist: {canon}")
        return canon
    
    if os.path.isdir(canon):
        # Walk directory to ensure no protected files or outside symlinks exist inside
        for root, dirs, files in os.walk(canon):
            for f in files:
                f_path = os.path.join(root, f)
                verify_target(f_path, for_delete=True)
        shutil.rmtree(canon)
        log_action("SAFE_DELETE_DIR", canon)
    else:
        os.remove(canon)
        log_action("SAFE_DELETE_FILE", canon)
    return canon

def safe_download(url: str, target_path: str, max_size_bytes: int = 200 * 1024 * 1024, max_total_dir_bytes: int = 3 * 1024 * 1024 * 1024) -> dict:
    """
    Safely download a public PDF from publisher's official page:
    - Target must be inside ROOT/_sources/magazines/
    - Cap of 200 MB per file, 3 GB total for directory
    - Validates PDF magic header (%PDF-)
    - Computes SHA-256 hash
    - Never executes or installs anything
    """
    if not (url.startswith("http://") or url.startswith("https://")):
        log_action("GUARD_EVENT", f"REFUSED non-http URL for download: {url}")
        raise ValueError(f"Invalid URL protocol: {url}")
    
    canon = verify_target(target_path, for_delete=False)
    canon_mag = canonicalize_path(MAGAZINES_DIR).lower()
    if not canon.lower().startswith(canon_mag):
        log_action("GUARD_EVENT", f"REFUSED download outside magazines dir: {canon}")
        raise PermissionError(f"Download target must be inside {MAGAZINES_DIR}")
    
    # Check total size of magazines dir
    total_size = 0
    if os.path.exists(canon_mag):
        for root, _, files in os.walk(canon_mag):
            for f in files:
                fp = os.path.join(root, f)
                try:
                    total_size += os.path.getsize(fp)
                except Exception:
                    pass
    if total_size >= max_total_dir_bytes:
        log_action("GUARD_EVENT", f"REFUSED download: magazines dir quota exceeded ({total_size} bytes)")
        raise ValueError("Magazines directory storage cap (3 GB) reached")
    
    parent = os.path.dirname(canon)
    if parent:
        os.makedirs(parent, exist_ok=True)
        
    temp_target = canon + ".downloading"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) KPSCStudyVaultBot/2.0"}
    )
    
    hasher = hashlib.sha256()
    downloaded_bytes = 0
    header_checked = False
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content_len = resp.headers.get("Content-Length")
            if content_len and int(content_len) > max_size_bytes:
                raise ValueError(f"File exceeds maximum size limit of {max_size_bytes} bytes")
                
            with open(temp_target, "wb") as f_out:
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    if not header_checked:
                        if not chunk.startswith(b"%PDF-"):
                            raise ValueError(f"File is not a valid PDF (header was {chunk[:10]!r})")
                        header_checked = True
                    downloaded_bytes += len(chunk)
                    if downloaded_bytes > max_size_bytes:
                        raise ValueError(f"Download exceeded maximum limit of {max_size_bytes} bytes")
                    hasher.update(chunk)
                    f_out.write(chunk)
                    
        sha256_hex = hasher.hexdigest()
        if os.path.exists(canon):
            os.remove(canon)
        os.rename(temp_target, canon)
        log_action("SAFE_DOWNLOAD", f"{url} -> {canon} ({downloaded_bytes} bytes, sha256={sha256_hex[:12]}...)")
        return {
            "path": canon,
            "size": downloaded_bytes,
            "sha256": sha256_hex,
            "url": url
        }
    except Exception as e:
        if os.path.exists(temp_target):
            try:
                os.remove(temp_target)
            except Exception:
                pass
        log_action("DOWNLOAD_FAILED", f"Failed to download {url}: {e}")
        raise

def run_self_test() -> bool:
    """Run comprehensive self-tests verifying boundaries and refusal of outside paths."""
    print("Running safe_ops self-test...")
    test_ok = True
    
    # 1. Inside write test
    test_file = os.path.join(RUN_DIR, "test_file.tmp")
    try:
        safe_write(test_file, "self-test content")
        assert os.path.exists(test_file), "Test file was not created"
        safe_append(test_file, "\nappended content")
        print("  [PASS] Inside write and append")
    except Exception as e:
        print(f"  [FAIL] Inside write: {e}")
        test_ok = False
        
    # 2. Inside delete test
    try:
        safe_delete(test_file)
        assert not os.path.exists(test_file), "Test file was not deleted"
        print("  [PASS] Inside delete")
    except Exception as e:
        print(f"  [FAIL] Inside delete: {e}")
        test_ok = False

    # 3. Inside move test
    move_src = os.path.join(RUN_DIR, "test_move_src.tmp")
    move_dst = os.path.join(RUN_DIR, "test_move_dst.tmp")
    try:
        safe_write(move_src, "move-test content")
        safe_move(move_src, move_dst)
        assert not os.path.exists(move_src), "Source file still exists after move"
        assert os.path.exists(move_dst), "Destination file does not exist after move"
        safe_delete(move_dst)
        print("  [PASS] Inside move")
    except Exception as e:
        print(f"  [FAIL] Inside move: {e}")
        test_ok = False
        
    # 4. Refusal of outside paths
    outside_paths = [
        r"D:\outside.txt",
        r"C:\test.txt",
        r"..\outside.txt",
        os.path.join(ROOT_DIR, r"..\outside.txt"),
        r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\outside.txt",
        ROOT_DIR,  # ROOT itself cannot be deleted
        ACTIONS_LOG,  # Protected
        PROMPT_FILE,  # Protected
        PROMPT_R2_FILE,  # Protected
        PROMPT_R3_FILE,  # Protected
        os.path.join(RUN_DIR, "test*.txt"), # Wildcard
        os.path.join(RUN_DIR, "test:stream.txt") # ADS
    ]

    
    for p in outside_paths:
        refused = False
        try:
            if p in [ROOT_DIR, ACTIONS_LOG, PROMPT_FILE, PROMPT_R2_FILE, PROMPT_R3_FILE]:
                safe_delete(p)
            else:
                safe_write(p, "illegal content")

        except PermissionError:
            refused = True
        except ValueError:
            refused = True
        except Exception:
            refused = True
            
        if refused:
            print(f"  [PASS] Refused prohibited target: {p}")
        else:
            print(f"  [FAIL] FAILED to refuse target: {p}")
            test_ok = False
            
    # 4. Refusal of safe_download invalid targets
    try:
        safe_download("https://example.com/test.pdf", os.path.join(RUN_DIR, "outside_mag.pdf"))
        print("  [FAIL] safe_download failed to refuse path outside magazines dir")
        test_ok = False
    except PermissionError:
        print("  [PASS] safe_download refused destination outside magazines dir")
    except Exception as e:
        print(f"  [PASS] safe_download refused invalid destination: {e}")

    try:
        safe_download("ftp://example.com/test.pdf", os.path.join(MAGAZINES_DIR, "test.pdf"))
        print("  [FAIL] safe_download failed to refuse non-http protocol")
        test_ok = False
    except ValueError:
        print("  [PASS] safe_download refused non-http protocol")
    except Exception as e:
        print(f"  [PASS] safe_download refused non-http protocol: {e}")

    if test_ok:
        print("ALL safe_ops SELF-TESTS PASSED SUCCESSFULLY.")
        log_action("SELF_TEST", "All safe_ops boundary checks passed.")

    else:
        print("SOME safe_ops SELF-TESTS FAILED!")
        log_action("SELF_TEST_FAILED", "safe_ops self-test encountered errors.")
    return test_ok

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "test":
            success = run_self_test()
            sys.exit(0 if success else 1)
        elif cmd == "mkdir" and len(sys.argv) > 2:
            safe_mkdir(sys.argv[2])
        elif cmd == "write" and len(sys.argv) > 3:
            content = sys.argv[3]
            safe_write(sys.argv[2], content)
        elif cmd == "delete" and len(sys.argv) > 2:
            safe_delete(sys.argv[2])
        else:
            print(f"Unknown command: {cmd}")
            sys.exit(1)
    else:
        run_self_test()
