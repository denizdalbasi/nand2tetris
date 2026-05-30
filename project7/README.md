# Hack VM Translator (Part 1)

This project is a Virtual Machine (VM) Translator built for the **Nand2Tetris** curriculum (Project 7). It translates VM code written in the Hack VM language into standard Hack Assembly (`.asm`) code, which can then be assembled into binary machine code.

Currently, this translator handles stack arithmetic commands, logical commands, and basic memory segments (`constant`, `local`, and `argument`).

---

## Features

* **Arithmetic/Logical Operations:** Fully supports `add`, `sub`, `neg`, `eq`, `gt`, `lt`, `and`, `or`, and `not`.
* **Memory Access:** Supports `push` and `pop` commands for `constant`, `local`, and `argument` memory segments.
* **Batch Processing:** Processes either a single `.vm` file or an entire directory containing multiple `.vm` files into a single `.asm` output file.
* **Clean Code Parsing:** Filters out inline/block comments and whitespace to extract pure VM instructions.

---

## Project Structure

* `codeWritter.py`: Generates the target Hack assembly code from parsed VM commands.
* `parse.py`: Reads the VM file, handles formatting, and breaks down the commands into their internal components (`commandType`, `arg1`, `arg2`).
* `main.py`: The entry point script that orchestrates file/folder directory detection, loops through code files, and drives the compilation workflow.
