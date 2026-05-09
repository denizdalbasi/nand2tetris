#!/usr/bin/env python3
"""
Hack Assembler – Chapter 6 (Nand2Tetris)
Translates .asm file to .hack binary.
Usage: python Assembler.py Prog.asm
"""

import sys

class Parser:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        # Temizle: yorumlar ve boşlukları sil
        self.commands = []
        for line in lines:
            line = line.split('//')[0].strip()
            if line:
                self.commands.append(line)
        self.idx = -1
        self.current = None

    def hasMoreCommands(self):
        return self.idx + 1 < len(self.commands)

    def advance(self):
        if self.hasMoreCommands():
            self.idx += 1
            self.current = self.commands[self.idx]

    def commandType(self):
        # A_COMMAND: @Xxx
        if self.current.startswith('@'):
            return 'A_COMMAND'
        # L_COMMAND: (Xxx)
        if self.current.startswith('(') and self.current.endswith(')'):
            return 'L_COMMAND'
        # else C_COMMAND
        return 'C_COMMAND'

    def symbol(self):
        # @Xxx veya (Xxx) içindeki Xxx
        if self.commandType() == 'A_COMMAND':
            return self.current[1:]
        elif self.commandType() == 'L_COMMAND':
            return self.current[1:-1]
        return None

    def dest(self):
        # C komutunda '=' işaretinden önceki kısım
        if '=' in self.current:
            return self.current.split('=')[0]
        return 'null'

    def comp(self):
        # C komutunda '=' sonrası ve ';' öncesi
        comp_part = self.current
        if '=' in comp_part:
            comp_part = comp_part.split('=')[1]
        if ';' in comp_part:
            comp_part = comp_part.split(';')[0]
        return comp_part

    def jump(self):
        # C komutunda ';' sonrası
        if ';' in self.current:
            return self.current.split(';')[1]
        return 'null'


class Code:
    @staticmethod
    def dest(mnemonic):
        table = {
            'null': '000', 'M': '001', 'D': '010', 'MD': '011',
            'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'
        }
        return table.get(mnemonic, '000')

    @staticmethod
    def comp(mnemonic):
        table = {
            '0':   '0101010', '1':   '0111111', '-1':  '0111010',
            'D':   '0001100', 'A':   '0110000', 'M':   '1110000',
            '!D':  '0001101', '!A':  '0110001', '!M':  '1110001',
            '-D':  '0001111', '-A':  '0110011', '-M':  '1110011',
            'D+1': '0011111', 'A+1': '0110111', 'M+1': '1110111',
            'D-1': '0001110', 'A-1': '0110010', 'M-1': '1110010',
            'D+A': '0000010', 'D+M': '1000010',
            'D-A': '0010011', 'D-M': '1010011',
            'A-D': '0000111', 'M-D': '1000111',
            'D&A': '0000000', 'D&M': '1000000',
            'D|A': '0010101', 'D|M': '1010101'
        }
        return table.get(mnemonic, '0000000')

    @staticmethod
    def jump(mnemonic):
        table = {
            'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
            'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'
        }
        return table.get(mnemonic, '000')


class SymbolTable:
    def __init__(self):
        self.table = {
            'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
            'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4,
            'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9,
            'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
            'SCREEN': 16384, 'KBD': 24576
        }
        self.next_var_addr = 16

    def addEntry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol):
        return symbol in self.table

    def getAddress(self, symbol):
        return self.table[symbol]

    def addVariable(self, symbol):
        addr = self.next_var_addr
        self.addEntry(symbol, addr)
        self.next_var_addr += 1
        return addr


def assemble(in_filename):
    out_filename = in_filename.replace('.asm', '.hack')
    symbol_table = SymbolTable()

    # First pass: collect labels (L_COMMAND)
    parser = Parser(in_filename)
    rom_address = 0
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == 'L_COMMAND':
            label = parser.symbol()
            if not symbol_table.contains(label):
                symbol_table.addEntry(label, rom_address)
        elif parser.commandType() in ('A_COMMAND', 'C_COMMAND'):
            rom_address += 1

    # Second pass: translate
    parser = Parser(in_filename)
    with open(out_filename, 'w') as out:
        while parser.hasMoreCommands():
            parser.advance()
            typ = parser.commandType()
            if typ == 'A_COMMAND':
                sym = parser.symbol()
                # sayı mı sembol mü?
                if sym.isdigit():
                    addr = int(sym)
                else:
                    if symbol_table.contains(sym):
                        addr = symbol_table.getAddress(sym)
                    else:
                        addr = symbol_table.addVariable(sym)
                bin_str = f"{addr:015b}"  # 15 bit
                out.write('0' + bin_str + '\n')
            elif typ == 'C_COMMAND':
                dest = Code.dest(parser.dest())
                comp = Code.comp(parser.comp())
                jump = Code.jump(parser.jump())
                out.write('111' + comp + dest + jump + '\n')
            # L_COMMAND ignore in second pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python Assembler.py Prog.asm")
        sys.exit(1)
    assemble(sys.argv[1])
