class HazardDetector:

    def __init__(self):
        self.stall = False
        self.flush = False

    def check_hazards(self, fetch_inst, decode_inst, execute_inst):
        self.stall = False
        self.flush = False

        forward_a = "NONE"
        forward_d = "NONE"

        if self._is_c_instruction(execute_inst):
            jump_bits = execute_inst & 0x0007
            if jump_bits != 0:
                self.flush = True

        if self._is_c_instruction(decode_inst):
            dest_ex = (execute_inst >> 3) & 0x07 if self._is_c_instruction(execute_inst) else (1 if not self._is_a_instruction(execute_inst) else 0)
            
            ex_writes_d = bool(dest_ex & 2)
            ex_writes_a = bool(dest_ex & 4) or self._is_a_instruction(execute_inst)

            uses_a_reg = True
            uses_d_reg = True

            if ex_writes_d and uses_d_reg:
                forward_d = "FROM_EX"

            if ex_writes_a and uses_a_reg:
                forward_a = "FROM_EX"

        return {
            "stall": self.stall,
            "flush": self.flush,
            "forward_a": forward_a,
            "forward_d": forward_d
        }

    @staticmethod
    def _is_a_instruction(instruction):
        return (instruction & 0x8000) == 0

    @staticmethod
    def _is_c_instruction(instruction):
        return (instruction & 0x8000) != 0


if __name__ == "__main__":
    detector = HazardDetector()

    inst_ex = 0xEC10
    inst_dec = 0x1F410
    inst_fet = 0x0001

    signals = detector.check_hazards(inst_fet, inst_dec, inst_ex)

    inst_jmp = 0xEA07
    signals_jump = detector.check_hazards(0x0002, 0x0001, inst_jmp)