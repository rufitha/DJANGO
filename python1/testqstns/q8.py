n=int(input("enter the num:"))
s=0
x=n
while(n>0):
    t=n%10
    s=s*10+t
    n=n//10
if(x==s):
    print("palindrome")
else:
    print("not palindrome")
