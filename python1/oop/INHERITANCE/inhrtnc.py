class Car:
    def defntn(self):
        print("abc")
class Mg(Car):
    def yr(self):
        print("2009")

class Hector(Mg):
    def model(self):
        print("2019")
ob=Hector()
ob.model()
ob.yr()
ob.defntn()