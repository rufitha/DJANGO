#mail id validation

import re
x ='\w[a-zA-Z0-9]*@[a-zA-Z]*[.]com'
n=input("entr id:")
matcher=re.fullmatch(x,n)

if(matcher==None):
    print("invalid")
else:
    print("valid")


