import  urllib.request,urllib.parse,urllib.error
link=input("entr link")
fhand=urllib.request.urlopen(link)
for line in fhand:
    print(line.decode().strip())
#line.decode