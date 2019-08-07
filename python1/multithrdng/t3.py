from threading import *

class Mythread(Thread):  #inheritnce ppy used
    def run(self):
        for i in range(3):
            print(("inside mythread run method"))
t=Mythread() #objct creatd
t.start()
for i in range(3):
    print("inside main thread")