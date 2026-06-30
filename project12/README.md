# Nand2Tetris - Project 12: The Operating System

This project contains the complete code for the **Jack Operating System (OS)**. The OS is a group of 8 standard library classes written in the high-level Jack programming language. It fills the final gap in the Nand2Tetris software stack. With this OS, Jack programs can talk directly to the Hack computer hardware.

---

## The 8 OS Classes Included

### 1. `Sys.jack`

This class starts the OS. When you turn on the computer, it runs `Sys.init()`. This method starts all the other OS classes and then opens your main program (`Main.main()`). It also handles system freezes (`Sys.halt()`) and execution delays (`Sys.wait()`).

### 2. `Memory.jack`

This class manages the computer's RAM. It uses a **First-Fit Linked List** method to manage heap memory allocations (from address `2048` to `16383`).

- `Memory.peek(address)`: Reads data directly from a RAM address.
- `Memory.poke(address, value)`: Writes data directly to a RAM address.
- `Memory.alloc(size)` & `Memory.dealloc(object)`: Handles dynamic memory allocation and cleanup.

### 3. `Math.jack`

This class provides basic mathematical functions because the Hack hardware cannot do math by itself.

- It uses an array of powers-of-two to check bits quickly.
- It implements an efficient binary shift-and-add method for **multiplication**.
- It implements a recursive long-division method for **division**.
- It implements a binary search method to find **square roots** ($\sqrt{x}$).

### 4. `Array.jack`

A very simple class that lets Jack programs use dynamic arrays. It connects the `Array.new()` method directly to `Memory.alloc()`.

### 5. `String.jack`

This class manages text strings. It handles dynamic memory allocations for text and safely converts integers into text characters (ASCII values) and vice versa.

### 6. `Screen.jack`

This class handles drawing graphics on the Hack physical screen (from address `16384` to `24575`).

- It draws single pixels by calculating exact memory bitmasks.
- It implements **Bresenham's Line Algorithm** to draw straight diagonal lines without using slow floating-point math.
- It quickly draws filled rectangles.

### 7. `Output.jack`

This class handles printing text characters on the screen. It maps fixed 11x8 pixel matrix fonts for every character in the ASCII table and manages the cursor's row and column positions.

### 8. `Keyboard.jack`

This class listens to the Hack keyboard memory-mapped register (address `24576`). It allows the software to read individual pressed keys, read full text strings, and accept integer inputs from users.
