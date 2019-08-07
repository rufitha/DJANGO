def rfibo(n):
    if n <= 1:
        return n
    else:
        return (rfibo(n - 1) + rfibo(n - 2))



a = int(input("enter the limit: "))


print("Fibonacci sequence:")
for i in range(a):
    print(rfibo(i))