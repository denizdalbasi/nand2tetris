class SymbolTable:
    def __init__(self):
        self.class_table={}
        self.subroutine_table = {}
        self.counts = {"STATIC":0,"FIELD":0, "VAR":0,"ARG":0}

    def start_subroutine(self):
        self.subroutine_table.clear()
        self.counts["ARG"]=0
        self.counts["VAR"]=0

    def define(self,name,type_str,kind):
        index=self.counts[kind]
        if kind in  ["STATIC", "FIELD"]:
            self.class_table[name]= (type_str, kind, index)
        else:
            self.subroutine_table[name]= (type_str, kind, index)
        self.counts[kind] += 1

    def varCount(self,kind):
        return self.counts[kind]

    def __lkUp(self,name):
        if name in self.subroutine_table:
            return self.subroutine_table[name]
        elif name in self.class_table:
            return self.class_table[name]
        else:
            return None
        
    def kindOf(self ,name):
        res = self.__lkUp(name)
        return res[1] if res else None
    
    def indexOf(self,name):
        res =self.__lkUp(name)
        return res[2] if res else None