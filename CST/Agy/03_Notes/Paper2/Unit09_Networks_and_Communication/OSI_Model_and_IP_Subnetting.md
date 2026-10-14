---
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
> - Data units (PDU): Bits $\to$ Frames $\to$ Packets $\to$ Segments $\to$ Data.
> - TCP 3-Way Handshake ($SYN \to SYN-ACK \to ACK$) and Connection Teardown ($FIN \to ACK \to FIN \to ACK$).
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
    participant C as TCP Client
    participant S as TCP Server
    
    Note over C, S: Client in CLOSED and Server in LISTEN
    C->>S: SYN (Seq = x)
    Note over S: Server enters SYN_RCVD
    S->>C: SYN-ACK (Seq = y, Ack = x + 1)
    Note over C: Client enters ESTABLISHED
    C->>S: ACK (Seq = x + 1, Ack = y + 1)
    Note over S: Server enters ESTABLISHED
    Note over C, S: Full-Duplex Data Transfer Active
```

The sequence diagram above illustrates the 3-Way Handshake protocol establishing synchronized sequence numbers.

### 2.2 Connection Teardown (4-Way Handshake)

```mermaid
sequenceDiagram
    autonumber
    participant C as TCP Client
    participant S as TCP Server
    
    C->>S: FIN (Seq = u)
    S->>C: ACK (Ack = u + 1)
    Note over S: Server flushes remaining data buffer
    S->>C: FIN (Seq = v)
    C->>S: ACK (Ack = v + 1)
    Note over C: Client waits 2MSL timer before CLOSED
    Note over S: Server enters CLOSED
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
  $$\mathbf{\text{Usable Hosts} = 2^H - 2}$$
  *(1st address is Network Address; last address is Directed Broadcast Address).*\n