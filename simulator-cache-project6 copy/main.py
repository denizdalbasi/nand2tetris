import argparse
from assembler.symbol_table import SymbolTable

def main():
    parser = argparse.ArgumentParser(description="Custom Two-Pass Assembler")
    parser.add_argument("input_file", help="Path to the assembly source file")
    parser.add_argument("--debug", action="store_true", help="Enable detailed debug output")
    args = parser.parse_args()

    symbol_table = SymbolTable()

    if args.debug:
        print(f"[DEBUG] Processing file: {args.input_file}")
        print(f"[DEBUG] Initial symbol table loaded with {len(symbol_table.table)} entries.")

    with open(args.input_file, "r") as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("//"):
            cleaned_lines.append(line)

    if args.debug:
        print(f"[DEBUG] Found {len(cleaned_lines)} executable instructions.")

if __name__ == "__main__":
    main()