                                                ##In this section we will practise multhreading  method main_thread() used to print inside the target function##
##importing the modules
from threading import Thread,main_thread,current_thread

##creating a target function 
def func1():
    print(f"This is your current thread function 1 {current_thread()}")
    print(f"This is your main thread {main_thread()}")
    try:
        for i in range(10):
            print("This is function 1")
    except Exception as e:
        print(f"This is the exception of e",e)

def func2():
    print(f"This is your current thread function 2 {current_thread()}")
    print(f"This is your main thread {main_thread()}")
    try:
        for i in range(10):
            print("This is function 2")
    except Exception as e:
        print(f"This is the exception of e",e)

def func3():
    print(f"This is your current thread of function 3 {current_thread()}")
    print(f"This is your main thread {main_thread()}")
    try:
        for i in range(10):
            print("This is function 3")
    except Exception as e:
        print(f"This is the exception of e",e)

##creating the thread object
t1 = Thread(target=func1)
t2 = Thread(target=func2)
t3 = Thread(target=func3)

##starting the all the sub threads 
t1.start()
t2.start()
t3.start()


##printing the main thread outside the function
print(f"This is your current thread {current_thread()}".center(120,"*"))