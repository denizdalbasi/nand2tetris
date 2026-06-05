class CodeWriter:
    def __init__(self, output_file):
        self.file = open(output_file, 'w')

    def write_arithmetic(self, command):
        if command == "add":
            self.file.write("@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nM=M+D\n@SP\nM=M+1\n")
        elif command == "sub":
            self.file.write("@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nM=M-D\n@SP\nM=M+1\n")

    def write_push_pop(self, command, segment, index):
        if command == "C_PUSH" and segment == "constant":
            self.file.write(f"@{index}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

    def close(self):
        self.file.close()