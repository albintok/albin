import threading
import time
def cals(num):
    for n in num:
        time.sleep(0.8)
        print("square:",n*n)
def calc(num):
    for n in num:
        time.sleep(0.8)
        print("cube:",n*n*n)
a=[1,2,3,4]
t1=threading.Thread(target=cals,args=(a,))
t2=threading.Thread(target=calc,args=(a,))
t1.start()
t2.start()