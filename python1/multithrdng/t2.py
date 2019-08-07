# from threading import  *
# def display():
#     for i in range(10):
#         print("child thread executing")
#     print(current_thread().getName())
# for i in range(1,10):
#     print("main thread executing")
# print(current_thread().getName())
#
# display()
#===================================creating thread

from threading import  *
def display():
    for i in range(10):
        print("child thread executing")
    print(current_thread().getName())
t=Thread(target=display)
t.start()
for i in range(1,10):
    print("main thread executing")
print(current_thread().getName())

display()