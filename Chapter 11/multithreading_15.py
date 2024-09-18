                                  ##In this section we will practise multhreading  method main_thread() & active count() used to print inside the target function##
from threading import Thread,current_thread,main_thread,active_count
##creating target function
def func1():
    try:
        print(f"This is the current thread of function 1 {current_thread()}")
        print(f"This is the main thread {main_thread()}")
        for items  in range(80):
            print(f"({items}) {"Hello  function 1"}")

    except Exception as e:
        print(f"This is the exception of the function {e}")

def func2():
    try:
        print(f"This is the current thread of function 2 {current_thread()}")
        print(f"This is the main thread {main_thread()}")
        for items  in range(80):
            print(f"({items}) {"Hello  function 2"}")
    except Exception as e:
        print(f"This is the exception of the function {e}")

def func3():
    try:
        print(f"This is the cuurent thread of the function 3 {current_thread()}")
        print(f"This is the main thread {main_thread()}")
        for items  in range(80):
            print(f"({items}) {"Hello  function 3"}")
    except Exception as e:
        print(f"This the exception of the function {e}")


##creating the threads object for the each target function
t1 = Thread(target=func1)
t2 = Thread(target=func2)
t3 = Thread(target=func3)

##Printing the current status of the thread before starting the thread
print(f"Before starting the thread t1:-{t1.is_alive()}")
print(f"Before starting the thread t2:-{t2.is_alive()}")
print(f"Before starting the thread t3:-{t3.is_alive()}")

##starting all the threads 
t1.start()
t2.start()
t3.start()

##Priting the stauts of the thread after starting the thread
print(f"After starting the thread t1:- {t1.is_alive()}")
print(f"After starting the thread t2:- {t2.is_alive()}")
print(f"After starting the thread t3:- {t3.is_alive()}")

##printing the active count number of running thread
print(f"*--------*-*-*-*-*-*-*-*-*-*--*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- {active_count()} <*-*-*-**-*-*-***-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*")

##waiting for the sub thread to complete and execute the main thread 
t1.join()
t2.join()
t3.join()



