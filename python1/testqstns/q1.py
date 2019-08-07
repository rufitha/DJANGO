class circle:
    def setval(self,r):


        self.r=r
    def area(self):

        print("area:",3.14*self.r*self.r)
    def perimeter(self):

        print("perimeter:",2*3.14*self.r)
ob=circle()
ob.setval(4)
ob.area()
ob.perimeter()