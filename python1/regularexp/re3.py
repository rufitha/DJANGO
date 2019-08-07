# q) 1st char starts with a-k n 2nd must be adigit div by 3 and cont without any limit

import re
x='[a-k][3 6 9][a-z A-Z 0-9#]*'
n=input("entr the string:")
matcher=re.fullmatch(x,n)

if(matcher==None):
    print("invalid")
else:
    print("valid")






