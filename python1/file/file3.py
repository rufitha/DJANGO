f1=open("name.txt",'r')
lst=[]
for i in f1:
    lst.append(i.rstrip("\n"))
print(lst)




f2=open("phone.txt",'r')
l=[]
for i in f2:
    l.append(i.rstrip("\n"))
print(l)
f3=open("out.txt",'w')         
for val in lst:

    for v in l:
        f3.write(val+" "+v+"\n")
        break