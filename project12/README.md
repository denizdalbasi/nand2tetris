# Nand2Tetris - Project 12: The Operating System

This project contains the complete code for the **Jack Operating System (OS)**. Classes written in Jack programming language. With this OS, Jack programs can talk directly to the Hack computer hardware.

---

## The 8 OS Classes Included

### 1. `Sys.jack`

This class starts the OS. When you turn on the computer, the method starts all the other OS classes and then opens your main program. It also handles system freezes and execution delays.

### 2. `Memory.jack`

This class manages the computer's RAM. It manages heap memory allocations.

- `Memory.peek(address)`: Reads data directly from a RAM address.
- `Memory.poke(address, value)`: Writes data directly to a RAM address.
- `Memory.alloc(size)` & `Memory.dealloc(object)`: Handles dynamic memory allocation and cleanup.

### 3. `Math.jack`

This class provides basic mathematical functions because the Hack hardware cannot do math by itself.

### 4. `Array.jack`

A very simple class that lets Jack programs use dynamic arrays. It connects the `Array.new()` method directly to `Memory.alloc()`.

### 5. `String.jack`

This class manages text strings. It handles dynamic memory allocations for text and safely converts integers into text characters (ASCII values) and vice versa.

### 6. `Screen.jack`

This class handles drawing graphics on the Hack physical screen.

### 7. `Output.jack`

This class handles printing text characters on the screen.

### 8. `Keyboard.jack`

This class listens to the Hack keyboard memory-mapped register. It allows the software to read individual pressed keys, read full text strings, and accept integer inputs from users.
