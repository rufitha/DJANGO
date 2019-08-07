

class Employee:
    def __init__(self,id,name,sal,dep):
        self.id=id
        self.name=name
        self.sal=sal
        self.dep=dep
    def __str__(self):
        return self.name+" "+str(self.sal)+" "+self.dep

f1=open("emply.txt",'r')
lst=[]
for i in f1:create
    l=(i[:-1].split(","))
    # s=i.rstrip("\n")
    lst.append(Employee(l[0],l[1],l[2],l[3]))

x = sorted(lst,key=lambda emp:emp.sal,reverse=True)
for emp in x:
    print(emp)

print()

s=list(filter(lambda em:int(em.sal)>19000,lst))
for em in s:
    print(em)






# x=[(num,name,sal,pos) for (num,name,sal,pos) in lst if sal>=19000]
# print(x)
