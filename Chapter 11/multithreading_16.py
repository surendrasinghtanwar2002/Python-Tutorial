                        ## In this section we will practise about the enumeate method to get the list of all running thread ##
from threading import Thread,current_thread,main_thread,enumerate

##Creating the target function for multiple thread 

def func1():
    try:
        print(f"Current thread of func1 {current_thread}")
        print(f"Native thread or main thread of the script {main_thread}")
        for items in range(80):
            print(f"{items} Hello function 1")
    except Exception as e:
        print(f"This is the exception of the e {e}")

def func2():
    try:
        print(f"Current thread of func2 {current_thread}")
        print(f"Native thread or main thread of the script {main_thread}")
        for items in range(80):
            print(f"{items} Hello function 2")
    except Exception as e:
        print(f"This is the exception of the e {e}")

def func3():
    try:
        print(f"Current thread of func3 {current_thread}")
        print(f"Native thread or main thread of the script {main_thread}")
        for items in range(80):
            print(f"{items} Hello function 3")
    except Exception as e:
        print(f"This is the exception of the e {e}")


def func4():
    try:
        print(f"Current thread of func4 {current_thread}")
        print(f"Native thread or main thread of the script {main_thread}")
        for items in range(80):
            print(f"{items} Hello function 4")
    except Exception as e:
        print(f"This is the exception of the e {e}")

##Creating the object of threads
t1 = Thread(target=func1)
t2 = Thread(target=func2)
t3 = Thread(target=func3)
t4 = Thread(target=func4)

##staring all the threadas 
t1.start()
t2.start()
t3.start()
t4.start()

#getting the list of the running threads
print(f"Details of the all running threads {enumerate()}")

##waiting for  the sub thread to be completed
t1.join()
t2.join()
t3.join()
t4.join()
