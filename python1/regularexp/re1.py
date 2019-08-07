import re
count=0
matcher=re.finditer('ab','abaababa')
for match in matcher:
    print("match availabls at",match.start())
    print("group=",match.group())
    count=count+1
print("count=",count)