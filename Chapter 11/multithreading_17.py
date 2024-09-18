                        ##In this section we will practise on the native id of the thread##
from threading import Thread,get_native_id,current_thread,main_thread

##Creating the target function
def targ1():
    try:
        print(f"This is the current thread of target 1 function {current_thread()}")
        print(f"This is the main thread of target 1 function {main_thread()}")
        print(f"This is the native id of target 1 function {get_native_id()}")
        for items in range(80):
            print(f"Helo target 1 function")
    except Exception as e:
        print(f"This is the exception of the target 1 {e}")

def targ2():
    try:
        print(f"This is the current thread of target 2 function {current_thread()}")
        print(f"This is the main thread of target 2 function {main_thread()}")
        print(f"This is the native id of target 2 function {get_native_id()}")
        for items in range(80):
            print(f"Helo target 2 function")
    except Exception as e:
        print(f"This is the exception of the target 2 {e}")

def targ3():
    try:
        print(f"This is the current thread of target 3 function {current_thread()}")
        print(f"This is the main thread of target 3 function {main_thread()}")
        print(f"This is the native id of target 3 function {get_native_id()}")
        for items in range(80):
            print(f"Helo target 3 function")
    except Exception as e:
        print(f"This is the exception of the target 3 {e}")

def targ4():
    try:
        print(f"This is the current thread of target 4 function {current_thread()}")
        print(f"This is the main thread of target 4 function {main_thread()}")
        print(f"This is the native id of target 4 function {get_native_id()}")
        for items in range(80):
            print(f"Helo target 4 function")
    except Exception as e:
        print(f"This is the exception of the target 4 {e}")

#Creating thread of each target function
t1 = Thread(target=targ1)
t2 = Thread(target=targ2)
t3 = Thread(target=targ3)
t4 = Thread(target=targ4)

##starting all the thread
t1.start()
t2.start()
t3.start()
t4.start()