class Parser:
    def __init__(self, filepath):
        self.commands = []
        self.current_command = None
        self.pointer = 0
        
        # Read file and clean up lines
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
        arithmetic = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        
        if cmd in arithmetic: return "C_ARITHMETIC"
        elif cmd == "push":    return "C_PUSH"
        elif cmd == "pop":     return "C_POP"
        elif cmd == "label":   return "C_LABEL"
        elif cmd == "goto":    return "C_GOTO"
        elif cmd == "if-goto": return "C_IF"
        elif cmd == "function":return "C_FUNCTION"
        elif cmd == "return":  return "C_RETURN"
        elif cmd == "call":    return "C_CALL"

    def arg1(self) -> str:
        if self.command_type() == "C_ARITHMETIC":
            return self.current_command[0]
        return self.current_command[1]

    def arg2(self) -> int:
        return int(self.current_command[2])