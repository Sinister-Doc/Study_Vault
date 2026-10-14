# -*- coding: utf-8 -*-
"""
Generate complete 150 distinct, syllabus-locked, authentic questions for Paper 2 Test 2.
Units:
U1: Fundamentals of Computers (15 Qs: Q1 to Q15)
U2: Digital Logic & Computer Organization (15 Qs: Q16 to Q30)
U3: Programming with C & C++ (15 Qs: Q31 to Q45)
U4: Data Structures & Algorithms (15 Qs: Q46 to Q60)
U5: Database Management Systems (15 Qs: Q61 to Q75)
U6: Operating Systems & System Programming (15 Qs: Q76 to Q90)
U7: Computer Networks & Data Communication (15 Qs: Q91 to Q105)
U8: Software Engineering & OOAD (15 Qs: Q106 to Q120)
U9: Web Technologies & Internet Applications (15 Qs: Q121 to Q135)
U10: Information Security & Emerging Trends (15 Qs: Q136 to Q150)
Total = 150 Questions.
"""

def get_paper2_test2_questions():
    qs = []

    # ----------------------------------------------------
    # UNIT 1: FUNDAMENTALS OF COMPUTERS (15 QUESTIONS: Q1 to Q15)
    # ----------------------------------------------------
    u1 = [
        {
            "id": "P2-T2-U1-01", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Which functional unit of the computer system coordinates and synchronizes all hardware operations by issuing timing and control signals?",
            "options": [{"label": "A", "text": "Control Unit (CU)"}, {"label": "B", "text": "Arithmetic Logic Unit (ALU)"}, {"label": "C", "text": "Memory Unit"}, {"label": "D", "text": "Input Interface"}],
            "answer": "A",
            "explanation": "The Control Unit acts as the supervisor of the CPU, decoding instructions and directing the data flow across registers, ALU, and buses."
        },
        {
            "id": "P2-T2-U1-02", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.2",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Convert the decimal number (147)₁₀ into its equivalent binary number:",
            "options": [{"label": "A", "text": "(10010011)₂"}, {"label": "B", "text": "(10010111)₂"}, {"label": "C", "text": "(10110011)₂"}, {"label": "D", "text": "(11010011)₂"}],
            "answer": "A",
            "explanation": "147 = 128 + 16 + 2 + 1 = 2⁷ + 2⁴ + 2¹ + 2⁰ = (10010011)₂."
        },
        {
            "id": "P2-T2-U1-03", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the 1's complement of the binary number (10110100)₂?",
            "options": [{"label": "A", "text": "01001011"}, {"label": "B", "text": "01001100"}, {"label": "C", "text": "11001011"}, {"label": "D", "text": "01101011"}],
            "answer": "A",
            "explanation": "1's complement is obtained by bitwise inversion: 1 becomes 0, and 0 becomes 1. Inverting 10110100 yields 01001011."
        },
        {
            "id": "P2-T2-U1-04", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "In IEEE 754 Double-Precision Floating-Point standard (64 bits), how many bits are allocated to the exponent, and what is the exponent bias?",
            "options": [{"label": "A", "text": "11 bits exponent, bias 1023"}, {"label": "B", "text": "8 bits exponent, bias 127"}, {"label": "C", "text": "12 bits exponent, bias 2047"}, {"label": "D", "text": "10 bits exponent, bias 511"}],
            "answer": "A",
            "explanation": "IEEE 754 double precision allocates 1 sign bit, 11 exponent bits (bias = 2¹⁰ - 1 = 1023), and 52 fraction/mantissa bits."
        },
        {
            "id": "P2-T2-U1-05", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "In a 2-level memory hierarchy, cache access time is 5 ns and main memory access time is 80 ns. What must be the minimum cache hit ratio to achieve an AMAT of at most 8 ns?",
            "options": [{"label": "A", "text": "0.9625 (96.25%)"}, {"label": "B", "text": "0.9000 (90%)"}, {"label": "C", "text": "0.9250 (92.5%)"}, {"label": "D", "text": "0.9500 (95%)"}],
            "answer": "A",
            "explanation": "AMAT = Hit Time + (1 - H) * Miss Penalty => 8 = 5 + (1 - H)*80 => 3 = 80*(1 - H) => 1 - H = 3/80 = 0.0375 => H = 0.9625 (96.25%)."
        },
        {
            "id": "P2-T2-U1-06", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.1",
            "origin_tag": "PYQ - KPSC CST 2015", "label": "PYQ", "difficulty": "easy",
            "text": "The ENIAC (Electronic Numerical Integrator and Computer) developed by Mauchly and Eckert belongs to which generation of computers?",
            "options": [{"label": "A", "text": "First Generation (Vacuum Tubes)"}, {"label": "B", "text": "Second Generation"}, {"label": "C", "text": "Third Generation"}, {"label": "D", "text": "Fourth Generation"}],
            "answer": "A",
            "explanation": "ENIAC (1946) was a pioneering First Generation computer built with over 17,000 vacuum tubes."
        },
        {
            "id": "P2-T2-U1-07", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which type of semiconductor RAM requires periodic refresh cycles to maintain stored capacitive charge?",
            "options": [{"label": "A", "text": "Dynamic RAM (DRAM)"}, {"label": "B", "text": "Static RAM (SRAM)"}, {"label": "C", "text": "Mask ROM"}, {"label": "D", "text": "Flash EEPROM"}],
            "answer": "A",
            "explanation": "DRAM cells store data as charge in a tiny capacitor (1 transistor + 1 capacitor) which leaks charge, necessitating periodic refresh cycles."
        },
        {
            "id": "P2-T2-U1-08", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Convert the octal number (357)₈ into its equivalent hexadecimal representation:",
            "options": [{"label": "A", "text": "EF"}, {"label": "B", "text": "DF"}, {"label": "C", "text": "E7"}, {"label": "D", "text": "CF"}],
            "answer": "A",
            "explanation": "(357)₈ to binary: 3=011, 5=101, 7=111 => 011101111₂. Grouping in 4s from right: 1110 1111 = (EF)₁₆."
        },
        {
            "id": "P2-T2-U1-09", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the maximum signed integer value that can be represented using an 8-bit register in 2's complement notation?",
            "options": [{"label": "A", "text": "+127"}, {"label": "B", "text": "+128"}, {"label": "C", "text": "+255"}, {"label": "D", "text": "+63"}],
            "answer": "A",
            "explanation": "An n-bit 2's complement register represents numbers from -(2ⁿ⁻¹) to +(2ⁿ⁻¹ - 1). For n=8, the range is -128 to +127."
        },
        {
            "id": "P2-T2-U1-10", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which computer bus is unidirectional, carrying memory locations exclusively from the CPU to memory/IO devices?",
            "options": [{"label": "A", "text": "Address Bus"}, {"label": "B", "text": "Data Bus"}, {"label": "C", "text": "Control Bus"}, {"label": "D", "text": "Power Bus"}],
            "answer": "A",
            "explanation": "The Address Bus is unidirectional (CPU -> Memory/IO), while the Data Bus is bidirectional."
        },
        {
            "id": "P2-T2-U1-11", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In a direct-mapped cache, how many blocks of main memory map to a specific cache line?",
            "options": [{"label": "A", "text": "Multiple main memory blocks map to the same cache line via modulo indexing"}, {"label": "B", "text": "Only exactly one block per cache line"}, {"label": "C", "text": "Any block can map to any cache line"}, {"label": "D", "text": "Zero blocks"}],
            "answer": "A",
            "explanation": "In direct-mapped cache, Line = (Block Address) mod (Total Cache Lines). Multiple blocks share the same cache line, distinguished by Tag bits."
        },
        {
            "id": "P2-T2-U1-12", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the BCD (Binary Coded Decimal) representation of the decimal number 89?",
            "options": [{"label": "A", "text": "1000 1001"}, {"label": "B", "text": "0101 1001"}, {"label": "C", "text": "1000 1000"}, {"label": "D", "text": "1001 1000"}],
            "answer": "A",
            "explanation": "In BCD, each decimal digit is encoded in 4-bit binary: 8 = 1000 and 9 = 1001, giving 1000 1001."
        },
        {
            "id": "P2-T2-U1-13", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which magnetic storage device allows purely sequential (serial) access to stored records?",
            "options": [{"label": "A", "text": "Magnetic Tape"}, {"label": "B", "text": "Hard Disk Drive"}, {"label": "C", "text": "Floppy Disk"}, {"label": "D", "text": "CD-ROM"}],
            "answer": "A",
            "explanation": "Magnetic tape is a sequential access medium (must wind through preceding data); disks and SSDs provide direct/random access."
        },
        {
            "id": "P2-T2-U1-14", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "A byte-addressable computer system has a 32-bit physical address. If the cache size is 64 KB with 32-byte block size in a 4-way set associative cache, how many tag bits are required?",
            "options": [{"label": "A", "text": "18 bits"}, {"label": "B", "text": "19 bits"}, {"label": "C", "text": "14 bits"}, {"label": "D", "text": "16 bits"}],
            "answer": "A",
            "explanation": "Block offset = log2(32) = 5 bits. Cache lines = 64KB / 32B = 2048 lines. Sets = 2048 / 4 = 512 sets => Set index = log2(512) = 9 bits. Tag bits = 32 - (9 + 5) = 18 bits."
        },
        {
            "id": "P2-T2-U1-15", "paper": 2, "section_id": "U1", "subject": "Fundamentals of Computers", "syllabus_id": "P2-1.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "What is the ASCII character code value for uppercase letter 'A' in decimal?",
            "options": [{"label": "A", "text": "65"}, {"label": "B", "text": "97"}, {"label": "C", "text": "48"}, {"label": "D", "text": "66"}],
            "answer": "A",
            "explanation": "In 7-bit ASCII: 'A' = 65, 'Z' = 90, lowercase 'a' = 97, 'z' = 122, digit '0' = 48."
        }
    ]
    qs.extend(u1)

    # ----------------------------------------------------
    # UNIT 2: DIGITAL LOGIC & COMPUTER ORGANIZATION (15 QUESTIONS: Q16 to Q30)
    # ----------------------------------------------------
    u2 = [
        {
            "id": "P2-T2-U2-16", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Which logic gates are referred to as 'Universal Logic Gates' because any Boolean function can be implemented using them alone?",
            "options": [{"label": "A", "text": "NAND and NOR"}, {"label": "B", "text": "AND and OR"}, {"label": "C", "text": "XOR and XNOR"}, {"label": "D", "text": "NOT and AND"}],
            "answer": "A",
            "explanation": "NAND and NOR gates are universal gates capable of realizing NOT, AND, and OR operations independently."
        },
        {
            "id": "P2-T2-U2-17", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "According to De Morgan's Law, the Boolean expression (A + B)' is equivalent to:",
            "options": [{"label": "A", "text": "A' . B'"}, {"label": "B", "text": "A' + B'"}, {"label": "C", "text": "(A . B)'"}, {"label": "D", "text": "A + B'"}],
            "answer": "A",
            "explanation": "De Morgan's first theorem states: (A + B)' = A' . B'. De Morgan's second theorem states: (A . B)' = A' + B'."
        },
        {
            "id": "P2-T2-U2-18", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "A Full Adder combinational circuit can be constructed using:",
            "options": [{"label": "A", "text": "Two Half Adders and One OR gate"}, {"label": "B", "text": "Two Half Adders and One AND gate"}, {"label": "C", "text": "One Half Adder and Two OR gates"}, {"label": "D", "text": "Three Half Adders"}],
            "answer": "A",
            "explanation": "A Full Adder adds 3 bits (A, B, Cin). It consists of two Half Adders (generating intermediate sums and carries) and an OR gate combining the carry outputs."
        },
        {
            "id": "P2-T2-U2-19", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.2",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "In a JK Flip-Flop, what happens when both J and K inputs are set to logic HIGH (J=1, K=1) during a clock pulse?",
            "options": [{"label": "A", "text": "Toggle condition (Q(next) = Q')"}, {"label": "B", "text": "No change (Q(next) = Q)"}, {"label": "C", "text": "Reset to 0"}, {"label": "D", "text": "Undefined / Invalid state"}],
            "answer": "A",
            "explanation": "When J=1 and K=1, the JK flip-flop toggles its output state (solves the indeterminate state problem of the SR flip-flop)."
        },
        {
            "id": "P2-T2-U2-20", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "How many select input lines are required for a 16-to-1 Multiplexer (MUX)?",
            "options": [{"label": "A", "text": "4 select lines"}, {"label": "B", "text": "3 select lines"}, {"label": "C", "text": "8 select lines"}, {"label": "D", "text": "16 select lines"}],
            "answer": "A",
            "explanation": "A multiplexer with 2ⁿ data inputs requires n select lines. Since 16 = 2⁴, 4 select lines are required."
        },
        {
            "id": "P2-T2-U2-21", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which flip-flop eliminates the race-around condition by ensuring the next state always equals the data input D?",
            "options": [{"label": "A", "text": "D Flip-Flop (Data / Delay Flip-Flop)"}, {"label": "B", "text": "SR Flip-Flop"}, {"label": "C", "text": "T Flip-Flop"}, {"label": "D", "text": "Master-Slave SR"}],
            "answer": "A",
            "explanation": "A D flip-flop transfers its D input directly to output Q on the clock trigger (Q(next) = D), widely used in shift registers."
        },
        {
            "id": "P2-T2-U2-22", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.3",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "hard",
            "text": "In Morris Mano's basic computer architecture, what are the four phases of the instruction cycle in order?",
            "options": [{"label": "A", "text": "Fetch Instruction $\\to$ Decode Instruction $\\to$ Read Effective Address $\\to$ Execute Instruction"}, {"label": "B", "text": "Decode $\\to$ Fetch $\\to$ Execute $\\to$ Interrupt"}, {"label": "C", "text": "Execute $\\to$ Decode $\\to$ Fetch $\\to$ Store"}, {"label": "D", "text": "Read $\\to$ Write $\\to$ Decode $\\to$ Reset"}],
            "answer": "A",
            "explanation": "The instruction cycle phases are: 1. Fetch instruction from memory into IR; 2. Decode instruction; 3. Read effective address (if indirect); 4. Execute."
        },
        {
            "id": "P2-T2-U2-23", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which addressing mode specifies the operand directly within the instruction itself (e.g., ADDI R1, #5)?",
            "options": [{"label": "A", "text": "Immediate Addressing Mode"}, {"label": "B", "text": "Direct Addressing Mode"}, {"label": "C", "text": "Indirect Addressing Mode"}, {"label": "D", "text": "Register Indirect Mode"}],
            "answer": "A",
            "explanation": "In Immediate addressing mode, the operand is part of the instruction itself, requiring no memory access to fetch the data."
        },
        {
            "id": "P2-T2-U2-24", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Relative Addressing Mode, the effective address of the operand is calculated by adding the address field to the contents of:",
            "options": [{"label": "A", "text": "Program Counter (PC)"}, {"label": "B", "text": "Accumulator (AC)"}, {"label": "C", "text": "Index Register (XR)"}, {"label": "D", "text": "Stack Pointer (SP)"}],
            "answer": "A",
            "explanation": "Relative addressing computes Effective Address = PC + Address Offset, commonly used in branch and jump instructions."
        },
        {
            "id": "P2-T2-U2-25", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "A 5-stage non-pipelined processor executes an instruction in 50 ns. If a 5-stage pipelined version has a clock cycle of 11 ns (due to 1 ns latch delay), what is the speedup for executing 1000 instructions?",
            "options": [{"label": "A", "text": "~4.53"}, {"label": "B", "text": "~5.00"}, {"label": "C", "text": "~3.85"}, {"label": "D", "text": "~2.75"}],
            "answer": "A",
            "explanation": "Non-pipelined time = 1000 * 50 ns = 50,000 ns. Pipelined time = (k + n - 1) * cycle = (5 + 1000 - 1) * 11 ns = 1004 * 11 = 11,044 ns. Speedup = 50,000 / 11,044 ≈ 4.527."
        },
        {
            "id": "P2-T2-U2-26", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "The minimal Sum of Products (SOP) form of the Boolean expression F = A'B + AB is:",
            "options": [{"label": "A", "text": "B"}, {"label": "B", "text": "A"}, {"label": "C", "text": "A + B"}, {"label": "D", "text": "A'B'"}],
            "answer": "A",
            "explanation": "F = B(A' + A) = B(1) = B."
        },
        {
            "id": "P2-T2-U2-27", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "How many 3-to-8 line decoders with enable inputs are needed to construct a 4-to-16 line decoder?",
            "options": [{"label": "A", "text": "Two 3-to-8 decoders (and one inverter for enable)"}, {"label": "B", "text": "Four decoders"}, {"label": "C", "text": "Three decoders"}, {"label": "D", "text": "Eight decoders"}],
            "answer": "A",
            "explanation": "Using the 4th bit to drive the active-high/active-low enable lines directly (with one inverter), two 3-to-8 decoders form a 4-to-16 decoder."
        },
        {
            "id": "P2-T2-U2-28", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Direct Memory Access (DMA) data transfer bypasses which component to achieve high-speed bulk data movement between disk and RAM?",
            "options": [{"label": "A", "text": "CPU (Microprocessor core)"}, {"label": "B", "text": "System Bus"}, {"label": "C", "text": "Main Memory"}, {"label": "D", "text": "Disk Controller"}],
            "answer": "A",
            "explanation": "DMA controllers transfer data directly between I/O peripherals and main memory without burdening the CPU with per-byte interrupts."
        },
        {
            "id": "P2-T2-U2-29", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "An interrupt that cannot be masked or ignored by software instructions is called a:",
            "text_alt": "ಸಾಫ್ಟ್‌ವೇರ್ ಮೂಲಕ ನಿರ್ಲಕ್ಷಿಸಲು ಸಾಧ್ಯವಾಗದ ಅತ್ಯುನ್ನತ ಆದ್ಯತೆಯ ಇಂಟರಪ್ಟ್ ಯಾವುದು?",
            "options": [{"label": "A", "text": "Non-Maskable Interrupt (NMI)"}, {"label": "B", "text": "Vectored Maskable Interrupt"}, {"label": "C", "text": "Software Interrupt"}, {"label": "D", "text": "Polled Interrupt"}],
            "answer": "A",
            "explanation": "Non-Maskable Interrupts (like power failure, bus parity errors) have the highest priority and cannot be disabled by CLI instructions."
        },
        {
            "id": "P2-T2-U2-30", "paper": 2, "section_id": "U2", "subject": "Digital Logic & Organization", "syllabus_id": "P2-2.1",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "In a 4-variable Karnaugh Map (K-Map), grouping a block of 8 adjacent cells (an octet) eliminates how many variables?",
            "options": [{"label": "A", "text": "3 variables"}, {"label": "B", "text": "2 variables"}, {"label": "C", "text": "1 variable"}, {"label": "D", "text": "4 variables"}],
            "answer": "A",
            "explanation": "In a K-map, grouping 2ⁿ cells eliminates n variables. An octet has 2³ = 8 cells, so it eliminates 3 variables."
        }
    ]
    qs.extend(u2)

    # ----------------------------------------------------
    # UNIT 3: PROGRAMMING WITH C & C++ (15 QUESTIONS: Q31 to Q45)
    # ----------------------------------------------------
    u3 = [
        {
            "id": "P2-T2-U3-31", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "What will be the output of the C expression: 5 + 3 * 2 - 8 / 4?",
            "options": [{"label": "A", "text": "9"}, {"label": "B", "text": "14"}, {"label": "C", "text": "12"}, {"label": "D", "text": "7"}],
            "answer": "A",
            "explanation": "Operator precedence: * and / have higher precedence than + and -: 3*2 = 6, 8/4 = 2. Then left-to-right: 5 + 6 - 2 = 11 - 2 = 9."
        },
        {
            "id": "P2-T2-U3-32", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In C, what is the effect of declaring a variable with the 'static' storage class inside a function?",
            "options": [{"label": "A", "text": "The variable retains its value between function calls and has lifetime equal to program execution"}, {"label": "B", "text": "The variable becomes global and accessible across all files"}, {"label": "C", "text": "The variable is stored in CPU registers"}, {"label": "D", "text": "The variable cannot be modified (read-only)"}],
            "answer": "A",
            "explanation": "Static local variables are initialized once and reside in the data segment, retaining their values across successive function calls."
        },
        {
            "id": "P2-T2-U3-33", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "What does the declaration `int (*fp)(char, float);` signify in C?",
            "options": [{"label": "A", "text": "fp is a pointer to a function taking (char, float) arguments and returning int"}, {"label": "B", "text": "fp is a function returning a pointer to int"}, {"label": "C", "text": "fp is an array of function pointers"}, {"label": "D", "text": "Syntax error"}],
            "answer": "A",
            "explanation": "Parentheses around `*fp` bind the pointer to the identifier: `(*fp)` is a function pointer accepting `(char, float)` and returning `int`."
        },
        {
            "id": "P2-T2-U3-34", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the primary difference between `malloc()` and `calloc()` functions in standard C?",
            "options": [{"label": "A", "text": "calloc() initializes allocated memory bytes to zero; malloc() leaves memory uninitialized (garbage values)"}, {"label": "B", "text": "malloc() allocates from heap, calloc() allocates from stack"}, {"label": "C", "text": "malloc() takes two arguments, calloc() takes one"}, {"label": "D", "text": "calloc() cannot be freed using free()"}],
            "answer": "A",
            "explanation": "calloc(n, size) allocates contiguous memory and initializes all bits to zero; malloc(bytes) allocates uninitialized memory containing garbage."
        },
        {
            "id": "P2-T2-U3-35", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.3",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "In C++, dynamic polymorphism (late binding) is achieved using which mechanism?",
            "options": [{"label": "A", "text": "Virtual functions and base class pointers/references"}, {"label": "B", "text": "Function overloading"}, {"label": "C", "text": "Template functions"}, {"label": "D", "text": "Friend functions"}],
            "answer": "A",
            "explanation": "Runtime polymorphism in C++ is implemented via virtual functions, where the compiler sets up a vtable and vptr to resolve calls at runtime."
        },
        {
            "id": "P2-T2-U3-36", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "A class containing at least one pure virtual function (e.g., `virtual void draw() = 0;`) is known as:",
            "options": [{"label": "A", "text": "Abstract Class"}, {"label": "B", "text": "Concrete Class"}, {"label": "C", "text": "Sealed Class"}, {"label": "D", "text": "Singleton Class"}],
            "answer": "A",
            "explanation": "An abstract class contains one or more pure virtual functions (`= 0`) and cannot be directly instantiated."
        },
        {
            "id": "P2-T2-U3-37", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "Why should a base class destructor always be declared as `virtual` when deleting derived objects via base pointers?",
            "options": [{"label": "A", "text": "To prevent memory leaks by ensuring the derived class destructor is invoked first"}, {"label": "B", "text": "To make the base class abstract"}, {"label": "C", "text": "To prevent object slicing"}, {"label": "D", "text": "C++ requires all destructors to be virtual"}],
            "answer": "A",
            "explanation": "If a base destructor is non-virtual, deleting a derived object via a base pointer causes undefined behavior (derived destructor never executes, leaking resources)."
        },
        {
            "id": "P2-T2-U3-38", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which C++ feature solves the 'Diamond Problem' in multiple inheritance where a derived class inherits two copies of a common grandparent class?",
            "options": [{"label": "A", "text": "Virtual Base Classes (`virtual public Base`)"}, {"label": "B", "text": "Friend classes"}, {"label": "C", "text": "Namespace aliasing"}, {"label": "D", "text": "Inline functions"}],
            "answer": "A",
            "explanation": "Virtual base classes ensure that only one shared instance of the common ancestor sub-object is included in the most derived class."
        },
        {
            "id": "P2-T2-U3-39", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "What does a pointer variable contain in C?",
            "options": [{"label": "A", "text": "Memory address of another variable"}, {"label": "B", "text": "The data value directly"}, {"label": "C", "text": "A copy of CPU register contents"}, {"label": "D", "text": "Floating point constant"}],
            "answer": "A",
            "explanation": "A pointer is a variable that stores the hexadecimal/binary memory address of another variable."
        },
        {
            "id": "P2-T2-U3-40", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.2",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "What is the output of the following C code?\n```c\nint a[5] = {10, 20, 30, 40, 50};\nint *p = a;\nprintf(\"%d\", *(p + 3));\n```",
            "options": [{"label": "A", "text": "40"}, {"label": "B", "text": "30"}, {"label": "C", "text": "50"}, {"label": "D", "text": "Address of element"}],
            "answer": "A",
            "explanation": "`p` points to a[0] (10). Pointer arithmetic `p + 3` offsets 3 elements forward to &a[3]. Dereferencing `*(p + 3)` yields a[3] = 40."
        },
        {
            "id": "P2-T2-U3-41", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What happens when a dynamically allocated block of memory is lost without being released via `free()` or `delete`?",
            "options": [{"label": "A", "text": "Memory Leak"}, {"label": "B", "text": "Segmentation Fault"}, {"label": "C", "text": "Stack Overflow"}, {"label": "D", "text": "Dangling Pointer"}],
            "answer": "A",
            "explanation": "A memory leak occurs when heap memory is allocated but never deallocated and the pointer reference is lost."
        },
        {
            "id": "P2-T2-U3-42", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which constructor is invoked when a new object is initialized as a copy of an existing object of the same class (e.g., `Point p2 = p1;`)?",
            "options": [{"label": "A", "text": "Copy Constructor"}, {"label": "B", "text": "Default Constructor"}, {"label": "C", "text": "Parameterized Constructor"}, {"label": "D", "text": "Move Assignment Operator"}],
            "answer": "A",
            "explanation": "A copy constructor has the signature `ClassName(const ClassName &obj)` and initializes an object using an existing instance."
        },
        {
            "id": "P2-T2-U3-43", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In C++, which operator CANNOT be overloaded?",
            "options": [{"label": "A", "text": "Scope resolution operator (`::`)"}, {"label": "B", "text": "Addition operator (`+`)"}, {"label": "C", "text": "Array subscript operator (`[]`)"}, {"label": "D", "text": "Function call operator (`()`)"}],
            "answer": "A",
            "explanation": "Operators that cannot be overloaded in C++ include: scope resolution `::`, member selection `.`, pointer-to-member `.*`, and ternary `?:`."
        },
        {
            "id": "P2-T2-U3-44", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the size of a `union` in C?",
            "options": [{"label": "A", "text": "Equal to the size of its largest member"}, {"label": "B", "text": "Sum of sizes of all its members"}, {"label": "C", "text": "Size of its first member"}, {"label": "D", "text": "Always 4 bytes"}],
            "answer": "A",
            "explanation": "All members of a union share the same memory location; hence the union's size is determined by its largest data member."
        },
        {
            "id": "P2-T2-U3-45", "paper": 2, "section_id": "U3", "subject": "Programming with C & C++", "syllabus_id": "P2-3.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "In C++, when an exception is thrown inside a `try` block, what mechanism ensures that local stack objects are properly destructed in reverse order of construction?",
            "options": [{"label": "A", "text": "Stack Unwinding"}, {"label": "B", "text": "Garbage Collection"}, {"label": "C", "text": "Type Coercion"}, {"label": "D", "text": "Dynamic Casting"}],
            "answer": "A",
            "explanation": "Stack Unwinding is the runtime process that exits scopes and executes destructors of local automatic objects until an appropriate catch block is found."
        }
    ]
    qs.extend(u3)

    # ----------------------------------------------------
    # UNIT 4: DATA STRUCTURES & ALGORITHMS (15 QUESTIONS: Q46 to Q60)
    # ----------------------------------------------------
    u4 = [
        {
            "id": "P2-T2-U4-46", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Which data structure operates on the Last-In, First-Out (LIFO) operational principle?",
            "options": [{"label": "A", "text": "Stack"}, {"label": "B", "text": "Queue"}, {"label": "C", "text": "Linked List"}, {"label": "D", "text": "Binary Tree"}],
            "answer": "A",
            "explanation": "A Stack operates on LIFO (Last-In First-Out), where the last inserted element is the first removed (push/pop at top)."
        },
        {
            "id": "P2-T2-U4-47", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the postfix evaluation result of the expression: `6 3 2 + * 5 -`?",
            "options": [{"label": "A", "text": "25"}, {"label": "B", "text": "15"}, {"label": "C", "text": "20"}, {"label": "D", "text": "30"}],
            "answer": "A",
            "explanation": "Evaluation: 3 2 + = 5. Then 6 * 5 = 30. Then 30 - 5 = 25."
        },
        {
            "id": "P2-T2-U4-48", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In a Circular Queue of size N implemented using an array, what condition indicates that the queue is completely full?",
            "options": [{"label": "A", "text": "(rear + 1) % N == front"}, {"label": "B", "text": "rear == front"}, {"label": "C", "text": "front == 0"}, {"label": "D", "text": "rear == N - 1"}],
            "answer": "A",
            "explanation": "In a circular queue, full condition is `(rear + 1) % N == front`; empty condition is `front == rear` (or front == -1)."
        },
        {
            "id": "P2-T2-U4-49", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.2",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "What is the worst-case time complexity of QuickSort algorithm?",
            "options": [{"label": "A", "text": "O(n²)"}, {"label": "B", "text": "O(n log n)"}, {"label": "C", "text": "O(n)"}, {"label": "D", "text": "O(log n)"}],
            "answer": "A",
            "explanation": "QuickSort has average complexity O(n log n), but degrades to worst-case O(n²) when the partition is unbalanced (e.g. array already sorted)."
        },
        {
            "id": "P2-T2-U4-50", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which sorting algorithm guarantees O(n log n) time complexity in the worst case, best case, and average case, while requiring O(n) auxiliary space?",
            "options": [{"label": "A", "text": "Merge Sort"}, {"label": "B", "text": "Quick Sort"}, {"label": "C", "text": "Bubble Sort"}, {"label": "D", "text": "Insertion Sort"}],
            "answer": "A",
            "explanation": "Merge Sort consistently divides the array in half and merges, guaranteeing O(n log n) in all cases with O(n) auxiliary space."
        },
        {
            "id": "P2-T2-U4-51", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In-order traversal of a valid Binary Search Tree (BST) produces keys in:",
            "options": [{"label": "A", "text": "Strictly ascending (sorted) order"}, {"label": "B", "text": "Strictly descending order"}, {"label": "C", "text": "Random order"}, {"label": "D", "text": "Breadth-first order"}],
            "answer": "A",
            "explanation": "In-order traversal visits (Left, Root, Right). In a BST, Left < Root < Right, so in-order produces sorted ascending keys."
        },
        {
            "id": "P2-T2-U4-52", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "What is the defining balance factor property of an AVL tree for every node?",
            "options": [{"label": "A", "text": "Balance Factor ∈ {-1, 0, +1}"}, {"label": "B", "text": "Balance Factor == 0"}, {"label": "C", "text": "Balance Factor ≤ 2"}, {"label": "D", "text": "Balance Factor ≥ 0"}],
            "answer": "A",
            "explanation": "An AVL tree is a self-balancing BST where the balance factor (Height(Left) - Height(Right)) of every node must be -1, 0, or +1."
        },
        {
            "id": "P2-T2-U4-53", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.4",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Dijkstra's Single-Source Shortest Path algorithm fails to produce correct results in graphs containing:",
            "options": [{"label": "A", "text": "Negative weight edges"}, {"label": "B", "text": "Cycles"}, {"label": "C", "text": "Disconnected components"}, {"label": "D", "text": "Zero weight edges"}],
            "answer": "A",
            "explanation": "Dijkstra's greedy choice assumes adding an edge never decreases path cost, so it fails on negative weight edges (Bellman-Ford is used instead)."
        },
        {
            "id": "P2-T2-U4-54", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which algorithmic design paradigm is used by Kruskal's algorithm to construct a Minimum Spanning Tree (MST)?",
            "options": [{"label": "A", "text": "Greedy Method"}, {"label": "B", "text": "Dynamic Programming"}, {"label": "C", "text": "Divide and Conquer"}, {"label": "D", "text": "Backtracking"}],
            "answer": "A",
            "explanation": "Kruskal's algorithm sorts edges by weight and greedily selects the minimum-weight edge that does not form a cycle (using Disjoint Set Union)."
        },
        {
            "id": "P2-T2-U4-55", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "What is the time complexity to insert a new node at the beginning (head) of a Singly Linked List?",
            "options": [{"label": "A", "text": "O(1)"}, {"label": "B", "text": "O(n)"}, {"label": "C", "text": "O(log n)"}, {"label": "D", "text": "O(n²)"}],
            "answer": "A",
            "explanation": "Inserting at head requires allocating a node, setting `newNode->next = head`, and `head = newNode`, executing in O(1) constant time."
        },
        {
            "id": "P2-T2-U4-56", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Breadth-First Search (BFS) graph traversal standardly uses which data structure?",
            "options": [{"label": "A", "text": "Queue"}, {"label": "B", "text": "Stack"}, {"label": "C", "text": "Priority Queue"}, {"label": "D", "text": "Binary Tree"}],
            "answer": "A",
            "explanation": "BFS explores level by level using a FIFO Queue; Depth-First Search (DFS) uses a LIFO Stack (or recursion)."
        },
        {
            "id": "P2-T2-U4-57", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the maximum number of nodes in a binary tree of depth (height) h, where root is at level 0?",
            "options": [{"label": "A", "text": "2^(h+1) - 1"}, {"label": "B", "text": "2^h"}, {"label": "C", "text": "2^(h-1)"}, {"label": "D", "text": "2h + 1"}],
            "answer": "A",
            "explanation": "Max nodes = 2⁰ + 2¹ + ... + 2ʰ = 2^(h+1) - 1. For height h=3, max nodes = 2⁴ - 1 = 15."
        },
        {
            "id": "P2-T2-U4-58", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.1",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Floyd's Cycle-Finding algorithm (tortoise and hare) detects a loop in a linked list in:",
            "options": [{"label": "A", "text": "O(n) time and O(1) auxiliary space"}, {"label": "B", "text": "O(n²) time and O(n) space"}, {"label": "C", "text": "O(n log n) time and O(1) space"}, {"label": "D", "text": "O(1) time and O(n) space"}],
            "answer": "A",
            "explanation": "Floyd's algorithm advances slow pointer by 1 step and fast pointer by 2 steps; if they meet, a cycle exists, achieving O(n) time and O(1) space."
        },
        {
            "id": "P2-T2-U4-59", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In a Max-Heap data structure with n elements, what is the time complexity to extract the maximum element?",
            "options": [{"label": "A", "text": "O(log n)"}, {"label": "B", "text": "O(1)"}, {"label": "C", "text": "O(n)"}, {"label": "D", "text": "O(n log n)"}],
            "answer": "A",
            "explanation": "Extract-Max removes root, places last element at root, and runs Max-Heapify to restore heap property in O(log n) time."
        },
        {
            "id": "P2-T2-U4-60", "paper": 2, "section_id": "U4", "subject": "Data Structures & Algorithms", "syllabus_id": "P2-4.4",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "The 0/1 Knapsack problem is standardly solved using Dynamic Programming in pseudo-polynomial time of:",
            "options": [{"label": "A", "text": "O(n * W), where n is items and W is capacity"}, {"label": "B", "text": "O(n log n)"}, {"label": "C", "text": "O(2^n)"}, {"label": "D", "text": "O(n + W)"}],
            "answer": "A",
            "explanation": "The 2D dynamic programming table `K[i][w]` requires `n` rows and `W` columns, yielding O(n * W) time complexity."
        }
    ]
    qs.extend(u4)

    # ----------------------------------------------------
    # UNIT 5: DATABASE MANAGEMENT SYSTEMS (15 QUESTIONS: Q61 to Q75)
    # ----------------------------------------------------
    u5 = [
        {
            "id": "P2-T2-U5-61", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "In relational database theory, what is a single row in a database table called?",
            "options": [{"label": "A", "text": "Tuple"}, {"label": "B", "text": "Attribute"}, {"label": "C", "text": "Domain"}, {"label": "D", "text": "Schema"}],
            "answer": "A",
            "explanation": "In relational model terminology: Table = Relation, Row = Tuple, Column = Attribute, Number of rows = Cardinality, Number of columns = Degree."
        },
        {
            "id": "P2-T2-U5-62", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What does Entity Integrity constraint state in the relational model?",
            "options": [{"label": "A", "text": "No primary key attribute can contain a NULL value"}, {"label": "B", "text": "Foreign keys must match valid primary keys"}, {"label": "C", "text": "Attribute values must be atomic"}, {"label": "D", "text": "Tables must be sorted"}],
            "answer": "A",
            "explanation": "Entity Integrity dictates that no component of a Primary Key can be NULL, ensuring every tuple can be uniquely identified."
        },
        {
            "id": "P2-T2-U5-63", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.2",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "A relation is in Second Normal Form (2NF) if and only if it is in 1NF and:",
            "options": [{"label": "A", "text": "Every non-prime attribute is fully functionally dependent on the entire primary key (no partial dependency)"}, {"label": "B", "text": "There are no transitive dependencies"}, {"label": "C", "text": "All multivalued dependencies are eliminated"}, {"label": "D", "text": "Every determinant is a candidate key"}],
            "answer": "A",
            "explanation": "2NF requires 1NF + elimination of partial functional dependencies (non-prime attributes cannot depend on a proper subset of a composite candidate key)."
        },
        {
            "id": "P2-T2-U5-64", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "A relation is in Third Normal Form (3NF) if for every non-trivial functional dependency X -> Y:",
            "options": [{"label": "A", "text": "Either X is a super key or Y is a prime attribute"}, {"label": "B", "text": "X must always be a candidate key"}, {"label": "C", "text": "Y must be a super key"}, {"label": "D", "text": "No attribute can be numeric"}],
            "answer": "A",
            "explanation": "3NF eliminates transitive dependencies: for X -> Y, either X is a superkey or Y is a prime attribute (part of a candidate key)."
        },
        {
            "id": "P2-T2-U5-65", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "What makes Boyce-Codd Normal Form (BCNF) strictly stronger than Third Normal Form (3NF)?",
            "options": [{"label": "A", "text": "In BCNF, for every functional dependency X -> Y, X must be a super key (eliminating prime attribute exception)"}, {"label": "B", "text": "BCNF permits partial dependencies"}, {"label": "C", "text": "BCNF requires lossy decomposition"}, {"label": "D", "text": "BCNF applies only to non-relational databases"}],
            "answer": "A",
            "explanation": "BCNF removes the exception present in 3NF: in BCNF, every determinant X in non-trivial X -> Y must strictly be a superkey."
        },
        {
            "id": "P2-T2-U5-66", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In SQL, which clause is used to filter aggregated group results produced by the `GROUP BY` clause?",
            "options": [{"label": "A", "text": "HAVING"}, {"label": "B", "text": "WHERE"}, {"label": "C", "text": "ORDER BY"}, {"label": "D", "text": "LIKE"}],
            "answer": "A",
            "explanation": "`WHERE` filters individual rows prior to grouping; `HAVING` filters aggregated groups after `GROUP BY`."
        },
        {
            "id": "P2-T2-U5-67", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which SQL JOIN returns all rows from the left table along with matching rows from the right table, and NULLs where no match exists?",
            "options": [{"label": "A", "text": "LEFT OUTER JOIN"}, {"label": "B", "text": "INNER JOIN"}, {"label": "C", "text": "RIGHT OUTER JOIN"}, {"label": "D", "text": "CROSS JOIN"}],
            "answer": "A",
            "explanation": "LEFT OUTER JOIN preserves all tuples from the left relation, padding right attributes with NULL when the join condition fails."
        },
        {
            "id": "P2-T2-U5-68", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.4",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "The ACID properties of database transactions ensure reliable processing. What does the 'I' in ACID stand for?",
            "options": [{"label": "A", "text": "Isolation"}, {"label": "B", "text": "Integrity"}, {"label": "C", "text": "Indexing"}, {"label": "D", "text": "Iteration"}],
            "answer": "A",
            "explanation": "ACID: Atomicity (all-or-nothing), Consistency (preserves constraints), Isolation (concurrent transactions execute independently), Durability (persists after commit)."
        },
        {
            "id": "P2-T2-U5-69", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "In Two-Phase Locking (2PL) protocol, what rule guarantees serializability?",
            "options": [{"label": "A", "text": "Once a transaction releases a lock, it can never acquire any new locks (Shrinking phase)"}, {"label": "B", "text": "Transactions must acquire all locks before starting"}, {"label": "C", "text": "Only shared locks are permitted"}, {"label": "D", "text": "Locks are never released"}],
            "answer": "A",
            "explanation": "2PL consists of a Growing Phase (only lock acquisitions) and a Shrinking Phase (only lock releases). No lock can be acquired after any lock is released."
        },
        {
            "id": "P2-T2-U5-70", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What type of schedule allows transactions to read only values written by committed transactions, preventing cascading rollbacks?",
            "options": [{"label": "A", "text": "Cascadeless Schedule"}, {"label": "B", "text": "Strict Schedule"}, {"label": "C", "text": "Recoverable Schedule"}, {"label": "D", "text": "View Serial Schedule"}],
            "answer": "A",
            "explanation": "In a Cascadeless schedule, each transaction reads only data committed by the writing transaction, avoiding cascading aborts."
        },
        {
            "id": "P2-T2-U5-71", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which SQL command is a Data Definition Language (DDL) command?",
            "options": [{"label": "A", "text": "CREATE"}, {"label": "B", "text": "INSERT"}, {"label": "C", "text": "UPDATE"}, {"label": "D", "text": "SELECT"}],
            "answer": "A",
            "explanation": "DDL commands define schema structures: CREATE, ALTER, DROP, TRUNCATE. DML commands manipulate data: INSERT, UPDATE, DELETE, SELECT."
        },
        {
            "id": "P2-T2-U5-72", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In an Entity-Relationship (ER) diagram, a Weak Entity Set is visually depicted by:",
            "options": [{"label": "A", "text": "Double Rectangle"}, {"label": "B", "text": "Double Diamond"}, {"label": "C", "text": "Dashed Ellipse"}, {"label": "D", "text": "Single Rectangle"}],
            "answer": "A",
            "explanation": "Weak entity sets (which lack a primary key of their own) are represented by Double Rectangles, and identifying relationships by Double Diamonds."
        },
        {
            "id": "P2-T2-U5-73", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.4",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "In B+ Tree file indexing, how do leaf nodes differ from internal index nodes?",
            "options": [{"label": "A", "text": "Leaf nodes store all actual record pointers and are linked sequentially as a doubly linked list"}, {"label": "B", "text": "Internal nodes store all data records"}, {"label": "C", "text": "Leaf nodes have no pointers"}, {"label": "D", "text": "Leaf nodes cannot be searched in O(log n)"}],
            "answer": "A",
            "explanation": "In a B+ Tree, leaf nodes contain all keys and record pointers and are linked sequentially, providing efficient range queries and sequential scans."
        },
        {
            "id": "P2-T2-U5-74", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the difference between `DELETE` and `TRUNCATE` statements in SQL?",
            "options": [{"label": "A", "text": "DELETE is a logged DML operation that can be rolled back; TRUNCATE is a DDL operation deallocating data pages"}, {"label": "B", "text": "TRUNCATE removes the table definition entirely"}, {"label": "C", "text": "DELETE cannot have a WHERE clause"}, {"label": "D", "text": "TRUNCATE fires row-level triggers"}],
            "answer": "A",
            "explanation": "DELETE logs row deletions and supports WHERE and ROLLBACK; TRUNCATE deallocates extents rapidly without per-row logging and resets identity."
        },
        {
            "id": "P2-T2-U5-75", "paper": 2, "section_id": "U5", "subject": "Database Management Systems", "syllabus_id": "P2-5.4",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "The Wait-Die deadlock prevention scheme for transactions is based on timestamp ordering. If older transaction T_old requests a lock held by younger transaction T_young:",
            "options": [{"label": "A", "text": "T_old is allowed to wait for T_young"}, {"label": "B", "text": "T_old dies"}, {"label": "C", "text": "T_young is aborted (wound)"}, {"label": "D", "text": "Both transactions abort"}],
            "answer": "A",
            "explanation": "In Wait-Die: If older requests lock held by younger, older is allowed to wait. If younger requests lock held by older, younger dies (aborts)."
        }
    ]
    qs.extend(u5)

    # ----------------------------------------------------
    # UNIT 6: OPERATING SYSTEMS & SYSTEM PROGRAMMING (15 QUESTIONS: Q76 to Q90)
    # ----------------------------------------------------
    u6 = [
        {
            "id": "P2-T2-U6-76", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "The data structure maintained by the Operating System to store all control attributes of an active process (state, PC, registers, memory limits) is:",
            "options": [{"label": "A", "text": "Process Control Block (PCB)"}, {"label": "B", "text": "File Allocation Table (FAT)"}, {"label": "C", "text": "Page Map Table"}, {"label": "D", "text": "Segment Table"}],
            "answer": "A",
            "explanation": "The PCB (Process Control Block / Task Descriptor) stores PID, state, CPU registers, program counter, CPU scheduling, and I/O status."
        },
        {
            "id": "P2-T2-U6-77", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which CPU scheduling algorithm gives the minimum theoretical average waiting time for a given set of stationary processes?",
            "options": [{"label": "A", "text": "Shortest Job First (SJF / SRTF)"}, {"label": "B", "text": "First-Come, First-Served (FCFS)"}, {"label": "C", "text": "Round Robin (RR)"}, {"label": "D", "text": "Priority Scheduling"}],
            "answer": "A",
            "explanation": "SJF is provably optimal because scheduling shorter jobs ahead reduces the cumulative waiting time for all subsequent processes."
        },
        {
            "id": "P2-T2-U6-78", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.2",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Which four Coffman conditions are simultaneously necessary and sufficient for a Deadlock to occur?",
            "options": [{"label": "A", "text": "Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait"}, {"label": "B", "text": "Paging, Segmentation, Swapping, Thrashing"}, {"label": "C", "text": "Starvation, Deadlock, Aging, Inversion"}, {"label": "D", "text": "Race Condition, Critical Section, Mutex, Semaphore"}],
            "answer": "A",
            "explanation": "Coffman conditions for deadlock: 1. Mutual Exclusion; 2. Hold and Wait; 3. No Preemption; 4. Circular Wait."
        },
        {
            "id": "P2-T2-U6-79", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "Banker's Algorithm for deadlock avoidance tests whether granting a resource request leaves the system in a:",
            "options": [{"label": "A", "text": "Safe State"}, {"label": "B", "text": "Preempted State"}, {"label": "C", "text": "Starvation State"}, {"label": "D", "text": "Deterministic State"}],
            "answer": "A",
            "explanation": "Banker's Algorithm simulates resource allocation to find a safe execution sequence where every process can satisfy maximum demand without deadlock."
        },
        {
            "id": "P2-T2-U6-80", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What happens when a process invokes the `wait()` (or `P()`) operation on a semaphore with value 0?",
            "options": [{"label": "A", "text": "The process is blocked (placed in the semaphore waiting queue)"}, {"label": "B", "text": "The semaphore value decrements to -1 and process continues"}, {"label": "C", "text": "The process terminates"}, {"label": "D", "text": "The OS crashes"}],
            "answer": "A",
            "explanation": "If semaphore value `S <= 0`, executing `wait(S)` blocks the calling process until another process calls `signal(S)`."
        },
        {
            "id": "P2-T2-U6-81", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.3",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "What is the phenomenon where the system spends more time servicing page faults and swapping pages than executing instructions?",
            "options": [{"label": "A", "text": "Thrashing"}, {"label": "B", "text": "Belady's Anomaly"}, {"label": "C", "text": "Segmentation Fault"}, {"label": "D", "text": "Aging"}],
            "answer": "A",
            "explanation": "Thrashing occurs when the sum of working sets exceeds available physical memory frames, causing continuous disk paging and CPU collapse."
        },
        {
            "id": "P2-T2-U6-82", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "Belady's Anomaly (where increasing the number of physical page frames results in an increased number of page faults) can occur in which algorithm?",
            "options": [{"label": "A", "text": "FIFO (First-In, First-Out)"}, {"label": "B", "text": "LRU (Least Recently Used)"}, {"label": "C", "text": "Optimal Page Replacement"}, {"label": "D", "text": "LFU"}],
            "answer": "A",
            "explanation": "FIFO does not satisfy the inclusion property (stack algorithms like LRU and Optimal are immune), hence it can exhibit Belady's Anomaly."
        },
        {
            "id": "P2-T2-U6-83", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In virtual memory paging, the hardware cache used by the Memory Management Unit (MMU) to accelerate virtual-to-physical address translation is:",
            "options": [{"label": "A", "text": "TLB (Translation Lookaside Buffer)"}, {"label": "B", "text": "Instruction Register"}, {"label": "C", "text": "Page Map Table"}, {"label": "D", "text": "Segment Descriptor"}],
            "answer": "A",
            "explanation": "The TLB is high-speed associative hardware cache storing recent page-table mappings to avoid multi-level memory lookups."
        },
        {
            "id": "P2-T2-U6-84", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "A process that has finished execution but whose parent has not yet read its exit status via `wait()` system call is a:",
            "options": [{"label": "A", "text": "Zombie Process"}, {"label": "B", "text": "Orphan Process"}, {"label": "C", "text": "Daemon Process"}, {"label": "D", "text": "Foreground Process"}],
            "answer": "A",
            "explanation": "A terminated process remains a 'Zombie' in the process table holding its PID and exit code until reaped by its parent."
        },
        {
            "id": "P2-T2-U6-85", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "In Unix/Linux, which system call creates an exact duplicate child process of the calling parent process?",
            "options": [{"label": "A", "text": "fork()"}, {"label": "B", "text": "exec()"}, {"label": "C", "text": "spawn()"}, {"label": "D", "text": "clone()"}],
            "answer": "A",
            "explanation": "fork() duplicates the calling process, returning 0 to child and child's PID to parent. exec() replaces address space with a new program."
        },
        {
            "id": "P2-T2-U6-86", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In language processor tools, which tool translates assembly language mnemonics into machine code object files?",
            "options": [{"label": "A", "text": "Assembler"}, {"label": "B", "text": "Linker"}, {"label": "C", "text": "Loader"}, {"label": "D", "text": "Pre-processor"}],
            "answer": "A",
            "explanation": "Assembler translates assembly code to object code; Linker combines object files and libraries; Loader loads executable into RAM."
        },
        {
            "id": "P2-T2-U6-87", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In compiler construction, lexical analysis (Phase 1) converts high-level source text into a stream of:",
            "options": [{"label": "A", "text": "Tokens"}, {"label": "B", "text": "Parse Trees"}, {"label": "C", "text": "Three-Address Codes"}, {"label": "D", "text": "Assembly Op-codes"}],
            "answer": "A",
            "explanation": "Lexical Analysis (Scanning) groups character streams into meaningful atomic language units called Tokens."
        },
        {
            "id": "P2-T2-U6-88", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Given page size = 4 KB, how many bits in a 32-bit virtual address represent the page offset, and how many represent the virtual page number?",
            "options": [{"label": "A", "text": "12 bits offset, 20 bits virtual page number"}, {"label": "B", "text": "10 bits offset, 22 bits virtual page number"}, {"label": "C", "text": "16 bits offset, 16 bits virtual page number"}, {"label": "D", "text": "14 bits offset, 18 bits virtual page number"}],
            "answer": "A",
            "explanation": "Page size 4 KB = 2¹² bytes => 12 bits for Page Offset. Virtual address = 32 bits => Page Number = 32 - 12 = 20 bits."
        },
        {
            "id": "P2-T2-U6-89", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Priority Inversion occurs when a high-priority task is indirectly blocked by a low-priority task holding a shared lock. It is resolved by:",
            "options": [{"label": "A", "text": "Priority Inheritance Protocol"}, {"label": "B", "text": "FCFS scheduling"}, {"label": "C", "text": "Killing the low-priority task"}, {"label": "D", "text": "Disabling interrupts"}],
            "answer": "A",
            "explanation": "Under Priority Inheritance, the low-priority task temporarily inherits the priority of the highest-priority task waiting on its lock."
        },
        {
            "id": "P2-T2-U6-90", "paper": 2, "section_id": "U6", "subject": "Operating Systems", "syllabus_id": "P2-6.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Round Robin CPU scheduling, if the Time Quantum (q) is chosen to be extremely large (larger than the longest burst time), the algorithm degenerates into:",
            "options": [{"label": "A", "text": "First-Come, First-Served (FCFS)"}, {"label": "B", "text": "Shortest Remaining Time First"}, {"label": "C", "text": "Priority Scheduling"}, {"label": "D", "text": "Multilevel Feedback Queue"}],
            "answer": "A",
            "explanation": "When time quantum q -> ∞, each process runs to completion on its first dispatch, exactly matching FCFS scheduling."
        }
    ]
    qs.extend(u6)

    # ----------------------------------------------------
    # UNIT 7: COMPUTER NETWORKS & DATA COMMUNICATION (15 QUESTIONS: Q91 to Q105)
    # ----------------------------------------------------
    u7 = [
        {
            "id": "P2-T2-U7-91", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Which layer of the OSI 7-layer reference model is responsible for end-to-end process-to-process communication, error recovery, and flow control?",
            "options": [{"label": "A", "text": "Transport Layer"}, {"label": "B", "text": "Network Layer"}, {"label": "C", "text": "Data Link Layer"}, {"label": "D", "text": "Session Layer"}],
            "answer": "A",
            "explanation": "The Transport Layer (Layer 4) ensures end-to-end process-to-process delivery (ports, segmentation, flow control, reliability)."
        },
        {
            "id": "P2-T2-U7-92", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Routers operate primarily at which layer of the OSI model?",
            "options": [{"label": "A", "text": "Network Layer (Layer 3)"}, {"label": "B", "text": "Data Link Layer (Layer 2)"}, {"label": "C", "text": "Transport Layer (Layer 4)"}, {"label": "D", "text": "Physical Layer (Layer 1)"}],
            "answer": "A",
            "explanation": "Routers operate at Network Layer (Layer 3) inspecting IP packet headers; Switches operate at Layer 2 (MAC); Hubs at Layer 1."
        },
        {
            "id": "P2-T2-U7-93", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.2",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Cyclic Redundancy Check (CRC) is an error detection code standardly implemented in which network layer?",
            "options": [{"label": "A", "text": "Data Link Layer"}, {"label": "B", "text": "Application Layer"}, {"label": "C", "text": "Transport Layer"}, {"label": "D", "text": "Session Layer"}],
            "answer": "A",
            "explanation": "CRC operates at the Data Link Layer (Layer 2), appending a frame check sequence (FCS) using binary polynomial division."
        },
        {
            "id": "P2-T2-U7-94", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "In CSMA/CD (Carrier Sense Multiple Access with Collision Detection) used in traditional Ethernet, what protocol resolves packet collisions?",
            "options": [{"label": "A", "text": "Binary Exponential Backoff Algorithm"}, {"label": "B", "text": "Token Ring Passing"}, {"label": "C", "text": "Sliding Window Protocol"}, {"label": "D", "text": "Bellman-Ford Relaxation"}],
            "answer": "A",
            "explanation": "When a collision is detected, stations jam the channel and wait for a random slot `r ∈ [0, 2^k - 1]` using Exponential Backoff."
        },
        {
            "id": "P2-T2-U7-95", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the broadcast address for the IPv4 subnet 192.168.10.0/24?",
            "options": [{"label": "A", "text": "192.168.10.255"}, {"label": "B", "text": "192.168.10.0"}, {"label": "C", "text": "192.168.10.1"}, {"label": "D", "text": "255.255.255.255"}],
            "answer": "A",
            "explanation": "In a /24 subnet (mask 255.255.255.0), the host bits are all 1s (255), giving the directed broadcast address 192.168.10.255."
        },
        {
            "id": "P2-T2-U7-96", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "An organization is assigned IP network 200.100.50.0/24. If they require 4 equal subnets, what is the new subnet mask and maximum usable hosts per subnet?",
            "options": [{"label": "A", "text": "Mask: 255.255.255.192 (/26), 62 usable hosts"}, {"label": "B", "text": "Mask: 255.255.255.224 (/27), 30 usable hosts"}, {"label": "C", "text": "Mask: 255.255.255.128 (/25), 126 usable hosts"}, {"label": "D", "text": "Mask: 255.255.255.240 (/28), 14 usable hosts"}],
            "answer": "A",
            "explanation": "4 subnets require borrowing 2 bits: /24 + 2 = /26 (mask 255.255.255.192). Host bits = 32 - 26 = 6 => Usable hosts = 2⁶ - 2 = 62 hosts."
        },
        {
            "id": "P2-T2-U7-97", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.4",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "In TCP connection establishment, what is the correct 3-way handshake sequence exchanged between Client and Server?",
            "options": [{"label": "A", "text": "SYN -> SYN+ACK -> ACK"}, {"label": "B", "text": "ACK -> SYN -> SYN+ACK"}, {"label": "C", "text": "SYN -> ACK -> DATA"}, {"label": "D", "text": "FIN -> FIN+ACK -> ACK"}],
            "answer": "A",
            "explanation": "TCP 3-way handshake: Client sends SYN -> Server responds with SYN-ACK -> Client sends ACK. Connection is now ESTABLISHED."
        },
        {
            "id": "P2-T2-U7-98", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which transport layer protocol is connectionless, unreliable (best-effort), and suitable for real-time video streaming and VoIP?",
            "options": [{"label": "A", "text": "UDP (User Datagram Protocol)"}, {"label": "B", "text": "TCP"}, {"label": "C", "text": "SCTP"}, {"label": "D", "text": "ICMP"}],
            "answer": "A",
            "explanation": "UDP has minimal 8-byte header overhead with no retransmissions or handshake, making it ideal for low-latency streaming and DNS."
        },
        {
            "id": "P2-T2-U7-99", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What protocol resolves an IP address into its corresponding physical hardware MAC address on a local area network?",
            "options": [{"label": "A", "text": "ARP (Address Resolution Protocol)"}, {"label": "B", "text": "RARP"}, {"label": "C", "text": "DHCP"}, {"label": "D", "text": "DNS"}],
            "answer": "A",
            "explanation": "ARP broadcasts an IP address to learn the target host's 48-bit MAC address; RARP resolves MAC to IP."
        },
        {
            "id": "P2-T2-U7-100", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The Count-to-Infinity problem is a known routing instability vulnerability associated with which routing algorithm?",
            "options": [{"label": "A", "text": "Distance Vector Routing (Bellman-Ford)"}, {"label": "B", "text": "Link State Routing (OSPF)"}, {"label": "C", "text": "Path Vector Routing (BGP)"}, {"label": "D", "text": "Flooding"}],
            "answer": "A",
            "explanation": "Distance Vector algorithms suffer from slow convergence upon link failure (Count-to-Infinity), mitigated by split horizon and poison reverse."
        },
        {
            "id": "P2-T2-U7-101", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which application layer protocol standardly uses well-known TCP Port 25 for sending emails across mail transfer agents?",
            "options": [{"label": "A", "text": "SMTP (Simple Mail Transfer Protocol)"}, {"label": "B", "text": "POP3"}, {"label": "C", "text": "IMAP"}, {"label": "D", "text": "SNMP"}],
            "answer": "A",
            "explanation": "SMTP uses Port 25 (or 587) for sending email; POP3 uses Port 110; IMAP uses Port 143."
        },
        {
            "id": "P2-T2-U7-102", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.2",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "In a Sliding Window protocol, if the sender window size is W, what is the maximum link utilization in Stop-and-Wait protocol where W = 1?",
            "options": [{"label": "A", "text": "1 / (1 + 2a), where a = Propagation Time / Transmission Time"}, {"label": "B", "text": "1 / (1 + a)"}, {"label": "C", "text": "W / (1 + 2a)"}, {"label": "D", "text": "100%"}],
            "answer": "A",
            "explanation": "Utilization $\\eta$ = Transmission Time / (Transmission Time + 2 * Propagation Time) = 1 / (1 + 2a), where a = $T_p / T_t$."
        },
        {
            "id": "P2-T2-U7-103", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "What is the loopback IPv4 address reserved for testing internal network protocol stacks on a local host?",
            "options": [{"label": "A", "text": "127.0.0.1"}, {"label": "B", "text": "192.168.0.1"}, {"label": "C", "text": "10.0.0.1"}, {"label": "D", "text": "0.0.0.0"}],
            "answer": "A",
            "explanation": "The entire 127.0.0.0/8 block is reserved for loopback; 127.0.0.1 standardly points to localhost."
        },
        {
            "id": "P2-T2-U7-104", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which ICMP message type is returned by intermediate routers when an IP packet's Time-to-Live (TTL) field reaches zero?",
            "options": [{"label": "A", "text": "Time Exceeded (ICMP Type 11)"}, {"label": "B", "text": "Destination Unreachable"}, {"label": "C", "text": "Echo Reply"}, {"label": "D", "text": "Redirect"}],
            "answer": "A",
            "explanation": "When TTL decrements to 0, the router drops the packet and responds with an ICMP Time Exceeded message (basis for `traceroute`)."
        },
        {
            "id": "P2-T2-U7-105", "paper": 2, "section_id": "U7", "subject": "Computer Networks", "syllabus_id": "P2-7.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which transmission medium utilizes total internal reflection of light pulses through silica glass strands for ultra-high-speed data transmission?",
            "options": [{"label": "A", "text": "Fiber Optic Cable"}, {"label": "B", "text": "Coaxial Cable"}, {"label": "C", "text": "Shielded Twisted Pair (STP)"}, {"label": "D", "text": "Infrared"}],
            "answer": "A",
            "explanation": "Fiber optic cables transmit light modulated signals via total internal reflection across a silica glass core, offering immune EMI and gigabit speeds."
        }
    ]
    qs.extend(u7)

    # ----------------------------------------------------
    # UNIT 8: SOFTWARE ENGINEERING & OOAD (15 QUESTIONS: Q106 to Q120)
    # ----------------------------------------------------
    u8 = [
        {
            "id": "P2-T2-U8-106", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Which classic Software Development Life Cycle (SDLC) model follows a strictly sequential phase-by-phase progression where each phase must finish before the next begins?",
            "options": [{"label": "A", "text": "Waterfall Model"}, {"label": "B", "text": "Agile Scrum"}, {"label": "C", "text": "Spiral Model"}, {"label": "D", "text": "RAD Model"}],
            "answer": "A",
            "explanation": "The Waterfall model (Winston Royce) is a linear-sequential lifecycle with distinct phases: Requirements -> Design -> Implementation -> Testing -> Maintenance."
        },
        {
            "id": "P2-T2-U8-107", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Barry Boehm's Spiral Model is particularly suited for large, high-risk projects because every iteration explicitly incorporates:",
            "options": [{"label": "A", "text": "Risk Analysis and Mitigation"}, {"label": "B", "text": "Strictly no prototyping"}, {"label": "C", "text": "Elimination of documentation"}, {"label": "D", "text": "Automated code generation"}],
            "answer": "A",
            "explanation": "The Spiral Model is risk-driven, combining prototyping with iterative development; each spiral quadrant conducts explicit risk assessment."
        },
        {
            "id": "P2-T2-U8-108", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "In White-Box testing, McCabe's Cyclomatic Complexity V(G) for a control flow graph with E edges, N nodes, and P connected components is calculated as:",
            "options": [{"label": "A", "text": "V(G) = E - N + 2P"}, {"label": "B", "text": "V(G) = E + N - P"}, {"label": "C", "text": "V(G) = E - N - 2P"}, {"label": "D", "text": "V(G) = N - E + P"}],
            "answer": "A",
            "explanation": "McCabe's formula: V(G) = E - N + 2P (or Predicate Nodes + 1 for single component), giving the count of linearly independent basis paths."
        },
        {
            "id": "P2-T2-U8-109", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.2",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "A testing technique where input domain values are divided into classes from which test test cases are derived assuming all values in a class behave identically is:",
            "options": [{"label": "A", "text": "Equivalence Partitioning"}, {"label": "B", "text": "Boundary Value Analysis"}, {"label": "C", "text": "Mutation Testing"}, {"label": "D", "text": "Stress Testing"}],
            "answer": "A",
            "explanation": "Equivalence Partitioning divides inputs into valid and invalid equivalence classes; Boundary Value Analysis focuses on boundary limits (min, max)."
        },
        {
            "id": "P2-T2-U8-110", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which Gang of Four (GoF) design pattern ensures that a class has only one instance and provides a global point of access to it?",
            "options": [{"label": "A", "text": "Singleton Pattern"}, {"label": "B", "text": "Factory Method Pattern"}, {"label": "C", "text": "Observer Pattern"}, {"label": "D", "text": "Adapter Pattern"}],
            "answer": "A",
            "explanation": "Singleton restricts instantiation of a class to one single object, using a private constructor and a static instance getter method."
        },
        {
            "id": "P2-T2-U8-111", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The Observer design pattern establishes which type of dependency between objects?",
            "options": [{"label": "A", "text": "One-to-many dependency where state changes notify all dependents automatically"}, {"label": "B", "text": "One-to-one strictly bidirectional coupling"}, {"label": "C", "text": "Many-to-many random coupling"}, {"label": "D", "text": "No communication"}],
            "answer": "A",
            "explanation": "Observer defines a one-to-many subscription model: when the Subject changes state, all registered Observers are automatically notified."
        },
        {
            "id": "P2-T2-U8-112", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In UML class modeling, a solid line with a hollow diamond at the owner end represents which relationship?",
            "options": [{"label": "A", "text": "Aggregation ('has-a' weak ownership)"}, {"label": "B", "text": "Composition ('part-of' strong ownership)"}, {"label": "C", "text": "Generalization (Inheritance)"}, {"label": "D", "text": "Dependency"}],
            "answer": "A",
            "explanation": "Hollow diamond = Shared Aggregation (parts can exist without container); Filled black diamond = Composition (parts destroyed with container)."
        },
        {
            "id": "P2-T2-U8-113", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which UML diagram models the temporal sequence of messages exchanged between interacting lifeline objects over time?",
            "options": [{"label": "A", "text": "Sequence Diagram"}, {"label": "B", "text": "Use Case Diagram"}, {"label": "C", "text": "Deployment Diagram"}, {"label": "D", "text": "State Machine Diagram"}],
            "answer": "A",
            "explanation": "Sequence diagrams visualize dynamic runtime interactions, showing lifelines, activation bars, and chronological message flow."
        },
        {
            "id": "P2-T2-U8-114", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "In Agile Scrum methodology, what is the fixed time-boxed development cycle (typically 2 to 4 weeks) called?",
            "options": [{"label": "A", "text": "Sprint"}, {"label": "B", "text": "Epic"}, {"label": "C", "text": "Release Milestone"}, {"label": "D", "text": "Waterfall Wave"}],
            "answer": "A",
            "explanation": "A Sprint is a repeatable, time-boxed development period (usually 2–4 weeks) during which a Potentially Shippable Product Increment is built."
        },
        {
            "id": "P2-T2-U8-115", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Software architecture principles recommend designing system modules with:",
            "options": [{"label": "A", "text": "High Cohesion and Low Coupling"}, {"label": "B", "text": "Low Cohesion and High Coupling"}, {"label": "C", "text": "High Coupling and High Fan-out"}, {"label": "D", "text": "Zero Modularity"}],
            "answer": "A",
            "explanation": "Good software modularity mandates High Cohesion (elements within a module are closely focused) and Low Coupling (minimal inter-module dependency)."
        },
        {
            "id": "P2-T2-U8-116", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What type of maintenance is performed to adapt software to changes in external environments (new OS, new database, hardware upgrade)?",
            "options": [{"label": "A", "text": "Adaptive Maintenance"}, {"label": "B", "text": "Corrective Maintenance"}, {"label": "C", "text": "Perfective Maintenance"}, {"label": "D", "text": "Preventive Maintenance"}],
            "answer": "A",
            "explanation": "Adaptive maintenance modifies software to interface with changing environments; Corrective fixes bugs; Perfective enhances features."
        },
        {
            "id": "P2-T2-U8-117", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In the Capability Maturity Model (CMM), what is the highest process maturity level (Level 5)?",
            "options": [{"label": "A", "text": "Optimizing"}, {"label": "B", "text": "Defined"}, {"label": "C", "text": "Managed"}, {"label": "D", "text": "Repeatable"}],
            "answer": "A",
            "explanation": "CMM Levels: 1. Initial; 2. Repeatable; 3. Defined; 4. Managed; 5. Optimizing (continuous process improvement and innovation)."
        },
        {
            "id": "P2-T2-U8-118", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Regression Testing is executed after code modification primarily to:",
            "options": [{"label": "A", "text": "Ensure that code changes have not introduced new defects into existing working features"}, {"label": "B", "text": "Verify compiler syntax"}, {"label": "C", "text": "Benchmark maximum load"}, {"label": "D", "text": "Evaluate user documentation"}],
            "answer": "A",
            "explanation": "Regression testing re-runs previous test suites to verify that bug fixes or updates haven't broken existing functional capabilities."
        },
        {
            "id": "P2-T2-U8-119", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In UML Use Case diagrams, what relationship is used when a base use case unconditionally incorporates the behavior of another use case?",
            "options": [{"label": "A", "text": "<<include>> relationship"}, {"label": "B", "text": "<<extend>> relationship"}, {"label": "C", "text": "<<generalize>> relationship"}, {"label": "D", "text": "<<implements>> relationship"}],
            "answer": "A",
            "explanation": "`<<include>>` indicates mandatory inclusion of sub-behavior; `<<extend>>` indicates optional conditional extension behavior."
        },
        {
            "id": "P2-T2-U8-120", "paper": 2, "section_id": "U8", "subject": "Software Engineering", "syllabus_id": "P2-8.3",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Which SOLID design principle states that software entities should be open for extension, but closed for modification?",
            "options": [{"label": "A", "text": "Open/Closed Principle (OCP)"}, {"label": "B", "text": "Single Responsibility Principle (SRP)"}, {"label": "C", "text": "Liskov Substitution Principle (LSP)"}, {"label": "D", "text": "Dependency Inversion Principle (DIP)"}],
            "answer": "A",
            "explanation": "Bertrand Meyer's Open/Closed Principle mandates that class behaviors should be extensible via inheritance or interfaces without altering source code."
        }
    ]
    qs.extend(u8)

    # ----------------------------------------------------
    # UNIT 9: WEB TECHNOLOGIES & INTERNET APPLICATIONS (15 QUESTIONS: Q121 to Q135)
    # ----------------------------------------------------
    u9 = [
        {
            "id": "P2-T2-U9-121", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "Which HTML5 semantic element is intended to encapsulate autonomous, self-contained content such as a blog post or news story?",
            "options": [{"label": "A", "text": "<article>"}, {"label": "B", "text": "<section>"}, {"label": "C", "text": "<div>"}, {"label": "D", "text": "<aside>"}],
            "answer": "A",
            "explanation": "HTML5 `<article>` represents independent, self-contained content distributable or reusable independently (e.g. forum post, news report)."
        },
        {
            "id": "P2-T2-U9-122", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In the standard CSS Box Model, what is the order of areas from innermost to outermost?",
            "options": [{"label": "A", "text": "Content -> Padding -> Border -> Margin"}, {"label": "B", "text": "Content -> Border -> Padding -> Margin"}, {"label": "C", "text": "Margin -> Border -> Padding -> Content"}, {"label": "D", "text": "Content -> Margin -> Padding -> Border"}],
            "answer": "A",
            "explanation": "Innermost is Content, enclosed by Padding (space inside border), then Border, and finally Margin (transparent space outside border)."
        },
        {
            "id": "P2-T2-U9-123", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "When `box-sizing: border-box` is declared in CSS, what does an element's specified `width` include?",
            "options": [{"label": "A", "text": "Content + Padding + Border"}, {"label": "B", "text": "Content only"}, {"label": "C", "text": "Content + Margin"}, {"label": "D", "text": "Padding only"}],
            "answer": "A",
            "explanation": "`border-box` includes padding and borders in the element's total width and height calculation, preventing layout overflows."
        },
        {
            "id": "P2-T2-U9-124", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "In JavaScript (ES6), how do variables declared with `const` differ from those declared with `let`?",
            "options": [{"label": "A", "text": "const variables cannot be reassigned; let variables can be reassigned"}, {"label": "B", "text": "const has function scope; let has block scope"}, {"label": "C", "text": "const variables are hoisted with assignment"}, {"label": "D", "text": "const can only hold numbers"}],
            "answer": "A",
            "explanation": "Both `let` and `const` are block-scoped; `let` allows reassignment while `const` establishes an immutable variable identifier binding."
        },
        {
            "id": "P2-T2-U9-125", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the return value of the expression `typeof null` in standard JavaScript?",
            "options": [{"label": "A", "text": "\"object\""}, {"label": "B", "text": "\"null\""}, {"label": "C", "text": "\"undefined\""}, {"label": "D", "text": "\"boolean\""}],
            "answer": "A",
            "explanation": "Due to a historic bug in JS's initial implementation where object tags were 000, `typeof null` evaluates to the string `\"object\"`."
        },
        {
            "id": "P2-T2-U9-126", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the equality comparison result of `0 == '0'` and `0 === '0'` in JavaScript respectively?",
            "options": [{"label": "A", "text": "true and false"}, {"label": "B", "text": "false and true"}, {"label": "C", "text": "true and true"}, {"label": "D", "text": "false and false"}],
            "answer": "A",
            "explanation": "`==` performs type coercion converting string '0' to number 0 (true); `===` checks both type and value without coercion (number vs string = false)."
        },
        {
            "id": "P2-T2-U9-127", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "hard",
            "text": "A JavaScript closure is created when:",
            "options": [{"label": "A", "text": "An inner function retains access to outer lexical environment variables even after outer function execution finishes"}, {"label": "B", "text": "A function is called asynchronously with setTimeout"}, {"label": "C", "text": "A class method is bound to this"}, {"label": "D", "text": "A promise rejects"}],
            "answer": "A",
            "explanation": "A closure is the combination of a function bundled together with references to its surrounding lexical state."
        },
        {
            "id": "P2-T2-U9-128", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "In RESTful API architectural design, which HTTP method is standardly used to modify an existing resource partially?",
            "options": [{"label": "A", "text": "PATCH"}, {"label": "B", "text": "PUT"}, {"label": "C", "text": "POST"}, {"label": "D", "text": "GET"}],
            "answer": "A",
            "explanation": "PUT replaces the entire resource representation; PATCH applies partial modifications to an existing resource."
        },
        {
            "id": "P2-T2-U9-129", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Which HTTP status code range indicates a client-side error (e.g., 404 Not Found, 401 Unauthorized)?",
            "options": [{"label": "A", "text": "4xx"}, {"label": "B", "text": "2xx"}, {"label": "C", "text": "3xx"}, {"label": "D", "text": "5xx"}],
            "answer": "A",
            "explanation": "1xx: Informational; 2xx: Success; 3xx: Redirection; 4xx: Client Error; 5xx: Server Error."
        },
        {
            "id": "P2-T2-U9-130", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "JSON (JavaScript Object Notation) data format does NOT natively support which data type?",
            "options": [{"label": "A", "text": "Date / Function objects"}, {"label": "B", "text": "Boolean"}, {"label": "C", "text": "Array"}, {"label": "D", "text": "Number"}],
            "answer": "A",
            "explanation": "JSON natively supports only: string, number, object, array, boolean, and null. Dates are represented as ISO strings; functions are unsupported."
        },
        {
            "id": "P2-T2-U9-131", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.4",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "medium",
            "text": "Cross-Site Scripting (XSS) web vulnerability is executed by:",
            "options": [{"label": "A", "text": "Injecting malicious client-side JavaScript scripts into web pages viewed by other users"}, {"label": "B", "text": "Manipulating backend SQL queries"}, {"label": "C", "text": "Overwhelming the server with traffic"}, {"label": "D", "text": "Guessing user passwords"}],
            "answer": "A",
            "explanation": "XSS occurs when unvalidated user input is rendered in the browser, executing malicious JavaScript to steal cookies and hijack sessions."
        },
        {
            "id": "P2-T2-U9-132", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What is the primary countermeasure against SQL Injection attacks in web applications?",
            "options": [{"label": "A", "text": "Parameterized queries / Prepared Statements"}, {"label": "B", "text": "Client-side JavaScript regex validation"}, {"label": "C", "text": "HTTPS encryption"}, {"label": "D", "text": "Hiding database error messages"}],
            "answer": "A",
            "explanation": "Prepared Statements with parameterized queries ensure that user input is treated strictly as data literals, never executable SQL commands."
        },
        {
            "id": "P2-T2-U9-133", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "Cross-Site Request Forgery (CSRF) attacks are standardly prevented by:",
            "options": [{"label": "A", "text": "Anti-CSRF synchronizer tokens and SameSite cookie attributes"}, {"label": "B", "text": "Base64 encoding passwords"}, {"label": "C", "text": "CSS styling"}, {"label": "D", "text": "Disabling JavaScript"}],
            "answer": "A",
            "explanation": "Anti-CSRF unique tokens validate that state-changing requests originated from the genuine application UI; SameSite cookies block third-party transmission."
        },
        {
            "id": "P2-T2-U9-134", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.2",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "In the JavaScript asynchronous event loop, in what order are execution queues serviced after call stack completion?",
            "options": [{"label": "A", "text": "Microtask Queue (Promises) -> Macrotask Queue (setTimeout/setInterval)"}, {"label": "B", "text": "Macrotask Queue -> Microtask Queue"}, {"label": "C", "text": "Random interleaving"}, {"label": "D", "text": "FIFO exclusively"}],
            "answer": "A",
            "explanation": "When the call stack empties, the event loop drains all pending Microtasks (Promise handlers, queueMicrotask) before picking the next Macrotask."
        },
        {
            "id": "P2-T2-U9-135", "paper": 2, "section_id": "U9", "subject": "Web Technologies", "syllabus_id": "P2-9.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "easy",
            "text": "Which CSS property is used in Flexbox layout to align flex items along the main axis?",
            "options": [{"label": "A", "text": "justify-content"}, {"label": "B", "text": "align-items"}, {"label": "C", "text": "flex-direction"}, {"label": "D", "text": "align-content"}],
            "answer": "A",
            "explanation": "`justify-content` aligns items along the main axis (flex-start, center, space-between); `align-items` aligns along the cross axis."
        }
    ]
    qs.extend(u9)

    # ----------------------------------------------------
    # UNIT 10: INFORMATION SECURITY & EMERGING TRENDS (15 QUESTIONS: Q136 to Q150)
    # ----------------------------------------------------
    u10 = [
        {
            "id": "P2-T2-U10-136", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "In Symmetric-Key Cryptography, how many secret keys are utilized for encryption and decryption?",
            "options": [{"label": "A", "text": "Single shared secret key"}, {"label": "B", "text": "Two mathematically paired keys (public and private)"}, {"label": "C", "text": "Four keys"}, {"label": "D", "text": "Zero keys"}],
            "answer": "A",
            "explanation": "Symmetric cryptography (e.g. AES, DES) uses one identical shared key for both encryption and decryption."
        },
        {
            "id": "P2-T2-U10-137", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "The RSA public-key cryptographic algorithm derives its mathematical security from the computational hardness of:",
            "options": [{"label": "A", "text": "Factoring large composite numbers into prime factors"}, {"label": "B", "text": "Discrete logarithm problem on elliptic curves"}, {"label": "C", "text": "Solving polynomial roots"}, {"label": "D", "text": "Traveling Salesperson problem"}],
            "answer": "A",
            "explanation": "RSA (Rivest-Shamir-Adleman) relies on the integer factorization problem: multiplying two large primes is easy, but factoring their product is computationally infeasible."
        },
        {
            "id": "P2-T2-U10-138", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What property of cryptographic hash functions (like SHA-256) guarantees that two different inputs cannot produce the identical hash digest?",
            "options": [{"label": "A", "text": "Collision Resistance"}, {"label": "B", "text": "Pre-image Resistance"}, {"label": "C", "text": "Reversibility"}, {"label": "D", "text": "Commutativity"}],
            "answer": "A",
            "explanation": "Collision Resistance ensures it is computationally infeasible to find any two distinct messages x and y such that hash(x) == hash(y)."
        },
        {
            "id": "P2-T2-U10-139", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "To create an authentic Digital Signature for a message, the sender encrypts the document hash using:",
            "options": [{"label": "A", "text": "Sender's Private Key"}, {"label": "B", "text": "Sender's Public Key"}, {"label": "C", "text": "Recipient's Public Key"}, {"label": "D", "text": "Recipient's Private Key"}],
            "answer": "A",
            "explanation": "Digital signatures are generated using the Sender's Private Key (guaranteeing non-repudiation and authenticity), verified by anyone using Sender's Public Key."
        },
        {
            "id": "P2-T2-U10-140", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Cloud Computing service models, Google Docs and Microsoft 365 are canonical examples of:",
            "options": [{"label": "A", "text": "SaaS (Software as a Service)"}, {"label": "B", "text": "PaaS (Platform as a Service)"}, {"label": "C", "text": "IaaS (Infrastructure as a Service)"}, {"label": "D", "text": "FaaS (Function as a Service)"}],
            "answer": "A",
            "explanation": "SaaS delivers fully operational end-user applications over the web; PaaS delivers runtime dev environments; IaaS delivers VMs, storage, and networks."
        },
        {
            "id": "P2-T2-U10-141", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "How do OS-level Containers (e.g., Docker) differ fundamentally from traditional Hypervisor Virtual Machines (VMs)?",
            "options": [{"label": "A", "text": "Containers share the host OS kernel and package only user-space binaries and libraries"}, {"label": "B", "text": "Containers require a complete guest operating system"}, {"label": "C", "text": "VMs are lighter and boot faster than containers"}, {"label": "D", "text": "Containers emulate hardware CPU instructions"}],
            "answer": "A",
            "explanation": "Docker containers share the host kernel via cgroups and namespaces, making them lightweight and fast compared to VMs carrying full guest OS kernels."
        },
        {
            "id": "P2-T2-U10-142", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Machine Learning, training a model on unlabelled data to discover hidden clusters and patterns without target output labels is called:",
            "options": [{"label": "A", "text": "Unsupervised Learning"}, {"label": "B", "text": "Supervised Learning"}, {"label": "C", "text": "Reinforcement Learning"}, {"label": "D", "text": "Supervised Classification"}],
            "answer": "A",
            "explanation": "Unsupervised learning (e.g., K-Means clustering, PCA) finds inherent groupings in unlabelled datasets; Supervised learning trains on labeled (X, y) pairs."
        },
        {
            "id": "P2-T2-U10-143", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Artificial Neural Networks, the non-linear mathematical function that decides whether a neuron should fire is called an:",
            "options": [{"label": "A", "text": "Activation Function (e.g., ReLU, Sigmoid)"}, {"label": "B", "text": "Loss Function"}, {"label": "C", "text": "Optimizer"}, {"label": "D", "text": "Backpropagator"}],
            "answer": "A",
            "explanation": "Activation functions (ReLU, Sigmoid, Tanh) introduce non-linearity into neural networks, enabling them to learn complex non-linear decision boundaries."
        },
        {
            "id": "P2-T2-U10-144", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Blockchain technology, how are blocks cryptographically chained together to make history tamper-evident?",
            "options": [{"label": "A", "text": "Each block contains the cryptographic hash of the previous block's header"}, {"label": "B", "text": "Blocks are linked via physical Ethernet cables"}, {"label": "C", "text": "A central database administrator signs all blocks"}, {"label": "D", "text": "Blocks are indexed by row count"}],
            "answer": "A",
            "explanation": "Every block references `Previous_Block_Hash`. Altering any past block invalidates all subsequent block hashes across the distributed ledger."
        },
        {
            "id": "P2-T2-U10-145", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.4",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Internet of Things (IoT) ecosystems, which lightweight publish-subscribe messaging protocol designed for constrained low-bandwidth devices is standardly used?",
            "options": [{"label": "A", "text": "MQTT (Message Queuing Telemetry Transport)"}, {"label": "B", "text": "HTTP 1.1"}, {"label": "C", "text": "FTP"}, {"label": "D", "text": "Telnet"}],
            "answer": "A",
            "explanation": "MQTT is a minimal publish/subscribe protocol with tiny 2-byte packet headers, ideal for battery-operated IoT sensors over cellular/satellite links."
        },
        {
            "id": "P2-T2-U10-146", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.1",
            "origin_tag": "PYQ - KPSC CST 2017", "label": "PYQ", "difficulty": "easy",
            "text": "The CIA Triad constitutes the foundational pillars of information security. What does CIA stand for?",
            "options": [{"label": "A", "text": "Confidentiality, Integrity, Availability"}, {"label": "B", "text": "Central Intelligence Agency"}, {"label": "C", "text": "Control, Identification, Authentication"}, {"label": "D", "text": "Cryptography, IP, Authorization"}],
            "answer": "A",
            "explanation": "Confidentiality (preventing unauthorized reading), Integrity (preventing unauthorized modification), and Availability (ensuring authorized access when needed)."
        },
        {
            "id": "P2-T2-U10-147", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.1",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "What type of cryptographic attack precomputes millions of password hashes into indexed lookup tables to reverse password digests rapidly?",
            "options": [{"label": "A", "text": "Rainbow Table Attack"}, {"label": "B", "text": "Brute Force Attack"}, {"label": "C", "text": "Man-in-the-Middle Attack"}, {"label": "D", "text": "DNS Poisoning"}],
            "answer": "A",
            "explanation": "Rainbow tables trade space for time by storing precomputed hash chains; defended by adding unique random Salt to passwords before hashing."
        },
        {
            "id": "P2-T2-U10-148", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.2",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In Kubernetes container orchestration architecture, what is the smallest, basic deployable compute unit that encapsulates one or more containers?",
            "options": [{"label": "A", "text": "Pod"}, {"label": "B", "text": "Node"}, {"label": "C", "text": "Cluster"}, {"label": "D", "text": "Ingress"}],
            "answer": "A",
            "explanation": "A Pod represents a single instance of a running process in Kubernetes, sharing network namespace (IP) and storage volumes among its containers."
        },
        {
            "id": "P2-T2-U10-149", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.3",
            "origin_tag": "Expected - High Yield", "label": "expected", "difficulty": "medium",
            "text": "In machine learning evaluation metrics, what is the harmonic mean of Precision and Recall called?",
            "options": [{"label": "A", "text": "F1-Score"}, {"label": "B", "text": "Accuracy"}, {"label": "C", "text": "ROC-AUC"}, {"label": "D", "text": "Root Mean Squared Error"}],
            "answer": "A",
            "explanation": "F1-Score = 2 * (Precision * Recall) / (Precision + Recall), providing an balanced evaluation metric especially on imbalanced datasets."
        },
        {
            "id": "P2-T2-U10-150", "paper": 2, "section_id": "U10", "subject": "Information Security", "syllabus_id": "P2-10.1",
            "origin_tag": "Synthesized - Hard", "label": "expected", "difficulty": "hard",
            "text": "Diffie-Hellman Key Exchange allows two parties to establish a shared secret key over an insecure channel without transmitting the key. It is vulnerable to:",
            "options": [{"label": "A", "text": "Man-in-the-Middle (MitM) attack if unauthenticated"}, {"label": "B", "text": "SQL Injection"}, {"label": "C", "text": "Buffer Overflow"}, {"label": "D", "text": "Cross-Site Scripting"}],
            "answer": "A",
            "explanation": "Classic Diffie-Hellman does not authenticate the communicating parties; an active attacker can intercept and establish independent keys with both sides (MitM)."
        }
    ]
    qs.extend(u10)

    return qs

print("Paper 2 Test 2 all 150 questions assembled.")
