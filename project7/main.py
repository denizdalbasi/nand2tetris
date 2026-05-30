import os
import sys
from codeWritter import codeWritter 
from parse import Parser 

def translateFile(input_path, writer):
    parse = Parser(input_path)
    
    while parse.commend():
        parse.advance()
        commandtype = parse.commendType()
        
        if commandtype == "C_ARITHMETIC":
            writer.write_arithmetic(parse.arg1())
        elif commandtype in ("C_PUSH", "C_POP"):
            writer.write_push_pop(commandtype, parse.arg1(), parse.arg2())

def main():
    if len(sys.argv) != 2:
        print("Kullanım: python main.py <dosya_yolu.vm VEYA klasör_yolu>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    
    if os.path.isdir(input_path):
        folder_name = os.path.basename(os.path.normpath(input_path))
        output_path = os.path.join(input_path, folder_name + ".asm")
        
        vmfiles = sorted([
            os.path.join(input_path, f) 
            for f in os.listdir(input_path) if f.endswith(".vm")
        ])
        
        writer = codeWritter(output_path)
        
        if hasattr(writer, 'write_init'):
            writer.write_init()
            
        for vm_file in vmfiles:
            file_name = os.path.splitext(os.path.basename(vm_file))[0]
            writer.filename = file_name 
            
            translateFile(vm_file, writer)
            
        writer.close()
        print(f"Başarıyla tamamlandı! Çıktı dosyası: {output_path}")

    elif os.path.isfile(input_path) and input_path.endswith(".vm"):
        output_path = input_path.replace(".vm", ".asm")
        
        writer = codeWritter(output_path)
        translateFile(input_path, writer)
        writer.close()
        print(f"Başarıyla tamamlandı! Çıktı dosyası: {output_path}")
        
    else:
        print("Hata: Geçersiz dosya veya klasör yolu!")
        sys.exit(1)


if __name__ == "__main__":
    main()
