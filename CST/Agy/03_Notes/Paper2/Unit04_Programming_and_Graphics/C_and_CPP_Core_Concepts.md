---
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
> - Compilation & Linking stages: Preprocessor $\to$ Compiler $\to$ Assembler $\to$ Linker.
> - Dynamic memory management: `malloc()` vs `calloc()` (initialises to zero) vs `realloc()`, and C++ `new` vs `delete`.
> - OOP Core: Access specifiers, Virtual functions, Pure virtual functions $\to$ Abstract classes, Virtual base class (Diamond problem).
> - Virtual Table Mechanism: How `vtable` and `vptr` resolve runtime polymorphism in C++.
> - Computer Graphics: Raster Scan vs Random Scan (Vector) display architecture; Bresenham's Line Generation Decision parameter; 2D Affine transformations ($3 \times 3$ homogeneous coordinate matrices).

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

The diagram above visualizes the core architecture, sequence flow, and structural taxonomy for systematic review.

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

In computer graphics, affine transformations in 2D Euclidean space are represented as matrix operations using **$3 \times 3$ homogeneous coordinate matrices**.

### Homogeneous Transformation Matrices

1. **Translation ($T_{t_x, t_y}$):**
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

2. **Scaling ($S_{s_x, s_y}$):**
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

3. **Rotation ($R_\theta$ Counter-Clockwise about Origin):**
   $$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$\n
