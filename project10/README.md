# Project 10: Syntax Analyzer (Compiler Part 1) - Nand2Tetris

Welcome to Project 10 of the Nand2Tetris course. In this project, i  will build a **Syntax Analyzer**. This is the first part of the compiler that translates Jack code into Hack computer instructions.

---

## What does this project do?
A syntax analyzer reads my source code (written in the Jack language) and checks if the grammar is correct. 

Instead of translating the code into machine language right away, this project translates the code into an **XML structure** (a parse tree). This helps us see if our analyzer understands the structure of the Jack program correctly.

The analyzer does two main jobs:
1. **The Tokenizer:** Breaks the code into small pieces like keywords, symbols, identifiers, and constants.
2. **The Compilation Engine:** Uses the tokens to understand the grammar rules (like `if`, `while`, or mathematical expressions) and writes the XML output.