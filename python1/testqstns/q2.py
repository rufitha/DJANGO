class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)
    def sub(self):
        return(self.a-self.b)
    def mul(self):
        return(self.a*self.b)
    def div(self):
        return(self.a /self.b)
    def disp(self):
        print("add: ", obj.add())
        print("sub: ", obj.sub())
        print("mul: ", obj.mul())
        print("div: ", obj.div())
a=int(input("enter the number:"))
b=int(input("enetr the 2nd num:"))
obj=calculator(a,b)
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.disp()