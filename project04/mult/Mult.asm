// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

    @2
    M=0         // Initialize R2 = 0

    @0
    D=M
    @END
    D;JEQ       // If R0 == 0, jump to END (Result is already 0)

    @1
    D=M
    @END
    D;JEQ       // If R1 == 0, jump to END (Result is already 0)

(LOOP)
    @1
    D=M         // D = R1
    @2
    M=D+M       // R2 = R2 + R1

    @0
    MD=M-1      // R0 = R0 - 1, and also store result in D
    
    @LOOP
    D;JGT       // If R0 > 0, repeat the addition loop

(END)
    @END
    0;JMP       // Infinite loop to terminate the program