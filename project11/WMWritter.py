class WMWritter:
    def __init__(self,output_file):
        self.output=open(output_file,"w")

    def writePush(self,segment,index):
        seg="this" if segment=="FIELD" else segment.lower()
        seg ="local" if seg == "var" else seg
        seg ="argument" if seg == "arg" else seg
        self.output.write(f"push {seg} {index}\n")

    def writePop(self,segment,index):
        seg = "this" if segment == "FIELD" else segment.lower()
        seg = "local" if seg == "var" else seg
        seg = "argument" if seg == "arg" else seg
        self.output.write(f"pop {seg} {index}\n")


    def writeArithmethic(self,command):
        self.output.write(f"{command.lower()}\n")

    def writeLabel(self,label):
        self.output.write(f"label {label}\n")

    def writeGoto(self,label):
        self.output.write(f"goto {label}\n")

    def writeFunction(self,name,nLocals):
        self.output.write(f"function {name} {nLocals}\n")

    def writeCall(self, name,nArgs):
        self.output.write(f"call {name} {nArgs}\n")

    def writeIf(self, label):
        self.output.write(f"if-goto {label}\n")

    def close(self):
        self.output.close()

    def writeReturn(self):
        self.output.write("return\n")