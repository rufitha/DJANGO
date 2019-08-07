import re
x ='^KL[ -][0-9]{1,2}[ -][A-Z]{2}[ -][0-9]{4}$'
n=input("entr id:")
matcher=re.fullmatch(x,n)

if(matcher==None):
    print("invalid")
else:
    print("valid")