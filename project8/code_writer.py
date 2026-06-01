class CodeWriter:
    def __init__(self, output_file):
        self.file = open(output_file, 'w')
        self.filename = ""
        self.label_counter = 0  # For generating unique jump labels (eq, gt, lt)
        self.call_counter = 0   # For generating unique return labels for function calls

    def set_file_name(self, filename):
        # Crucial for handling static variables uniquely per file
        self.filename = filename.split('/')[-1].replace('.vm', '')

    def write_init(self):
        """Writes the bootstrap code that initializes the VM."""
        # 1. SP = 256
        asm = ["@256", "D=A", "@SP", "M=D"]
        self.file.write("\n".join(asm) + "\n")
        # 2. Call Sys.init
        self.write_call("Sys.init", 0)