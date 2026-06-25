# Nand2Tetris - Project 12: The Operating System

This project contains the complete implementation of the **Jack Operating System (OS)**. The OS is a collection of 8 standard library classes written in the high-level Jack language. It closes the final gap in the Nand2Tetris software stack, allowing Jack programs to talk directly to the Hack computer hardware.

---

## The 8 OS Classes Included

### 1. `Sys.jack`
The bootstrapper of the OS. When the computer turns on, it runs `Sys.init()`, which initializes all the other OS classes and then starts your main program (`Main.main()`). It also handles system freezes (`Sys.halt()`) and execution delays (`Sys.wait()`).

### 2. `Memory.jack`
Manages the computer's RAM. It uses a **First-Fit Linked List** algorithm to manage heap allocations (`2048` to `16383`).
* `Memory.peek(address)`: Reads directly from a RAM address.
* `Memory.poke(address, value)`: Writes directly to a RAM address.
* `Memory.alloc(size)` & `Memory.dealloc(object)`: Handles dynamic memory management.

### 3. `Math.jack`
Provides basic mathematical functions that the Hack hardware cannot do by itself.
* Uses an array of powers-of-two for fast bitwise checking.
* Implements efficient binary shift-and-add for **multiplication**.
* Implements recursive long-division for **division**.
* Implements binary search for **square roots** ($\sqrt{x}$).

### 4. `Array.jack`
A very simple class that allows Jack programs to use dynamic arrays. It connects the `Array.new()` method directly to `Memory.alloc()`.

### 5. `String.jack`
Manages text strings. It handles dynamic memory allocations for characters and safely converts integers to text characters (ASCII values) and vice versa.

### 6. `Screen.jack`
Handles drawing graphics on the Hack physical screen (`16384` to `24575`).
* Draws single pixels by calculating exact memory bitmasks.
* Implements **Bresenham's Line Algorithm** to draw straight diagonal lines without slow floating-point math.
* Efficiently draws filled rectangles.

### 7. `Output.jack`
Handles printing text characters on the screen. It maps fixed 11x8 pixel matrix fonts for every readable character in the ASCII table and manages cursor row/column positions.

### 8. `Keyboard.jack`
Listens to the Hack keyboard memory-mapped register (`24576`). It allows the software to read individual pressed keys, read full text strings, and accept integer inputs from users.