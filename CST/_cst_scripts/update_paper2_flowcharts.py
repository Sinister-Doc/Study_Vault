# -*- coding: utf-8 -*-
"""
Script to expand Paper 2 notes with comprehensive architectural flowcharts,
visual diagrams, and deep technical coverage.
"""
import os

AGY_ROOT = r"D:\SUPREETH N\Program Files\ObsidianVaults\StudyPrep\CST\Agy"

UNIT03_NOTE = """---
title: "Computer System Architecture: Digital Logic, Morris Mano Architecture, and Instruction Cycles"
description: "Comprehensive guide to Boolean algebra, Karnaugh maps, combinational logic (Adders, MUX, Decoders), flip-flops, Morris Mano basic computer architecture, register organization, instruction cycle flowcharts, addressing modes, and control unit design for CST Paper 2 Unit 3."
tags:
  - "kpsc-cst"
  - "paper2"
  - "unit03"
  - "computer-architecture"
  - "digital-logic"
  - "morris-mano"
  - "instruction-cycle"
syllabus_refs:
  - "P2-3.1"
  - "P2-3.2"
  - "P2-3.3"
syllabus_refs_partial: []
last_verified: "2026-10-12"
sources:
  - "https://schooleducation.karnataka.gov.in"
  - "Computer System Architecture (M. Morris Mano, 3rd Ed)"
  - "Digital Logic and Computer Design (M. Morris Mano)"
priority: "high"
---

> [!exam-focus]
> **Exam Weightage & Testing Style:** 15 questions (15 marks) in Paper 2 Unit 3. Core exam areas:
> - Universal Gates: Minimum NAND/NOR gate implementations for AND, OR, NOT, XOR, XNOR.
> - K-Map minimization (Gray code ordering: 00, 01, 11, 10; eliminating variables across pairs, quads, octets).
> - Combinational modules: Half/Full Adder and Subtractor equations; Multiplexers as universal function generators; Decoders.
> - Sequential logic: Flip-Flop characteristic equations ($SR, JK, D, T$), excitation tables, and eliminating JK race-around condition via Master-Slave flip-flops.
> - Morris Mano Basic Computer Architecture: Register bit-widths (PC, AR, DR, AC, IR, TR), common bus architecture, direct vs indirect addressing ($I$ bit 15).
> - Complete Instruction Cycle: Fetch, Decode, Effective Address Calculation ($T_0, T_1, T_2, T_3$), Execution, and Interrupt cycle.
> - Hardwired Control Unit vs Microprogrammed Control Unit (Control Memory, CAR, CDR).

---

## 1. Logic Gates and Universal Gate Implementations

Universal gates can implement any Boolean switching function without requiring any other gate type.

```mermaid
flowchart TD
    GATES["Logic Gates"] --> BASIC["Basic Gates:<br/>AND, OR, NOT"]
    GATES --> UNIV["Universal Gates:<br/>NAND, NOR"]
    GATES --> ARITH["Special Arithmetic Gates:<br/>XOR, XNOR"]
    
    UNIV --> NAND_IMPL["NAND Gate Implementations:<br/>• NOT = 1 NAND<br/>• AND = 2 NANDs<br/>• OR = 3 NANDs<br/>• XOR = 4 NANDs<br/>• XNOR = 5 NANDs"]
    UNIV --> NOR_IMPL["NOR Gate Implementations:<br/>• NOT = 1 NOR<br/>• OR = 2 NORs<br/>• AND = 3 NORs<br/>• XNOR = 4 NORs<br/>• XOR = 5 NORs"]
```

The diagram above models the gate hierarchy and universal gate synthesis costs.

### Minimum Gate Count Table for Standard Functions

| Target Function | Minimum 2-input **NAND** Gates | Minimum 2-input **NOR** Gates | Boolean Expression |
|---|:---:|:---:|---|
| **NOT ($A'$)** | **1** | **1** | $\\overline{A}$ |
| **AND ($A \\cdot B$)** | **2** | **3** | $A \\cdot B$ |
| **OR ($A + B$)** | **3** | **2** | $A + B$ |
| **XOR ($A \\oplus B$)** | **4** | **5** | $A'B + AB'$ |
| **XNOR ($\\overline{A \\oplus B}$)** | **5** | **4** | $AB + A'B'$ |

---

## 2. Karnaugh Map (K-Map) Simplification

Karnaugh maps organize truth tables geometrically so that adjacent cells differ in only a single literal bit (**Gray Code ordering: 00, 01, 11, 10**).

### Rules for K-Map Reduction
1. **Grouping Sizes:** Groups must be powers of 2 ($2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16$).
2. **Elimination Rule:**
   - Group of 2 (Pair) eliminates **1 variable**.
   - Group of 4 (Quad) eliminates **2 variables**.
   - Group of 8 (Octet) eliminates **3 variables**.
3. **Wrapping:** Edge cells wrap around top-to-bottom and left-to-right (e.g., 4 corners form a quad).
4. **Don't Care Conditions ($d$ or $X$):** May be included in groups if they enlarge the group size, or ignored if they do not assist reduction.

---

## 3. Combinational Logic Circuits

### Adders and Subtractors

| Circuit | Inputs | Outputs | Sum / Difference Expression | Carry / Borrow Expression | Minimum NAND Gates |
|---|:---:|:---:|---|---|:---:|
| **Half Adder** | 2 ($A, B$) | 2 ($S, C$) | $S = A \\oplus B$ | $C = A \\cdot B$ | **5** |
| **Full Adder** | 3 ($A, B, C_{\\text{in}}$) | 2 ($S, C_{\\text{out}}$) | $S = A \\oplus B \\oplus C_{\\text{in}}$ | $C_{\\text{out}} = AB + BC_{\\text{in}} + AC_{\\text{in}}$ | **9** |
| **Half Subtractor** | 2 ($A, B$) | 2 ($D, B_{\\text{out}}$) | $D = A \\oplus B$ | $B_{\\text{out}} = A' \\cdot B$ | **5** |
| **Full Subtractor** | 3 ($A, B, B_{\\text{in}}$) | 2 ($D, B_{\\text{out}}$) | $D = A \\oplus B \\oplus B_{\\text{in}}$ | $B_{\\text{out}} = A'B + (A \\oplus B)' B_{\\text{in}}$ | **9** |

> [!NOTE]
> A Full Adder can be constructed using **Two Half Adders and One OR gate**.

---

### Multiplexers and Decoders
1. **Multiplexer ($2^n \\times 1$ MUX):**
   - Has $2^n$ data inputs, $n$ selection lines, and 1 output line.
   - A $2^n \\times 1$ MUX can implement any Boolean function of $n + 1$ variables without additional gates.
2. **Decoder ($n \\times 2^n$):**
   - Converts binary code on $n$ input lines into up to $2^n$ unique output lines (minterm generator).
   - $3 \\times 8$ Decoder produces 8 minterms ($m_0$ to $m_7$).

---

## 4. Sequential Logic: Latches and Flip-Flops

### Flip-Flop Characteristic and Excitation Tables

| Flip-Flop | Characteristic Equation | Inputs | Next State $Q_{n+1}$ | State Condition |
|---|---|:---:|:---:|---|
| **SR Flip-Flop** | $Q_{n+1} = S + R' Q_n$<br/>(Constraint: $S \\cdot R = 0$) | $S=0, R=0$<br/>$S=0, R=1$<br/>$S=1, R=0$<br/>$S=1, R=1$ | $Q_n$<br/>0<br/>1<br/>**Invalid / Indeterminate** | No Change<br/>Reset<br/>Set<br/>Forbidden |
| **JK Flip-Flop** | $Q_{n+1} = J Q_n' + K' Q_n$ | $J=0, K=0$<br/>$J=0, K=1$<br/>$J=1, K=0$<br/>$J=1, K=1$ | $Q_n$<br/>0<br/>1<br/>$\\overline{Q_n}$ | No Change<br/>Reset<br/>Set<br/>**Toggle** |
| **D Flip-Flop** | $Q_{n+1} = D$ | $D=0$<br/>$D=1$ | 0<br/>1 | Reset<br/>Set (Transparent Data) |
| **T Flip-Flop** | $Q_{n+1} = T \\oplus Q_n$ | $T=0$<br/>$T=1$ | $Q_n$<br/>$\\overline{Q_n}$ | No Change<br/>**Toggle** |

### Eliminating JK Race-Around Condition
- Occurs when $J = 1, K = 1$ and clock pulse duration $t_p > \\Delta t$ (propagation delay).
- **Remedies:**
  1. **Master-Slave JK Flip-Flop:** Master triggers on positive edge, Slave on negative edge.
  2. **Edge-Triggered Flip-Flops.**
  3. Setting clock pulse width $t_p < \\Delta t$.

---

## 5. Morris Mano Basic Computer Architecture

The Basic Computer designed by M. Morris Mano consists of memory, registers, and a common bus system.

### 5.1 Basic Computer Registers and Bit-Widths

```mermaid
flowchart TD
    subgraph REGISTERS["Morris Mano Basic Computer Registers"]
        PC["Program Counter (PC): 12 Bits<br/>Holds address of next instruction"]
        AR["Address Register (AR): 12 Bits<br/>Holds address for memory access"]
        DR["Data Register (DR): 16 Bits<br/>Holds memory operand"]
        AC["Accumulator (AC): 16 Bits<br/>General purpose processor register"]
        IR["Instruction Register (IR): 16 Bits<br/>Holds instruction code being executed"]
        TR["Temporary Register (TR): 16 Bits<br/>Holds temporary internal data"]
        INPR["Input Register (INPR): 8 Bits<br/>Holds input character from keyboard"]
        OUTR["Output Register (OUTR): 8 Bits<br/>Holds output character for display"]
    end
```

- **Memory Unit:** 4096 words of 16 bits each ($4096 \\times 16$). Requires a **12-bit address bus** ($2^{12} = 4096$).
- **Common Bus System:** An 8-line common bus multiplexes data between registers using a $3 \\times 8$ decoder with selection lines $S_2, S_1, S_0$.

### 5.2 Instruction Format (16 Bits)

```text
 15    14      12  11                                  0
+----+-----------+--------------------------------------+
| I  |  Opcode   |            Address (12 Bits)         |
+----+-----------+--------------------------------------+
```
- **Bit 15 ($I$):** Addressing mode bit ($I = 0$: Direct Addressing; $I = 1$: Indirect Addressing).
- **Bits 12–14 (Opcode):** 3-bit operation code ($000$ to $111$).
  - If Opcode $\\ne 111$: **Memory-Reference Instruction**.
  - If Opcode $= 111$ and $I = 0$: **Register-Reference Instruction**.
  - If Opcode $= 111$ and $I = 1$: **Input-Output Instruction**.
- **Bits 0–11 (Address):** 12-bit memory address operand.

---

## 6. Complete Morris Mano Instruction Cycle Flowchart

The instruction cycle repeats indefinitely and consists of 4 primary phases:
1. **Fetch**
2. **Decode**
3. **Read Effective Address (if indirect)**
4. **Execute**

```mermaid
flowchart TD
    START["Start Instruction Cycle"] --> T0["T0: AR ← PC"]
    T0 --> T1["T1: IR ← M[AR], PC ← PC + 1<br/>(Fetch Instruction & Increment PC)"]
    T1 --> T2["T2: Decode Opcode (bits 12-14) into D0..D7<br/>AR ← IR(0-11), I ← IR(15)"]
    
    T2 --> CHECK_D7{"Is D7 = 1?<br/>(Opcode = 111)"}
    
    CHECK_D7 -- "No (D7 = 0: Memory Ref)" --> CHECK_I{"Is I = 1?<br/>(Indirect Mode)"}
    CHECK_I -- "Yes (I = 1)" --> T3_IND["T3: AR ← M[AR]<br/>(Read Effective Address)"]
    CHECK_I -- "No (I = 0)" --> T3_DIR["T3: Nothing<br/>(Direct Address already in AR)"]
    
    T3_IND --> EXEC_MEM["Execute Memory-Reference Instruction<br/>(AND, ADD, LDA, STA, BUN, BSA, ISZ)<br/>at T4, T5, T6"]
    T3_DIR --> EXEC_MEM
    
    CHECK_D7 -- "Yes (D7 = 1)" --> CHECK_REG_IO{"Is I = 0?"}
    CHECK_REG_IO -- "Yes (I = 0)" --> EXEC_REG["Execute Register-Reference Instruction<br/>(CLA, CLE, CMA, CME, CIR, CIL, INC, SPA, SNA, SZA, SZE, HLT)<br/>at T3"]
    CHECK_REG_IO -- "No (I = 1)" --> EXEC_IO["Execute Input-Output Instruction<br/>(INP, OUT, SKI, SKO, ION, IOF)<br/>at T3"]
    
    EXEC_MEM --> INTR_CHECK{"Interrupt Request?<br/>(R = 1 and IEN = 1)"}
    EXEC_REG --> INTR_CHECK
    EXEC_IO --> INTR_CHECK
    
    INTR_CHECK -- "Yes" --> INTR_CYCLE["Interrupt Cycle:<br/>T0': AR ← 0, TR ← PC<br/>T1': M[0] ← TR, PC ← 0<br/>T2': PC ← PC + 1, IEN ← 0, R ← 0"]
    INTR_CHECK -- "No" --> T0
    INTR_CYCLE --> T0
```

The flowchart above models the complete Morris Mano instruction cycle with hardware timing signals $T_0$ to $T_6$ and interrupt handling.

---

## 7. Addressing Modes Summary

| Addressing Mode | Effective Address ($EA$) Formula | Primary Advantage | Example Instruction |
|---|---|---|---|
| **Immediate** | Operand is part of instruction itself ($EA = \\text{None}$) | No memory access required for operand | `MOV R1, #25` |
| **Direct (Absolute)** | $EA = \\text{Address Field}$ | Simple memory reference | `LDA 2000H` |
| **Indirect** | $EA = M[\\text{Address Field}]$ | Enables pointer dereferencing and dynamic pointers | `ADD @2000H` |
| **Register** | Operand resides in named CPU Register | Fastest execution; no bus cycles | `ADD R1, R2` |
| **Register Indirect** | $EA = [\\text{Register}]$ | Fast pointer operations in loops | `MOV A, @R0` |
| **Relative (PC-Relative)**| $EA = \\text{PC} + \\text{Address Offset}$ | Position-independent code; short jump branches | `JMP +12` |
| **Indexed** | $EA = \\text{Index Register (XR)} + \\text{Address Field}$| Efficient array and table indexing | `LDA 1000H(XR)` |
| **Base Register** | $EA = \\text{Base Register (BR)} + \\text{Displacement}$ | Relocatable programs in multiprogramming OS | `MOV R1, 50(BR)` |

---

## 8. Hardwired Control Unit vs Microprogrammed Control Unit

```mermaid
flowchart LR
    subgraph HW["Hardwired Control Unit"]
        H1["Combinational Logic Gates & Decoders"] --> H2["Fastest Execution Speed"]
        H2 --> H3["Rigid; Difficult to Modify or Expand"]
        H3 --> H4["RISC Processors"]
    end
    
    subgraph MP["Microprogrammed Control Unit"]
        M1["Control Memory (ROM) storing Microinstructions"] --> M2["Slower (Memory read latency)"]
        M2 --> M3["Flexible; Easy to modify firmware"]
        M3 --> M4["CISC Processors"]
    end
```

| Feature | Hardwired Control Unit | Microprogrammed Control Unit |
|---|---|---|
| **Mechanism** | Hardware digital logic gates, multiplexers, decoders, and flip-flops. | Microprogram stored in high-speed Control Memory (ROM). |
| **Speed** | **Fastest** (direct electronic propagation delay). | Slower (requires microinstruction fetch from control store). |
| **Modifiability** | Inflexible; modifying instruction set requires hardware rewiring. | Flexible; changes achieved by updating microcode in ROM. |
| **Control Logic Complexity** | Complex for extensive instruction sets. | Systematic, structured, and modular. |
| **Typical Architecture** | **RISC** architectures. | **CISC** architectures. |
"""

UNIT04_NOTE = """---
title: "Programming Languages & Computer Graphics: C, C++, OOP, Memory Layout, and Transformations"
description: "Comprehensive guide to C/C++ memory models, pointers, dynamic allocation, OOP paradigms, vtable/vptr runtime dispatch, compilation pipeline, Bresenham line algorithm, and 2D graphics affine transformations for CST Paper 2 Unit 4."
tags:
  - "kpsc-cst"
  - "paper2"
  - "unit04"
  - "programming"
  - "cpp-oop"
  - "vtable"
  - "computer-graphics"
  - "bresenham"
syllabus_refs:
  - "P2-4.1"
  - "P2-4.2"
syllabus_refs_partial: []
last_verified: "2026-10-12"
sources:
  - "https://schooleducation.karnataka.gov.in"
  - "The C Programming Language (Kernighan & Ritchie)"
  - "Object-Oriented Programming with C++ (E. Balagurusamy)"
  - "Computer Graphics: C Version (Hearn & Baker)"
priority: "high"
---

> [!exam-focus]
> **Exam Weightage & Testing Style:** 15 questions (15 marks) in Paper 2 Unit 4. Core exam areas:
> - Pointers and memory addressing: Pointer arithmetic, `*p++` vs `(*p)++`, function pointers, dangling pointers, memory leaks.
> - Compilation & Linking stages: Preprocessor $\\to$ Compiler $\\to$ Assembler $\\to$ Linker.
> - Dynamic memory management: `malloc()` vs `calloc()` (initialises to zero) vs `realloc()`, and C++ `new` vs `delete`.
> - OOP Core: Access specifiers, Virtual functions, Pure virtual functions $\\to$ Abstract classes, Virtual base class (Diamond problem).
> - Virtual Table Mechanism: How `vtable` and `vptr` resolve runtime polymorphism in C++.
> - Computer Graphics: Raster Scan vs Random Scan (Vector) display architecture; Bresenham's Line Generation Decision parameter; 2D Affine transformations ($3 \\times 3$ homogeneous coordinate matrices).

---

## 1. C Compilation and Build Pipeline

```mermaid
flowchart LR
    SRC["Source Code<br/>(program.c)"] -->|"Preprocessor (cpp)<br/>Expands #include, #define, removes comments"| EXP["Preprocessed Code<br/>(program.i)"]
    EXP -->|"Compiler (gcc)<br/>Syntax check, translates to assembly"| ASM["Assembly Code<br/>(program.s)"]
    ASM -->|"Assembler (as)<br/>Translates mnemonics to machine opcodes"| OBJ["Object Code<br/>(program.o / .obj)"]
    OBJ -->|"Linker (ld)<br/>Resolves external symbols, merges libraries (libc)"| EXE["Executable Binary<br/>(program.exe / a.out)"]
```

The flowchart above tracks the transformation of C source text into an executable binary through preprocessing, compilation, assembly, and linking.

---

## 2. Process Memory Model & Pointers

In C and C++, variables reside in distinct virtual memory segments:
1. **Code Segment (Text):** Read-only executable binary instructions.
2. **Data Segment:** Initialised global and static variables.
3. **BSS Segment (Block Started by Symbol):** Uninitialised global and static variables (automatically zeroed by OS kernel at load time).
4. **Stack:** Local variables, function call frames, parameters, return addresses (grows downwards; LIFO order).
5. **Heap:** Dynamically allocated memory managed at runtime via `malloc`/`calloc`/`new` (grows upwards).

```mermaid
flowchart TD
    subgraph MEMORY["32-bit / 64-bit Process Virtual Address Space"]
        STACK["Stack Segment (Local variables, function frames) ↓"]
        GAP["Free Memory Space (Stack & Heap grow towards each other)"]
        HEAP["↑ Heap Segment (Dynamically allocated: malloc / new)"]
        BSS["BSS Segment (Uninitialised static & global variables)"]
        DATA["Data Segment (Initialised static & global variables)"]
        TEXT["Text / Code Segment (Executable machine instructions, Read-Only)"]
    end
    STACK --- GAP --- HEAP --- BSS --- DATA --- TEXT
```

### Dynamic Memory Allocation Functions in C vs C++

| Function / Operator | Header | Syntax | Initial Value | Return Type | Memory Freeing Mechanism |
|---|---|---|---|---|---|
| **malloc()** | `<stdlib.h>` | `ptr = (int*)malloc(n * sizeof(int));` | Indeterminate **garbage values**. | `void*` (requires explicit typecast in C++) | `free(ptr);` |
| **calloc()** | `<stdlib.h>` | `ptr = (int*)calloc(n, sizeof(int));` | All allocated bytes are **initialised to zero**. | `void*` | `free(ptr);` |
| **realloc()** | `<stdlib.h>` | `ptr = (int*)realloc(ptr, new_size);` | Preserves existing data up to minimum size. | `void*` | `free(ptr);` |
| **new / delete** | Core C++ | `int* p = new int(10);`<br/>`int* arr = new int[n];` | Calls **class constructor**; zero-initialises if requested. | Exact type pointer (Type safe) | `delete p;`<br/>`delete[] arr;` |

---

## 3. Object-Oriented Programming (OOP) in C++

### Runtime Polymorphism & Virtual Table (`vtable` / `vptr`) Mechanics

When a class declares or inherits a `virtual` function, the C++ compiler:
1. Generates a static **Virtual Method Table (`vtable`)** for that class containing pointers to its virtual functions.
2. Inserts an invisible pointer member, **`vptr`**, into every instantiated object of that class, pointing directly to that class's `vtable`.

```mermaid
flowchart LR
    subgraph OBJECT["Heap / Stack Memory"]
        OBJ_B["Base* ptr = new Derived()"]
        VPTR["Object's Hidden *vptr"]
    end
    
    subgraph VTABLE["Derived Class vtable in Static Data Segment"]
        VT_ENTRY1["vtable[0]: &Derived::show()"]
        VT_ENTRY2["vtable[1]: &Derived::print()"]
    end
    
    subgraph CODE["Code Segment"]
        FN_SHOW["Derived::show() Code"]
        FN_PRINT["Derived::print() Code"]
    end
    
    OBJ_B --> VPTR
    VPTR --> VT_ENTRY1
    VT_ENTRY1 --> FN_SHOW
    VT_ENTRY2 --> FN_PRINT
```

The flowchart above models dynamic dispatch: calling `ptr->show()` dereferences `ptr->vptr`, indexes into `vtable[0]`, and jumps to the derived method at runtime.

---

### Virtual Destructors and The Diamond Problem
- **Virtual Destructor:** Crucial when deleting a derived object via a base pointer:
  ```cpp
  class Base {
  public:
      virtual ~Base() { cout << "Base destroyed"; }
  };
  ```
  Without `virtual`, only the base class destructor is invoked, causing memory leaks for resources held by the derived class.
- **The Diamond Problem (Virtual Base Class):** When class $D$ inherits from $B$ and $C$, both of which inherit from $A$, $D$ receives two duplicate copies of $A$.
  - *Fix:* Declare inheritance using `virtual`:
    `class B : virtual public A { ... };`
    `class C : virtual public A { ... };`

---

## 4. Computer Graphics: Display Architectures & Line Drawing

### 4.1 Raster Scan vs Random Scan (Vector) Display

```mermaid
flowchart TD
    DISPLAY["Display Architectures"] --> RASTER["Raster Scan Display<br/>• Electron beam sweeps entire screen row by row (Raster)<br/>• Uses Refresh Buffer / Frame Buffer in RAM<br/>• Standard for photorealistic images, TV, monitors"]
    DISPLAY --> RANDOM["Random Scan / Vector Display<br/>• Electron beam directed ONLY to parts where lines are drawn<br/>• Uses Display Buffer containing drawing commands<br/>• High resolution lines; no aliasing (jaggies)"]
```

| Characteristic | Raster Scan Display | Random Scan (Vector / Stroke) Display |
|---|---|---|
| **Beam Deflection Pattern** | Sweeps line by line from top to bottom (Horizontal & Vertical Retrace). | Directed directly from point to point along line paths. |
| **Resolution** | Limited by pixel grid (Frame buffer resolution). | Extremely high; smooth continuous lines. |
| **Refresh Rate** | 60 to 120 frames per second (independent of picture complexity). | Depends inversely on total number of lines to be drawn. |
| **Picture Storage** | Frame Buffer (stores color/intensity for every pixel). | Display Buffer / Display File (stores vector draw commands). |
| **Aliasing (Jaggies)** | Present (requires anti-aliasing filtering). | **Absent** (straight vector lines). |

---

### 4.2 Bresenham's Line Generation Algorithm

Bresenham's algorithm uses **pure integer addition and subtraction** (no floating point arithmetic or multiplication/division) to determine the next pixel coordinates along a line with slope $0 < m < 1$.

```mermaid
flowchart TD
    START["Start: Given (x0, y0) and (x1, y1)"] --> INIT["Calculate:<br/>dx = x1 - x0, dy = y1 - y0<br/>Initial Decision Parameter: p0 = 2*dy - dx<br/>Set current pixel: (x, y) = (x0, y0)"]
    INIT --> PLOT["Plot Pixel at (x, y)"]
    PLOT --> CHECK_END{"Is x == x1?"}
    CHECK_END -- "Yes" --> DONE["Line Complete"]
    CHECK_END -- "No" --> EVAL_P{"Is pk < 0?"}
    
    EVAL_P -- "Yes (pk < 0)" --> P_NEG["Next pixel: (x + 1, y)<br/>pk+1 = pk + 2*dy"]
    EVAL_P -- "No (pk >= 0)" --> P_POS["Next pixel: (x + 1, y + 1)<br/>pk+1 = pk + 2*dy - 2*dx"]
    
    P_NEG --> SET_NEXT["Update x = x + 1"]
    P_POS --> SET_NEXT_Y["Update x = x + 1, y = y + 1"]
    SET_NEXT --> PLOT
    SET_NEXT_Y --> PLOT
```

The flowchart above traces Bresenham's integer decision loop. Because it avoids floating-point operations, it is significantly faster than the Digital Differential Analyzer (DDA) algorithm.

---

## 5. 2D Computer Graphics Affine Transformations

In computer graphics, affine transformations in 2D Euclidean space are represented as matrix operations using **$3 \\times 3$ homogeneous coordinate matrices**.

### Homogeneous Transformation Matrices

1. **Translation ($T_{t_x, t_y}$):**
   $$\\begin{bmatrix} x' \\\\ y' \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} 1 & 0 & t_x \\\\ 0 & 1 & t_y \\\\ 0 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\\\ 1 \\end{bmatrix}$$

2. **Scaling ($S_{s_x, s_y}$):**
   $$\\begin{bmatrix} x' \\\\ y' \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} s_x & 0 & 0 \\\\ 0 & s_y & 0 \\\\ 0 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\\\ 1 \\end{bmatrix}$$

3. **Rotation ($R_\\theta$ Counter-Clockwise about Origin):**
   $$\\begin{bmatrix} x' \\\\ y' \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta & 0 \\\\ \\sin\\theta & \\cos\\theta & 0 \\\\ 0 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\\\ 1 \\end{bmatrix}$$
"""

UNIT05_NOTE = """---
title: "Database Management Systems: Relational Model, Normalization, 2PL, and ACID Transactions"
description: "Comprehensive guide to keys, functional dependencies, normal forms (1NF to BCNF), decomposition tests, transaction state transitions, Two-Phase Locking (2PL), serializability precedence graphs, and ACID properties for CST Paper 2 Unit 5."
tags:
  - "kpsc-cst"
  - "paper2"
  - "unit05"
  - "dbms"
  - "normalization"
  - "transactions"
  - "two-phase-locking"
  - "serializability"
syllabus_refs:
  - "P2-5.1"
  - "P2-5.2"
  - "P2-5.3"
syllabus_refs_partial: []
last_verified: "2026-10-12"
sources:
  - "https://schooleducation.karnataka.gov.in"
  - "Database System Concepts (Silberschatz, Korth, Sudarshan, 7th Ed)"
  - "Fundamentals of Database Systems (Elmasri & Navathe)"
priority: "high"
---

> [!exam-focus]
> **Exam Weightage & Testing Style:** 15 questions (15 marks) in Paper 2 Unit 5. Frequently tested areas:
> - Keys hierarchy: Super Key $\\supseteq$ Candidate Key. Primary Key cannot be NULL (Entity Integrity).
> - Foreign Key constraint: References a Primary Key; enforces Referential Integrity.
> - Computing Attribute Closure $X^+$ and finding minimal Candidate Keys.
> - Distinguishing normal forms:
>   - 1NF: Atomic attribute values.
>   - 2NF: 1NF + No partial dependencies (every non-prime attribute fully functionally dependent on whole key).
>   - 3NF: 2NF + No transitive dependencies (for $X \\to Y$, $X$ is super key OR $Y$ is prime attribute).
>   - BCNF: For every non-trivial $X \\to Y$, $X$ **must be a Super Key**.
> - Transaction State Transitions: Active $\\to$ Partially Committed $\\to$ Committed; Active $\\to$ Failed $\\to$ Aborted.
> - Concurrency Control: Two-Phase Locking (2PL: Growing phase & Shrinking phase), Strict 2PL, Rigorous 2PL, and Conflict Serializability Precedence Graphs.

---

## 1. Relational Keys and Integrity Constraints

```mermaid
flowchart TD
    SK["Super Key<br/>Any set of attributes uniquely identifying a tuple"] --> CK["Candidate Key<br/>Minimal Super Key (no redundant attributes)"]
    CK --> PK["Primary Key<br/>Chosen Candidate Key (Unique & NOT NULL)"]
    CK --> AK["Alternate Key<br/>Candidate Keys not selected as Primary Key"]
    PK -.-> FK["Foreign Key<br/>Points to Primary Key of another relation"]
```

The flowchart above models the key hierarchy in relational database theory.

### Integrity Constraints Summary

| Constraint Name | Rule & Formal Definition | Violation Example |
|---|---|---|
| **Entity Integrity** | Primary key attributes cannot contain **NULL values** (since NULL cannot identify a unique tuple). | Inserting a student record with `RollNo = NULL`. |
| **Referential Integrity** | A Foreign Key in a child table must either match a valid Primary Key in the parent table or be entirely NULL. | Inserting an `Order` with `CustomerID = 999` when no customer with ID 999 exists. |
| **Domain Integrity** | All values in a column must adhere to the defined data type, format, and range. | Entering `"ABC"` into an `Age` integer field. |

---

## 2. Functional Dependencies & Attribute Closure

Given a relation $R$, a **Functional Dependency (FD)** $X \\to Y$ states that whenever two tuples have the same value for attribute set $X$, they must also have the same value for attribute set $Y$.
- **Trivial FD:** $X \\to Y$ where $Y \\subseteq X$ (e.g., $A B \\to A$).
- **Non-Trivial FD:** $X \\to Y$ where $Y \\not\\subseteq X$ (e.g., $A \\to B$).

### Armstrong's Axioms (Sound and Complete)
1. **Reflexivity:** If $Y \\subseteq X$, then $X \\to Y$.
2. **Augmentation:** If $X \\to Y$, then $X Z \\to Y Z$.
3. **Transitivity:** If $X \\to Y$ and $Y \\to Z$, then $X \\to Z$.

---

## 3. Database Normalization (1NF, 2NF, 3NF, BCNF)

Normalization systematically decomposes tables to eliminate redundancy and prevent **insertion, deletion, and update anomalies**.

```mermaid
flowchart TD
    R["Unnormalized Relation"] --> N1["1NF: Atomic values only (no repeating groups/arrays)"]
    N1 --> N2["2NF: 1NF + No Partial Dependency<br/>(No non-prime attribute depends on subset of candidate key)"]
    N2 --> N3["3NF: 2NF + No Transitive Dependency<br/>(For X → Y, X is Super Key OR Y is Prime Attribute)"]
    N3 --> BCNF["BCNF: Boyce-Codd Normal Form<br/>(For every non-trivial X → Y, X must be a Super Key)"]
```

### Comparative Normal Form Evaluation Table

| Normal Form | Formal Condition for every non-trivial $X \\to Y$ | Anomalies Eliminated | Always Dependency Preserving? |
|---|---|---|:---:|
| **1NF** | Attribute values must be single atomic values. | Repeating groups, nested tables. | Yes |
| **2NF** | In 1NF and no non-prime attribute is partially dependent on any candidate key. | Partial key redundancy. | Yes |
| **3NF** | In 2NF and for every $X \\to Y$, either **$X$ is a Super Key** OR **$Y$ is a Prime Attribute** (part of a candidate key). | Transitive dependencies ($A \\to B \\to C$). | **Yes** (Lossless join & dependency preservation always achievable). |
| **BCNF** | For every non-trivial $X \\to Y$, **$X$ must be a Super Key**. | Redundancy due to functional dependencies where LHS is not a candidate key. | **No** (BCNF decomposition is always lossless, but may not preserve dependencies). |

---

## 4. Transaction Management & State Transitions

A **transaction** is a logical unit of database processing that includes one or more database access operations.

```mermaid
flowchart TD
    ACT["Active<br/>(Initial state; executing read/write operations)"] --> PART["Partially Committed<br/>(After final statement has executed)"]
    PART -->|"Commit Operation successful"| COMM["Committed<br/>(Changes permanent on disk)"]
    
    PART -->|"Failure during commit"| FAIL["Failed<br/>(Normal execution can no longer proceed)"]
    ACT -->|"Hardware / Logical Failure"| FAIL
    
    FAIL -->|"Rollback & undo changes"| ABORT["Aborted<br/>(Database restored to state prior to transaction)"]
    ABORT --> TERM["Terminated"]
    COMM --> TERM
```

The flowchart above outlines the standard 5 transaction lifecycle states. Once in the *Committed* state, changes cannot be rolled back.

---

## 5. Concurrency Control: Two-Phase Locking (2PL)

To ensure **conflict serializability**, transactions acquire shared ($S$) and exclusive ($X$) locks according to the Two-Phase Locking protocol:

```mermaid
flowchart LR
    subgraph PHASE1["1. Growing / Expanding Phase"]
        L1["Transaction may acquire new locks"]
        L2["Transaction CANNOT release any lock"]
    end
    
    subgraph LOCK_PT["Lock Point"]
        LP["Instant when transaction acquires its final lock"]
    end
    
    subgraph PHASE2["2. Shrinking Phase"]
        L3["Transaction may release locks"]
        L4["Transaction CANNOT acquire any new lock"]
    end
    
    PHASE1 --> LOCK_PT --> PHASE2
```

### Variations of 2PL Protocols

| 2PL Variant | Locking Rule | Cascading Rollback Free? | Deadlock Free? |
|---|---|:---:|:---:|
| **Basic 2PL** | Locks acquired in growing phase, released in shrinking phase. | No | No |
| **Strict 2PL** | All **Exclusive ($X$) locks** held until transaction commits or aborts. | **Yes** (Avoids cascading aborts) | No |
| **Rigorous 2PL** | **ALL locks (Shared and Exclusive)** held until transaction commits or aborts. | **Yes** | No |
| **Conservative 2PL** | Acquires **all required locks prior to starting execution**; if any lock unavailable, waits without holding any. | Yes | **Yes (Deadlock Free)** |

---

## 6. Conflict Serializability & Precedence Graph

A schedule $S$ of transactions is **conflict serializable** if it is conflict equivalent to some serial schedule.
- Two operations conflict if:
  1. They belong to different transactions.
  2. They access the same data item $Q$.
  3. At least one of the operations is a **Write($Q$)**.

```mermaid
flowchart TD
    SG["Precedence Graph / Serialization Graph"] --> NODES["Nodes: Represent active transactions (T1, T2, ... Tn)"]
    SG --> EDGES["Directed Edge Ti → Tj:<br/>If Ti executes a conflicting operation before Tj"]
    SG --> TEST{"Does the graph contain a CYCLE?"}
    TEST -- "Yes (Cycle Detected)" --> NOT_SER["Schedule is NOT Conflict Serializable (Potential Inconsistency)"]
    TEST -- "No (Acyclic Graph)" --> SER["Schedule IS Conflict Serializable (Equivalent to Topological Sort order)"]
```
"""

UNIT06_NOTE = """---
title: "Operating Systems: Process Scheduling, Deadlocks, RAG, and Virtual Memory"
description: "Comprehensive guide to 7-state process lifecycles, CPU scheduling algorithms, Coffman conditions, Resource Allocation Graph (RAG) deadlock detection, Banker's algorithm, and page replacement strategies for CST Paper 2 Unit 6."
tags:
  - "kpsc-cst"
  - "paper2"
  - "unit06"
  - "operating-systems"
  - "cpu-scheduling"
  - "deadlocks"
  - "rag-deadlock"
  - "virtual-memory"
syllabus_refs:
  - "P2-6.1"
  - "P2-6.2"
  - "P2-6.3"
syllabus_refs_partial: []
last_verified: "2026-10-12"
sources:
  - "https://schooleducation.karnataka.gov.in"
  - "Operating System Concepts (Silberschatz, Galvin, Gagne, 10th Ed)"
priority: "high"
---

> [!exam-focus]
> **Exam Weightage & Testing Style:** 15 questions (15 marks) in Paper 2 Unit 6. High-yield numericals and conceptual traps:
> - Average Turnaround Time (TAT) and Average Waiting Time (WT):
>   $$\\text{TAT} = \\text{Completion Time (CT)} - \\text{Arrival Time (AT)}$$
>   $$\\text{WT} = \\text{Turnaround Time (TAT)} - \\text{Burst Time (BT)}$$
> - Shortest Remaining Time First (SRTF) is optimal for minimizing average waiting time among preemptive schedulers.
> - The 4 Coffman conditions required for Deadlock to occur.
> - Resource Allocation Graph (RAG): Cycle detection rule (Single instance resource cycle $\\implies$ Definite Deadlock).
> - Banker's Algorithm: Need matrix computation ($\\text{Need} = \\text{Max} - \\text{Allocation}$) and finding a Safe Sequence.
> - Belady's Anomaly: Occurs in **FIFO** page replacement where increasing page frames leads to *more* page faults.

---

## 1. 7-State Process Transition Model

A **process** moves through various execution states managed by the operating system kernel:

```mermaid
flowchart TD
    NEW["New<br/>Created on disk"] -->|"Admitted (Long Term Scheduler)"| READY["Ready<br/>In RAM waiting for CPU"]
    READY -->|"Scheduler Dispatch"| RUN["Running<br/>Executing on CPU"]
    RUN -->|"Interrupt / Time Quantum expired"| READY
    RUN -->|"I/O or Event Wait"| WAIT["Blocked / Waiting<br/>Waiting for I/O completion"]
    WAIT -->|"I/O completed"| READY
    RUN -->|"Exit / Complete"| TERM["Terminated<br/>Deallocated"]
    
    READY -->|"Memory Full (Medium Term Scheduler)"| READY_SUSP["Ready Suspended<br/>Swapped out to secondary disk"]
    READY_SUSP -->|"Memory available"| READY
    
    WAIT -->|"Memory Full (Medium Term Scheduler)"| WAIT_SUSP["Blocked Suspended<br/>Swapped out to secondary disk"]
    WAIT_SUSP -->|"I/O complete while swapped"| READY_SUSP
    WAIT_SUSP -->|"Memory available"| WAIT
```

The flowchart above models the complete 7-state process lifecycle including swapping by the Medium-Term Scheduler.

---

## 2. CPU Scheduling Algorithms Comparison

| Algorithm | Preemption Mode | Scheduling Criteria | Advantages | Disadvantages & Pitfalls |
|---|---|---|---|---|
| **First-Come, First-Served (FCFS)** | Non-preemptive | Arrival Time ($AT$) | Simple, zero overhead. | **Convoy Effect:** Short processes trapped behind long CPU-intensive jobs, inflating average waiting time. |
| **Shortest Job First (SJF)** | Non-preemptive | Burst Time ($BT$) | **Provably optimal** for minimum average waiting time among non-preemptive schedulers. | Starvation of longer jobs; impossible to know exact future burst time in general OS. |
| **Shortest Remaining Time First (SRTF)** | **Preemptive** | Remaining Burst Time | Optimal average waiting time for preemptive systems. | Frequent context-switch overhead; high starvation risk for long processes. |
| **Round Robin (RR)** | **Preemptive** | Time Quantum ($q$) | Fair; responsive in time-sharing interactive systems; starvation-free. | If $q \\to \\infty$, behaves like FCFS. If $q$ is too small, context-switching overhead degrades CPU throughput. |
| **Priority Scheduling** | Preemptive or Non-preemptive | Priority integer | High-priority processes execute first. | **Starvation (indefinite blocking)** of low-priority tasks. Solved by **Aging** (gradually increasing priority over time). |

---

## 3. Deadlocks & Resource Allocation Graph (RAG)

A **deadlock** is a state where every process in a set is waiting for an event that can be caused only by another process in the set.

### 3.1 The Four Coffman Conditions
1. **Mutual Exclusion:** Resources cannot be shared simultaneously.
2. **Hold and Wait:** Process holds at least one resource while waiting for others.
3. **No Preemption:** Resources cannot be forcibly taken from a process.
4. **Circular Wait:** Closed chain of processes exists where each waits for a resource held by the next.

### 3.2 Resource Allocation Graph (RAG) Deadlock Cycle

```mermaid
flowchart LR
    P1((Process P1))
    P2((Process P2))
    R1[Resource R1]
    R2[Resource R2]
    
    R1 -->|"Allocated to"| P1
    P1 -->|"Requests / Waits for"| R2
    R2 -->|"Allocated to"| P2
    P2 -->|"Requests / Waits for"| R1
```

The diagram above models a Resource Allocation Graph cycle.
- **Single Instance per Resource Type:** A cycle in the graph is a **necessary AND sufficient condition** for Deadlock.
- **Multiple Instances per Resource Type:** A cycle is a **necessary condition, but NOT sufficient** (other processes with available instances might break the cycle).

---

## 4. Multilevel Feedback Queue (MLFQ) Scheduling Pipeline

```mermaid
flowchart TD
    NEW_PROC["New Process Arrives"] --> Q0["Queue 0: Round Robin (Time Quantum = 8 ms)<br/>Highest Priority"]
    Q0 -->|"Completes within 8 ms"| DONE["Finished"]
    Q0 -->|"CPU burst > 8 ms (Demoted)"| Q1["Queue 1: Round Robin (Time Quantum = 16 ms)<br/>Medium Priority"]
    Q1 -->|"Completes within 16 ms"| DONE
    Q1 -->|"CPU burst > 16 ms (Demoted)"| Q2["Queue 2: FCFS<br/>Lowest Priority"]
    Q2 --> DONE
    
    Q2 -.->|"Aging: Starving processes promoted upwards"| Q0
```

The flowchart above models an adaptive Multilevel Feedback Queue. Interactive short CPU tasks finish rapidly in $Q_0$, while long compute-bound jobs sink to lower priority queues without starving thanks to periodic Aging.

---

## 5. Virtual Memory & Page Replacement

### Comparative Page Replacement Matrix

| Algorithm | Decision Criteria | Belady's Anomaly Susceptible? | Performance & Implementability |
|---|---|:---:|---|
| **FIFO (First-In, First-Out)** | Replaces the page that entered memory earliest. | **YES (Susceptible)** | Simple to implement using a queue; exhibits poor locality of reference. |
| **Optimal (OPT / MIN)** | Replaces the page that will **not be used for the longest period in the future**. | **NO** (Stack algorithm) | **Theoretical benchmark** producing minimum page faults; unimplementable in real systems. |
| **LRU (Least Recently Used)** | Replaces the page that has **not been referenced for the longest period in the past**. | **NO** (Stack algorithm) | Excellent performance; approximates OPT; implemented via hardware timestamping or reference stack. |
"""

UNIT09_NOTE = """---
title: "Computer Networks: OSI Model, TCP 3-Way Handshake, and IPv4 Subnetting"
description: "Comprehensive guide to the OSI 7-layer hierarchy, protocol encapsulation, TCP connection establishment and teardown sequence diagrams, UDP mechanics, IPv4 addressing, and CIDR subnetting for CST Paper 2 Unit 9."
tags:
  - "kpsc-cst"
  - "paper2"
  - "unit09"
  - "computer-networks"
  - "osi-model"
  - "tcp-handshake"
  - "subnetting"
syllabus_refs:
  - "P2-9.1"
  - "P2-9.2"
  - "P2-9.3"
syllabus_refs_partial: []
last_verified: "2026-10-12"
sources:
  - "https://schooleducation.karnataka.gov.in"
  - "Computer Networks (Andrew S. Tanenbaum, 6th Ed)"
  - "Data Communications and Networking (Behrouz A. Forouzan)"
priority: "high"
---

> [!exam-focus]
> **Exam Weightage & Testing Style:** 15 questions (15 marks) in Paper 2 Unit 9. Frequent numerical and protocol questions:
> - OSI layer functionality: Encryption/Compression at Presentation; Dialog control at Session; Process-to-process delivery at Transport; Routing at Network; Framing and MAC at Data Link.
> - Data units (PDU): Bits $\\to$ Frames $\\to$ Packets $\\to$ Segments $\\to$ Data.
> - TCP 3-Way Handshake ($SYN \\to SYN-ACK \\to ACK$) and Connection Teardown ($FIN \\to ACK \\to FIN \\to ACK$).
> - Subnetting calculations: Finding Network Address, Broadcast Address, and number of usable hosts ($2^H - 2$).
> - Address Resolution Protocol (ARP): Maps logical IP address to physical MAC address.

---

## 1. The OSI 7-Layer Reference Model and PDU Encapsulation

```mermaid
flowchart TD
    L7["7. Application Layer: User services (HTTP, FTP, DNS)"] -->|"PDU: Data"| L6["6. Presentation Layer: Encryption, Compression, Translation"]
    L6 -->|"PDU: Data"| L5["5. Session Layer: Dialog control, Synchronization"]
    L5 -->|"PDU: Data"| L4["4. Transport Layer: End-to-End delivery (TCP, UDP)"]
    L4 -->|"PDU: Segment"| L3["3. Network Layer: Logical IP routing (Routers)"]
    L3 -->|"PDU: Packet"| L2["2. Data Link Layer: Framing & MAC addressing (Switches)"]
    L2 -->|"PDU: Frame"| L1["1. Physical Layer: Raw bit stream over physical cable (Hubs)"]
```

The flowchart above models the OSI layered protocol stack and Protocol Data Unit (PDU) encapsulation hierarchy.

---

## 2. TCP 3-Way Handshake & Connection Teardown Sequence

TCP provides a **reliable, full-duplex, connection-oriented** transport stream using sequence and acknowledgement numbers.

### 2.1 Connection Establishment (3-Way Handshake)

```mermaid
sequenceDiagram
    autonumber
    actor Client as TCP Client
    actor Server as TCP Server
    
    Note over Client,Server: Client in CLOSED state; Server in LISTEN state
    Client->>Server: SYN (Seq = x) [SYN_SENT]
    Note over Server: Server receives SYN; transitions to SYN_RCVD
    Server->>Client: SYN-ACK (Seq = y, Ack = x + 1)
    Note over Client: Client receives SYN-ACK; transitions to ESTABLISHED
    Client->>Server: ACK (Seq = x + 1, Ack = y + 1)
    Note over Server: Server receives ACK; transitions to ESTABLISHED
    Note over Client,Server: Connection Established; Full-Duplex Data Transfer begins
```

The sequence diagram above illustrates the 3-Way Handshake protocol establishing synchronized sequence numbers.

### 2.2 Connection Teardown (4-Way Handshake)

```mermaid
sequenceDiagram
    autonumber
    actor Client as TCP Client
    actor Server as TCP Server
    
    Client->>Server: FIN (Seq = u) [Client enters FIN_WAIT_1]
    Server->>Client: ACK (Ack = u + 1) [Server enters CLOSE_WAIT; Client enters FIN_WAIT_2]
    Note over Server: Server finishes transmitting remaining buffered data
    Server->>Client: FIN (Seq = v) [Server enters LAST_ACK]
    Client->>Server: ACK (Ack = v + 1) [Client enters TIME_WAIT (2MSL timer)]
    Note over Server: Server receives ACK; transitions to CLOSED
    Note over Client: Client timer expires; transitions to CLOSED
```

The sequence diagram above models the graceful bidirectional teardown ensuring zero lost data.

---

## 3. TCP vs UDP Comparison

| Feature | Transmission Control Protocol (TCP) | User Datagram Protocol (UDP) |
|---|---|---|
| **Connection Type** | **Connection-Oriented** (Requires 3-Way Handshake). | **Connectionless** (Sends datagrams immediately). |
| **Reliability** | **Reliable** (Guaranteed delivery via ACKs and retransmissions). | **Unreliable / Best Effort** (No ACKs; packets may be lost or disordered). |
| **Header Size** | 20 to 60 Bytes (Minimum 20 bytes). | Fixed **8 Bytes**. |
| **Speed / Overhead** | Slower due to flow control, congestion control, and ACK tracking. | Extremely fast, lightweight, minimal overhead. |
| **Typical Use Cases** | Web browsing (HTTP/HTTPS), File transfer (FTP), Email (SMTP), SSH. | Real-time streaming (VoIP, YouTube live), Video games, DNS queries, DHCP. |

---

## 4. IPv4 Addressing & CIDR Subnetting Calculations

An IPv4 address is a **32-bit logical address** expressed in dotted decimal format consisting of four 8-bit octets ($X.X.X.X$).

| Class | Leading Bits | 1st Octet Range | Default Subnet Mask | Network Bits ($N$) / Host Bits ($H$) | Usable Hosts per Network |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Class A** | `0` | 1 – 126 | `255.0.0.0` (/8) | $N=8, H=24$ | $2^{24} - 2 = 16,777,214$ |
| **Class B** | `10` | 128 – 191 | `255.255.0.0` (/16) | $N=16, H=16$ | $2^{16} - 2 = 65,534$ |
| **Class C** | `110` | 192 – 223 | `255.255.255.0` (/24) | $N=24, H=8$ | $2^8 - 2 = 254$ |
| **Class D** | `1110` | 224 – 239 | — | — | **Multicasting** |
| **Class E** | `1111` | 240 – 255 | — | — | Experimental / Research |

- **Subnetting Formula:** For a `/N` prefix, Host bits $H = 32 - N$.
  $$\\mathbf{\\text{Usable Hosts} = 2^H - 2}$$
  *(1st address is Network Address; last address is Directed Broadcast Address).*
"""

def main():
    notes = [
        (os.path.join(AGY_ROOT, "03_Notes", "Paper2", "Unit03_Computer_Architecture", "Digital_Logic_and_Combinational_Circuits.md"), UNIT03_NOTE),
        (os.path.join(AGY_ROOT, "03_Notes", "Paper2", "Unit04_Programming_and_Graphics", "C_and_CPP_Core_Concepts.md"), UNIT04_NOTE),
        (os.path.join(AGY_ROOT, "03_Notes", "Paper2", "Unit05_DBMS", "Relational_Model_and_Normalization.md"), UNIT05_NOTE),
        (os.path.join(AGY_ROOT, "03_Notes", "Paper2", "Unit06_Operating_Systems", "Process_Scheduling_and_Deadlocks.md"), UNIT06_NOTE),
        (os.path.join(AGY_ROOT, "03_Notes", "Paper2", "Unit09_Networks_and_Communication", "OSI_Model_and_IP_Subnetting.md"), UNIT09_NOTE),
    ]
    
    for path, content in notes:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\\n")
        print(f"Updated: {path}")

if __name__ == "__main__":
    main()
