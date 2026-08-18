@5
D=A        
M=D      

(LOOP)
@R1
D=M        
@END
D;JEQ      
@R1
D=M
@1
D=D-A     
@R1
M=D       

@LOOP
0;JMP    

(END)
@END
0;JMP      