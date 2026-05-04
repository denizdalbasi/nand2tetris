// This file is part of Nand2Tetris Project 4 
// Listens to keyboard input. While a key is pressed, fills the screen black. 
// When no key is pressed, clears the screen. 
(LOOP)
    @KBD
    D=M
    @SET_BLACK
    D;JNE       // If KBD != 0, go to SET_BLACK
    
    @color
    M=0         // Color = White (0)
    @START_FILL
    0;JMP

(SET_BLACK)
    @color
    M=-1        // Color = Black (-1)

(START_FILL)
    @SCREEN
    D=A
    @addr
    M=D         // addr = 16384

(FILL_LOOP)
    @color
    D=M
    @addr
    A=M
    M=D         // Paint the 16 pixels the chosen color

    @addr
    M=M+1
    D=M
    @24576      // KBD address (SCREEN + 8192)
    D=D-A
    @FILL_LOOP
    D;JLT       // If addr < 24576, keep looping

    @LOOP
    0;JMP