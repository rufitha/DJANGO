from threading import *
import time


def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("dbl value=",2*n)


def sqaures(numbers):
    for n in numbers:
        time.sleep(1)
        print("sqr value=",n*n)
numbers=[1,2,3,4,5]
begintime=time.time()
t=Thread(target=doubles,args=(numbers,))
x=Thread(target=sqaures,args=(numbers,))
t.start()
x.start()
t.join()
x.join()
endtime=time.time()
print("toral time:",endtime-begintime)
