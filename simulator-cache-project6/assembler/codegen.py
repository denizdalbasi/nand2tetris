class CodeGenerator:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        
        self.comp_table = {
            "0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100",
            "A": "0110000", "!D": "0001101", "!A": "0110001", "-D": "0001111",
            "-A": "0110011", "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
            "A-1": "0110010", "D+A": "0000010", "D-A": "0010011", "A-D": "0000111",
            "D&A": "0000000", "D|A": "0010101",
            "M": "1110000", "!M": "1110001", "-M": "1110011", "M+1": "1110111",
            "M-1": "1110010", "D+M": "1000010", "D-M": "1010011", "M-D": "1000111",
            "D&M": "1000000", "D|M": "1010101"
        }
        
        self.dest_table = {
            "": "000", "M": "001", "D": "010", "MD": "011",
            "A": "100", "AM": "101", "AD": "110", "AMD": "111"
        }
        
        self.jump_table = {
            "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
            "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
        }

    def translate_a_instruction(self, instruction):
        symbol = instruction[1:]
        if symbol.isdigit():
            val = int(symbol)
        else:
            if self.symbol_table.contains(symbol):
                val = self.symbol_table.get_address(symbol)
            else:
                val = self.symbol_table.add_entry(symbol)
        return format(val, '016b')

    def translate_c_instruction(self, parsed_c_dict):
        prefix = "111"
        comp_str = parsed_c_dict.get("comp", "0")
        a = "1" if "M" in comp_str else "0"
        comp_code = self.comp_table.get(comp_str, "0000000")
        dest_code = self.dest_table.get(parsed_c_dict.get("dest", ""), "000")
        jump_code = self.jump_table.get(parsed_c_dict.get("jump", ""), "000")
        return f"{prefix}{a}{comp_code}{dest_code}{jump_code}"

    def generate(self, parsed_instructions, debug_mode=False):
        binary_code = []
        for idx, inst in enumerate(parsed_instructions):
            if inst.startswith("@"):
                binary = self.translate_a_instruction(inst)
                if debug_mode:
                    print(f"[DEBUG] Line {idx+1}: A-Instruction [{inst}] -> {binary}")
            else:
                if isinstance(inst, dict):
                    binary = self.translate_c_instruction(inst)
                    if debug_mode:
                        print(f"[DEBUG] Line {idx+1}: C-Instruction {inst} -> {binary}")
                else:
                    raise ValueError(f"Invalid instruction format at line {idx+1}")
            binary_code.append(binary)
        return binary_code