n=int(input("enter the num:"))
if n>1:
    for i in range(2,n):
        if (n%i==0):
            print(" not prime")
    else:
        print(" prime")
else:
    print("not prime")