import sys
from parser_mod import Parser
from code_writer import CodeWriter

def main():
    if len(sys.argv) < 2:
        print("Usage: python vm_translator.py <file.vm>")
        return

    input_path = sys.argv[1]
    output_path = input_path.replace('.vm', '.asm')
    
    parser = Parser(input_path)
    writer = CodeWriter(output_path)

    while parser.has_more_commands():
        parser.advance()
        cmd_type = parser.command_type()
        
        if cmd_type == "C_ARITHMETIC":
            writer.write_arithmetic(parser.arg1())
        elif cmd_type in ["C_PUSH", "C_POP"]:
            writer.write_push_pop(cmd_type, parser.arg1(), parser.arg2())

    writer.close()
    print(f"Translation completed: {output_path}")

if __name__ == "__main__":
    main()