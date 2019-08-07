a=0
b=1
n=int(input("enter the limit:"))
print(a)
print(b)
while(n-2):
    c=a+b
    a=b
    b=c
    print(c)
    n=n-1