import os
import sys
from parser_mod import Parser
from code_writer import CodeWriter

def main():
    if len(sys.argv) != 2:
        print("Usage: python vm_translator.py <path-to-file-or-dir>")
        return

    path = sys.argv[1].rstrip('/')
    vm_files = []

    # Determine if path is a single file or a directory
    if os.path.isdir(path):
        out_pathname = f"{path}/{os.path.basename(path)}.asm"
        for file in os.listdir(path):
            if file.endswith('.vm'):
                vm_files.append(os.path.join(path, file))
    else:
        out_pathname = path.replace('.vm', '.asm')
        vm_files.append(path)

    writer = CodeWriter(out_pathname)

    # For Project 8 directory tests (like FibonacciElement), bootstrap is required
    if os.path.isdir(path):
        writer.write_init()

    # Process all detected VM files
    for filepath in vm_files:
        writer.set_file_name(filepath)
        parser = Parser(filepath)

        while parser.has_more_commands():
            parser.advance()
            cmd_type = parser.command_type()

            if cmd_type == "C_ARITHMETIC":
                writer.write_arithmetic(parser.arg1())
            elif cmd_type in ["C_PUSH", "C_POP"]:
                writer.write_push_pop(cmd_type, parser.arg1(), parser.arg2())
            elif cmd_type == "C_LABEL":
                writer.write_label(parser.arg1())
            elif cmd_type == "C_GOTO":
                writer.write_goto(parser.arg1())
            elif cmd_type == "C_IF":
                writer.write_if(parser.arg1())
            elif cmd_type == "C_FUNCTION":
                writer.write_function(parser.arg1(), parser.arg2())
            elif cmd_type == "C_CALL":
                writer.write_call(parser.arg1(), parser.arg2())
            elif cmd_type == "C_RETURN":
                writer.write_return()

    writer.close()
    print(f"Translation successful! Output saved to {out_pathname}")

if __name__ == "__main__":
    main()