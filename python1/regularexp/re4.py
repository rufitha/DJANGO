# #phn num validation
# starting with 6-9 n any digit
import re

x='[6-9]\d{9}' #\d=digit or [0-9]
n=input("entr phn num:")
matcher = re.fullmatch(x, n)

if (matcher == None):
    print("invalid")
else:
    print("valid")




