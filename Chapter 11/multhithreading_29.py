                            ## In this section we will create the custom thread exception handling  from the excepthook method ##

import threading

##Creating the custom exception handling module
def customexcepthandler(args):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

##Creating two target function
def target_1_function():
    try:
        for i in range(10):
            print("Hello world"+i)                  ##situation where exception will occur
    except Exception as e:
        print(f"This is the exception of the function {e}")

def target_2_function():
    try:
        for i in range(10):
            print("My name is Surendra")                  ##situation where exception will occur
    except Exception as e:
        print(f"This is the exception of the function {e}")

##Passing custom exception handling function to the threading module
threading.excepthook= customexcepthandler

#Creating the threads for each target function
t1 = threading.Thread(target=target_1_function,name="Child_Thread_1")
t2 = threading.Thread(target=target_2_function,name="Child_Thread_2")

##starting the thread
t1.start()
t2.start()