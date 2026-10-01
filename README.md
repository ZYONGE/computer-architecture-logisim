<div align="center">

# computer-architecture-logisim

Source code for the **Computer Architecture** course

</div>

### Simulator
<div>
  <img src="https://img.shields.io/badge/Logisim-2.7.1-1F6FEB?style=for-the-badge" alt="Logisim 2.7.1" />
</div>

### Runtime
<div>
  <img src="https://img.shields.io/badge/OpenJDK%2017-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="OpenJDK 17" />
</div>

### Version Control
<div>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-586069?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</div>

### AI Agents
<div>
  <img src="https://img.shields.io/badge/Claude%20Code-D97757?style=for-the-badge&logo=claude&logoColor=white" alt="Claude Code" />
</div>

---
## Project Overview
**Course:** Computer Architecture  
**University:** Tech University of Korea (TUK)

This repository contains the Logisim circuits used in the Computer Architecture lab sessions, from basic logic gates up to an 8-bit ALU.
The `.circ` files come with the lecture material; this repository keeps them together with notes on what each circuit shows.

The purpose of this project is to:

- understand the basic gates that digital logic systems are built from
- see how the ALU inside a CPU is assembled from those gates (logic unit, adder/subtractor, comparator)
- keep a structured record of lecture exercises

---
## Project Structure

```
computer-architecture-logisim/
├── 실습2-로지심/
│   ├── 1. 기본게이트.circ
│   ├── 2. ALU-Logic 파트.circ
│   ├── 3. ALU-감가산기 파트.circ
│   ├── 4. ALU-비교기 파트.circ
│   └── 5. 8bit ALU.circ
├── LICENSE                # MIT License
├── .gitignore
└── README.md
```

Practice folders are named after the lab number in the lecture material (`실습N-<topic>`).

---
## Practice Circuits (`실습2-로지심/`)

| File | Circuit | What it shows |
|------|---------|---------------|
| `1. 기본게이트.circ` | NOT, buffer, tri-state buffer, AND / OR / NAND / NOR (2- and 3-input), XOR, XNOR | Behavior of every basic gate; the wire color shows the signal level |
| `2. ALU-Logic 파트.circ` | 1-bit and 4-bit logic unit | AND, OR, XOR, NOT computed side by side; a 4:1 multiplexer selects one result |
| `3. ALU-감가산기 파트.circ` | Half adder, full adder, 4-bit adder, 4-bit adder/subtractor | Addition and subtraction built from gates and from Logisim's built-in adder, with an overflow output |
| `4. ALU-비교기 파트.circ` | `1bit 비교기`, `4bit 비교기` | Compares A and B and outputs greater / less / equal; four 1-bit stages make the 4-bit comparator |
| `5. 8bit ALU.circ` | 8-bit ALU without the logic unit (`FullAdder`, `8BitAdder`, `Not`, `Zero`) | Control inputs choose the operation on R1/R2 and write R0, with carry, overflow, zero and sign flags |

Logic unit select lines (`2. ALU-Logic 파트.circ`):

| `S2 S1` | Operation |
|---------|-----------|
| `00` | AND |
| `01` | OR |
| `10` | XOR |
| `11` | NOT |

8-bit ALU control points (`5. 8bit ALU.circ`, switch on exactly one):

| Control | Operation |
|---------|-----------|
| `ADD` | R0 ← R1 + R2 |
| `SUB` | R0 ← R1 − R2 |
| `INC` | R0 ← R2 + 1 |
| `2's complement` | R0 ← ~R2 + 1 |

---
## What I Learned

### Basic Gates
- NOT inverts its input; AND outputs 1 only when every input is 1; OR outputs 1 when at least one input is 1
- NAND, NOR and XNOR are AND, OR and XOR followed by a NOT; XOR outputs 1 only when an odd number of inputs are 1
- A buffer passes its input through unchanged (used to extend fan-out)
- A tri-state buffer leaves its output disconnected (floating) when the control input is 0
- In simulate mode: dark green wire = 0, bright green wire = 1, blue wire = floating

### Logic Unit with a Multiplexer
- Compute every candidate result in parallel, then let the select lines pick one
- An n-bit unit is n copies sharing the same select lines, which is how a real ALU is wired across the word length

### Adders and Subtractors
- Half adder: `S = A ⊕ B`, `C = A · B`
- Full adder: `S = A ⊕ B ⊕ Cin`, `Cout = Cin · (A ⊕ B) + A · B`
- A 4-bit ripple-carry adder feeds each stage's carry-out into the next stage's carry-in
- Subtraction reuses the adder: XOR every bit of B with the control signal (0 = add, 1 = subtract) and use the control signal as the first carry-in, so `A − B = A + ~B + 1`
- Overflow = carry into the MSB ⊕ carry out of the MSB

### Comparator
- A 1-bit comparator takes A, B and the "greater / less / equal" results of the previous stage, and outputs the updated three results
- The 4-bit comparator chains four 1-bit comparators; the "equal" input of the first stage is set to 1

### 8-bit ALU
- A control unit decodes the operator part of an instruction and turns exactly one control point on
- All four operations go through one 8-bit adder; helper blocks (`Not`, `Zero`, a "plus 1" selector) adjust its inputs
- The status flags (carry, overflow, zero, sign) are produced alongside the result

---
## How to Run

1. Install Java. Logisim 2.7.1 is a Java application (tested with OpenJDK 17 on macOS).
2. Get Logisim 2.7.1, the version used in the lecture, from <http://www.cburch.com/logisim/> (download page: <https://sourceforge.net/projects/circuit/>).
3. Start it with `java -jar <Logisim 2.7.1 jar>`.
   - The lecture's `logisim-win-2.7.1.exe` is itself a Java archive, so `java -jar logisim-win-2.7.1.exe` also works on macOS.
4. Choose **File → Open** and open a `.circ` file from `실습2-로지심/`.
5. Select the hand tool (simulate mode) and click an input pin to toggle it between 0 and 1; the outputs update immediately.

The lecture PDFs and the Windows installer are not part of this repository (see [.gitignore](.gitignore)).

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

The `.circ` lab circuits were provided by the course instructor with the lecture material; the license covers this repository's own content.


## Author
Name: Jiyong Kim (ZYONGE)  
Profile: https://github.com/ZYONGE  

## Motivation
For A+ !!!
