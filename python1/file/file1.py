f=open("num.txt")
print(f.mode)
#print(f.read())
for i in f:
    #print(f.readline())
    val=int(i)
    if (val%2==0):
        print(val)

