class codeWritter:
    def __init__(self, output_path):
        self.file = open(output_path, 'w')
        self.filename = output_path.split('/')[-1].replace('.asm','')

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
            if command == 'add':asm.append("M=D+M")
            elif command == 'sub':asm.append("M=M-D")
            elif command == 'and':asm.append("M=D&M")
            elif command == 'or':asm.append("M=D|M")
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
                "@SP", "A=M_1", "D=M-D",
                f"@{label_true}", f"D{jmp_type}",
                f"@{label_end}", "0;JMP",
                f"{label_true}",
                "@SP", "A=M-1","M=-1",
                f"({label_end})"
            ])

            self.file.write("\n".join(asm)+"\n")