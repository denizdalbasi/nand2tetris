# Nand2Tetris: Building a 16-bit Computer
**From Logic Gates to a Complete Computer System**

This repository shows my progress in the Nand2Tetris course. The goal is to build a modern computer from scratch. I started with a single NAND gate and used it to build all the necessary hardware and software parts.

## Progress: Project 1 Complete
I built basic logic gates using Hardware Description Language (HDL).
- **Basic gates:** `Not`, `And`, `Or`, `Xor`, `Mux`, `Demux`
- **16-bit versions:** `Not16`, `And16`, `Or16`, `Mux16`
- **Complex gates:** `Or8Way`, `Mux4Way16`, `Mux8Way16`, `DMux4Way`, `DMux8Way`
- **Extra:** `IsEqual`, `Majority`, `Mux3Way16`, `And3`, `Or3`.

## Progress: Project 2 Complete
I built the arithmetic parts of the computer.
- **Adders:** `HalfAdder`, `FullAdder`, `Add16`, `Inc16`
- **ALU:** The Arithmetic Logic Unit, which performs 18 different math and logic operations. 

## Progress: Project 3 Complete
I added memory so the computer can "remember" data.
- **Storage:** `Bit` and `Register` (16-bit).
- **RAM:** Various sizes (`RAM8` to `RAM16K`).
- **PC:** The Program Counter, which keeps track of the next instruction to run. 

[Image of D flip-flop circuit diagram]


## Progress: Project 4 Complete
I wrote programs in Hack Assembly Language to learn how software talks to the hardware.
- **Mult.asm:** A program to multiply two numbers.
- **Fill.asm:** An interactive program that paints the screen black when you press a key on the keyboard.

## Progress: Project 5 Complete
I put everything together to create the full Hack Computer architecture.
- **CPU:** The brain of the computer that handles all instructions.
- **Memory:** A single address space for RAM, the Screen, and the Keyboard.
- **Computer:** The final chip that connects the CPU, Memory, and ROM to run programs.

## Progress: Project 6 Complete
I built an **Assembler** using Python. It translates the Assembly code (text) into binary machine code (0s and 1s) that the computer understands.
- **Two-pass translation:** It reads the code twice to turn symbols (like labels and variables) into real addresses.
- **Code translation:** It converts instructions into the 16-bit binary format.

## Progress: Project 7 & 8 Complete
I built a **Virtual Machine (VM) Translator**. This allows high-level code to run on our computer.
- **Stack-based logic:** I implemented commands like `push`, `pop`, `add`, and `sub`.
- **Program flow:** I added `label`, `goto`, and `if-goto` to control how the program runs.
- **Functions:** I implemented `function`, `call`, and `return` so the computer can run complex, multi-file programs. 

## Progress: Project 9 Complete
I built a game using the **Jack** programming language.
- **Snake Game:** I created an interactive game where the user moves a snake around the screen to "eat" and grow.
- **Object-Oriented Design:** I used classes like `Snake`, `Game`, and `Main` to organize my code.
- **Interactivity:** The game uses the keyboard to change direction and the screen memory map to draw the movement in real-time.

## Progress: Project 10 Complete
I built a **Syntax Analyzer** for the **Jack** programming language. This project acts as the first half of the compiler, parsing human-readable code into a structured format.

* **Tokenizer (Lexical Analysis):** Developed a `JackTokenizer` to break the source code into meaningful tokens (keywords, symbols, identifiers, constants) while removing comments and whitespace.
* **Compilation Engine:** Implemented a recursive descent parser that enforces the Jack grammar rules. 
* **XML Output:** Created a `CompilationEngine` that generates an XML representation of the code's hierarchical structure (parse tree), confirming that the program logic is correctly understood by the parser.