from threading import *
import time

class test:
    def m1(self):
        time.sleep(2)
        for i in range(3):
            print("inside test")
ob=test()
t=Thread(target=ob.m1)
t.start()

for i in range(3):
    print("inside main thread")