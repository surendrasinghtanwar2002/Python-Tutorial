                                            ## In this section we will create mulithread and find their process id as well as their thread name and compare with main Thread ##
##Import the module
from threading import Thread,current_thread

#Create the thread target function (1)
def target_function_1(msg=None,seq=None):
    print(f"This is your First thread {current_thread()}")
    for items in range(seq):
        print(f"({items}) {msg}")

#Create the thread target function (2)
def target_function_2(msg=None,seq=None):
    print(f"This is your Second Thread {current_thread()}")
    for items in range(seq):
        print(f"({items}) {msg}")

##Create the thread target function (3)
def target_function_3(msg=None,seq=None):
    print(f"This is your Third Thread {current_thread()}")
    for items in range(seq):
        print(f"({items}) {msg}")


#Create a thread object for each target function
t1 = Thread(target=target_function_1,kwargs={'msg':"Hello world",'seq':5})
t2 = Thread(target=target_function_2,kwargs={'msg':"My name is Surendra",'seq':4})
t3 = Thread(target=target_function_3,kwargs={'msg':"My college name is Poornima Univeristy",'seq':6})

##starting all the thread 
t1.start()
t2.start()
t3.start()

##Printing the parent or main thread
print(f"This is the Main Thread / Parent Thread:-{current_thread()}")


