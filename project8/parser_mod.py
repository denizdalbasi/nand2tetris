class Parser:
    def __init__(self, filepath):
        self.commands = []
        self.current_command = None
        self.pointer = 0
        with open(filepath, 'r') as file:
            for line in file:
                clean_line = line.split('//')[0].strip()
                if clean_line:
                    self.commands.append(clean_line.split())

    def has_more_commands(self) -> bool:
        return self.pointer < len(self.commands)

    def advance(self):
        self.current_command = self.commands[self.pointer]
        self.pointer += 1

    def command_type(self) -> str:
        cmd = self.current_command[0]
        if cmd in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']: return "C_ARITHMETIC"
        if cmd == "push": return "C_PUSH"
        if cmd == "pop": return "C_POP"
        return "OTHER"

    def arg1(self):
        return self.current_command[0] if self.command_type() == "C_ARITHMETIC" else self.current_command[1]

    def arg2(self):
        return int(self.current_command[2])