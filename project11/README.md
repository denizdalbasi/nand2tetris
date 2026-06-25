# Jack Compiler Utilities

This project contains two helpful Python classes for building a **Jack Compiler** (from the Nand2Tetris course). These classes help you manage variables and write Virtual Machine (VM) code easily.

## What is inside?

1. **`SymbolTable`**: This class keeps track of all the variables in your Jack program. It knows their names, types (like `int` or `boolean`), kinds (like `static` or `local`), and their index numbers.
2. **`VMWriter`**: This class helps you write correct VM instructions into a text file. It handles all the basic commands like `push`, `pop`, arithmetic operations, and loops.