f=open("3.txt")
# print(f.mode)
#print(f.read())
for i in reversed(list(f)):
    print(i.rstrip())
