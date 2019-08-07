stack=[]
top= -1
size=int(input("enter the size:"))


def push(element):
    global top
    if((top+1)>size):
        print(size)
        print("stack is full")

    else:
        top+=1
        stack.insert(top,element)
        print("Element inserted")


def pop():
    global top
    if(top<0):
        print("stack empty")
    else:
        element=stack[top]
        top-=1
        print(element,"removed")

def display():
    for i in range(0,top+1):
        print(stack[i])



ch=0
while(ch!=4):
    ch = int(input("enter the choice:"))
    if(ch==1):
        element = int(input("enetr elemnt:"))
        push(element)
    elif(ch==2):
        pop()
    elif(ch==3):
        display()
    elif(ch==4):
        exit()















