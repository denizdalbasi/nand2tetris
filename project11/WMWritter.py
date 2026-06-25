class VMWriter:
    def __init__(self, output_file):
        self.output = open(output_file, "w")

    def writePush(self, segment, index):
        seg = self._map_segment(segment)
        self.output.write(f"push {seg} {index}\n")

    def writePop(self, segment, index):
        seg = self._map_segment(segment)
        self.output.write(f"pop {seg} {index}\n")

    def writeArithmetic(self, command):
        self.output.write(f"{command.lower()}\n")

    def writeLabel(self, label):
        self.output.write(f"label {label}\n")

    def writeGoto(self, label):
        self.output.write(f"goto {label}\n")

    def writeIf(self, label):
        self.output.write(f"if-goto {label}\n")

    def writeFunction(self, name, nLocals):
        self.output.write(f"function {name} {nLocals}\n")

    def writeCall(self, name, nArgs):
        self.output.write(f"call {name} {nArgs}\n")

    def writeReturn(self):
        self.output.write("return\n")

    def close(self):
        self.output.close()

    def _map_segment(self, segment):
        mapping = {
            "CONST": "constant",
            "ARG": "argument",
            "LOCAL": "local",
            "VAR": "local",
            "FIELD": "this",
            "STATIC": "static",
            "THIS": "this",
            "THAT": "that",
            "POINTER": "pointer",
            "TEMP": "temp"
        }
        return mapping.get(segment.upper(), segment.lower())