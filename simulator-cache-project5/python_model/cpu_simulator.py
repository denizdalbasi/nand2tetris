class PipelineCPUSimulator:
    def __init__(self, rom):
        self.rom = rom
        self.pc = 0
        
        # Pipeline Registers (Latches)
        self.if_id_instruction = 0
        self.if_id_pc = 0
        
        self.id_ex_pc = 0
        self.id_ex_instruction = 0
        self.id_ex_a_val = 0
        self.id_ex_d_val = 0
        
        self.ex_mem_alu_out = 0
        self.ex_mem_write_m = False
        self.ex_mem_address_m = 0
        
        # Architectural State
        self.a_register = 0
        self.d_register = 0
        self.memory = [0] * 32768
        
        self.stall = False
        self.flush = False

    def fetch(self):
        if not self.stall:
            if self.pc < len(self.rom):
                self.if_id_instruction = self.rom[self.pc]
                self.if_id_pc = self.pc
            else:
                self.if_id_instruction = 0
            self.pc += 1

    def decode(self):
        if self.flush:
            self.id_ex_instruction = 0
            self.id_ex_a_val = 0
            self.id_ex_d_val = 0
            return

        if not self.stall:
            instruction = self.if_id_instruction
            is_a_instruction = (instruction & 0x8000) == 0
            
            if is_a_instruction:
                self.id_ex_a_val = instruction
            else:
                self.id_ex_a_val = self.a_register
                
            self.id_ex_d_val = self.d_register
            self.id_ex_instruction = instruction
            self.id_ex_pc = self.if_id_pc

    def execute(self):
        instruction = self.id_ex_instruction
        is_c_instruction = (instruction & 0x8000) != 0
        
        if not is_c_instruction:
            alu_out = self.id_ex_a_val
            write_a = True
            write_d = False
            write_m = False
        else:
            a_bit = (instruction & 0x1000) != 0
            y_val = self.memory[self.id_ex_a_val] if a_bit else self.id_ex_a_val
            
            zx = (instruction & 0x0800) != 0
            nx = (instruction & 0x0400) != 0
            zy = (instruction & 0x0200) != 0
            ny = (instruction & 0x0100) != 0
            f  = (instruction & 0x0080) != 0
            no = (instruction & 0x0040) != 0
            
            x = self.id_ex_d_val
            y = y_val
            
            if zx: x = 0
            if nx: x = ~x & 0xFFFF
            if zy: y = 0
            if ny: y = ~y & 0xFFFF
            
            if f:
                alu_out = (x + y) & 0xFFFF
            else:
                alu_out = (x & y) & 0xFFFF
                
            if no: alu_out = ~alu_out & 0xFFFF
            
            dest = (instruction >> 3) & 0x0007
            write_m = (dest & 1) != 0
            write_d = (dest & 2) != 0
            write_a = (dest & 4) != 0
            
            jump = (instruction & 0x0007)
            zero = (alu_out == 0)
            neg = (alu_out & 0x8000) != 0
            
            jump_condition = False
            if jump == 1 and (not neg and not zero): jump_condition = True # JGT
            if jump == 2 and zero: jump_condition = True                    # JEQ
            if jump == 3 and (zero or not neg): jump_condition = True       # JGE
            if jump == 4 and neg: jump_condition = True                     # JLT
            if jump == 5 and not zero: jump_condition = True                # JNE
            if jump == 6 and (neg or zero): jump_condition = True           # JLE
            if jump == 7: jump_condition = True                             # JMP
            
            if jump_condition:
                self.pc = self.a_register
                self.flush = True

        if write_a:
            self.a_register = self.id_ex_a_val if not is_c_instruction else alu_out
        if write_d:
            self.d_register = alu_out
        if write_m:
            self.memory[self.a_register] = alu_out
            
        self.ex_mem_alu_out = alu_out
        self.ex_mem_write_m = write_m
        self.ex_mem_address_m = self.a_register

    def step(self):
        self.flush = False
        self.execute()
        self.decode()
        self.fetch()