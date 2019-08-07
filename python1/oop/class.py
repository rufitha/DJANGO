class Student:
    def setdetails(self,rolno,name):
        self.rolno=rolno
        self.name=name
    def disp(self):
        print(self.name)
        print(self.rolno)
class Bank:
    def depo(self,accno,amount):
        self.accno=accno
        self.amount=amount
    def withdrwl(self,accno,amount):
        self.accno = accno
        self.amount = amount

    def disply(self):
        print(self.accno)
        print(self.amount)
ob=Student()
ob.setdetails(1,'rufi')
ob.disp()

ob2=Bank()
ob2.depo(1,100)
ob2.withdrwl(1,100)
ob2.disply()