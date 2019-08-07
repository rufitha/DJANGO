import re
f1=open("phn.txt",)
lst=[]
for i in f1:
    lst.append(i.rstrip("\n"))
#print(lst)
f2=open("valid.txt",'w')
for val in lst:
    x='[6-9]\d{9}' #\d=digit or [0-9]

    matcher = re.fullmatch(x,val)
    if(matcher==None):
        print("inavlid")
    else:
        f2.write(val+"\n")




