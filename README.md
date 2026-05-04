# Nand2Tetris: Logic Gate Implementation  
**Building the Foundation of a 16-bit Computer**

This repository covers the projects of the Nand2Tetris curriculum. The goal is to be able to build a computer from scratch, starting with a single NAND gate and using it to build all fundamental logic components.

## Progress: Project 1 Complete  
I have implemented the basic set of logic gates using a Hardware Description Language (HDL), including:

- **Elementary gates:** `Not`, `And`, `Or`, `Xor`, `Mux`, `Demux`  
- **16-bit variants:** `Not16`, `And16`, `Or16`, `Mux16`  
- **Multi-way components:** `Or8Way`, `Mux4Way16`, `Mux8Way16`, `DMux4Way`, `DMux8Way`

## Progress: Project 2 Complete  
Implemented the core arithmetic components of the CPU.

- **Adders:** `HalfAdder`, `FullAdder`, `Add16`, `Inc16`  
- **Arithmetic Logic Unit (ALU):** A central component designed to execute 18 different functions based on six control inputs ($zx, nx, zy, ny, f, no$). 

## Progress: Project 3 Complete  
Added memory and stateful components to the system.

- **Registers:** `Bit` (1-bit storage) and `Register` (16-bit word storage).  
- **RAM Units:** `RAM8`, `RAM64`, `RAM512`, `RAM4K`, and `RAM16K` modules.
- **Program Counter (PC):** A specialized 16-bit register with increment, load, and reset functionality.

## Progress: Project 4 Complete
I implemented low-level programs using the Hack Assembly Language to understand how the CPU interacts with RAM and I/O devices.

- **Mult.asm:** An implementation of a multiplication algorithm using repetitive addition. Since the Hack ALU does not have a hardware-based multiplier, this program demonstrates how complex arithmetic is handled at the software level.

- ** Fill.asm:** An interactive program that handles I/O device mapping. It continuously polls the keyboard register and manipulates the screen's memory map to toggle pixels between black and white.

## Progress: Project 5 (In Progress)

## Progress: Project 6 (In Progress)
