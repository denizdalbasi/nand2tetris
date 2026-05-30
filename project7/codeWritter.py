class codeWritter:
    def __init__(self, output_path):
        self.file = open(output_path, 'w')
        self.filename = output_path.split('/')[-1].replace('.asm','')
        self.label_counter = 0  # eq, gt, lt için sayaç ekledim

        self.segments = {
            "local": "LCL",
            "argument": "ARG",
            "this":"THIS",
            "that":"THAT"
        }

    def write_arithmetic(self, command):
        asm = []
        asm.append(f"//{command}")

        if command in ['add','sub','and','or']:
            asm.extend([
                "@SP", "AM=M-1","D=M",
                "@SP", "A=M-1"
            ])
            if command == 'add': asm.append("M=D+M")
            elif command == 'sub': asm.append("M=M-D")
            elif command == 'and': asm.append("M=D&M")
            elif command == 'or': asm.append("M=D|M")
            
        elif command in ["neg", "not"]:
            asm.extend([ "@SP", "A=M-1"])
            if command == 'neg': asm.append("M=-M")
            if command == 'not': asm.append("M=!M")

        elif command in ['eq','gt','lt']:
            label_true = f"LABEL_TRUE_{self.label_counter}"
            label_end = f"LABEL_END_{self.label_counter}"
            self.label_counter += 1

            jmp_type = {"eq":"JEQ","gt":"JGT","lt":"JLT"}[command]
            
            asm.extend([
                "@SP","AM=M-1","D=M",
                "@SP", "A=M-1", "D=M-D",        # A=M_1 yerine A=M-1 yaptim
                f"@{label_true}", f"D;{jmp_type}", # Araya semikolon (;) eklendi
                "@SP", "A=M-1", "M=0",          # Koşulun yanlış (FALSE) olma durumu ekledim
                f"@{label_end}", "0;JMP",       #Yanlışsa TRUE bloğuna girmeden sona atlasın
                f"({label_true})",              #  Etiket tanımına parantez ekledim
                "@SP", "A=M-1","M=-1",
                f"({label_end})"
            ])

        self.file.write("\n".join(asm)+"\n")
        
    def write_push_pop(self, command_type, segment, index):
        pass

