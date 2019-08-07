list=[1,2,2,3,'a','a']
# a=input("enter the values:")
# list.append(a)

x=[]
for i in list:
    # for i not in x:
    if not i in x:
        x.append(i)

print("non duplicate values:")
print(x)


