#quantifiers....................................


import re
#x='a'
# x='a+'
# x='a*'  #any no of a including zero num of a
# x='a?' # individual positions
# x='a{2}' #check exactly 2
# x='a{2,5}' #min 2 max 5
# x='^a' #checks whthr startng wid a
x='a$' #ending with a






matcher=re.finditer(x,'abaabaaaba')
for match in matcher:
    print("position",match.start())
    print("group=",match.group())