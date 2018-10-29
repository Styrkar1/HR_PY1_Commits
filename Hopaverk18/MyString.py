class MyString():
    def __init__(self,string):
        self.string = string

    def __gt__(self,other):
        if len(self.string) > len(other.string):
            return True
        elif len(self.string) < len(other.string):
            return False

    def __sub__(self,other):
        res = len(self.string) - len(other.string)
        return res

