from threading import *

rlock = RLock()

def func1():
    print("In func1, trying to acquire lock...")
    rlock.acquire()  
    print("Lock acquired in func1")
    func2()
    rlock.release()  
    print("Lock released in func1")

def func2():
    print("In func2, trying to acquire lock...")
    rlock.acquire()  
    print("Lock acquired in func2")
    rlock.release()  
    print("Lock released in func2")

t = Thread(target=func1)
t.start()
t.join()