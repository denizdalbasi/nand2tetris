# Hack VM Translator (Full Implementation - Project 8)

This project is a complete **Virtual Machine (VM) Translator** built for the **Nand2Tetris** course (covering both Project 7 and Project 8). 

It takes intermediate VM code (which looks a bit like Java bytecode) and translates it into low-level **Hack Assembly code (`.asm`)**. This assembly code can then be run on the Hack CPU Emulator.

While Project 7 only handled basic math and simple memory access, **Project 8** turns this into a full compiler backend by adding loops, logic branches, and function calls.

---

## Key Features

* **Math & Logic:** Translates commands like `add`, `sub`, `neg`, `eq`, `gt`, `lt`, `and`, `or`, and `not`.
* **Full Memory Control:** Works with all 8 virtual memory areas (`constant`, `local`, `argument`, `this`, `that`, `pointer`, `temp`, and `static`).
* **Loops and Choices:** Handles branching commands like `label`, `goto`, and `if-goto`. It safely locks labels inside their own functions so they don't accidentally mix up.
* **Function Management:** Manages complex code routines using `function`, `call`, and `return`. It carefully saves the computer's memory state on a "stack" before starting a function, and restores everything exactly as it was when the function finishes.
* **Bootstrap Code:** Automatically adds a small initialization script (`SP=256` and a call to start `Sys.init`) whenever you translate a whole folder of files together.
* **Smart File Processing:** Can translate a single `.vm` file or bundle an entire folder of multiple `.vm` files into one final `.asm` file.

---

## How the Code is Structured

The translator uses three main files to do its job:

1. **`main.py`**: The manager. It looks at your files, creates the output assembly file, adds the startup bootstrap code if needed, and runs the translation loop.
2. **`parse.py`**: The reader. It cleans up the raw text by throwing away blank lines and comments, then breaks each VM command down into clean pieces.
3. **`codeWritter.py`**: The builder. This is where the heavy lifting happens. It takes the clean VM pieces and writes out the matching Hack Assembly instructions.
