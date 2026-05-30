
class Parser:
    def __init__(self, file_path):
        with open(file_path, "r") as f:
            #self.lies yerine self.lines, .sprit() -> .strip() oldu
            self.lines = [
                line.split('//')[0].strip()
                for line in f.readlines()
                if line.split('//')[0].strip()
            ]
        self.current_index = -1
        self.current_comment = ""

    def commend(self):
        # self.lines olarak güncellendi
        return (self.current_index + 1) < len(self.lines)
    
    def advance(self):
        #  = -1 yerine += 1 yapıldı ki her seferinde sonraki satıra geçebilsin
        self.current_index += 1
        self.current_comment = self.lines[self.current_index]

    def commendType(self):
        aritmethicCommend = {'add','sub','neg','eq','gt','lt','and','or','not'} #git eksikti eklendi
        firstWord = self.current_comment.split()[0]
        if firstWord in aritmethicCommend:
            return "C_ARITHMETIC"
        elif firstWord == "push":
            return "C_PUSH"
        elif firstWord == "pop":
            return "C_POP"
        return "UNKNOWN"
    
    def arg1(self):
        words = self.current_comment.split()
        if self.commendType() == "C_ARITHMETIC":
            return words[0]
        return words[1]

    def arg2(self):
        words = self.current_comment.split()
        return int(words[2])