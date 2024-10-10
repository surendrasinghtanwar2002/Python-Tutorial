                            ## In this section we will change the thread name with the new name ##
from threading import Thread,current_thread
import os

#Create the target function to create the task
def my_func_1():
    try:
        print("Hello world My name is Surendra Singh Tanwar This is my function 1")
    except Exception as e:
        print("This is the exception of the function",e)

def my_func_2():
    try:
        print("Hello world My name is Surendra Singh Tanwar This is my function 2")
    except Exception as e:
        print(f"This is the exception of the function {e}")


##Creating the object or instance of the threads
t1 = Thread(target=my_func_1)
t2 = Thread(target=my_func_2)

##starting the threads
t1.start()
t2.start()

##Getting the native identifier and thread identifier
print(f"This is Thread Identifier {t1.ident}")
print(f"This is the Native Identifier {t1.native_id}")


##Changing the thread name here
t1.name= "My Custom Thread Name 1 "
t2.name = "My Custom Thread Name 2"

##After changing thread name printing the current thread name
print(t1.name)
print(t2.name)


##Get the main thread details
print(f"Original Main Thread Name {current_thread()}")

##Changin the main thread name
current_thread().name="Current Thread Name have been changed"

print(f"After Chaning the  Main Thread Name {current_thread()}")



##Getting the this program current process id
print(f"this is operating system allocated Process Id:- {os.getpid()}")


