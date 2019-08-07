def lcm(a,b):
    if a>b:
        l=a
    else:
        l=b
    while(True):
        if(l % a == 0) & (l % b == 0):
            lcm=l
            break
        l=l+1
    return lcm





a=int(input("enter the first num:"))
b=int(input("enter the second num:"))
print("lcm of two num is:")
print(lcm(a,b))

