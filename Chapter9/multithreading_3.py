                                ## In this section we will print the current thread and thread which is created for the target function name and process id ##
from threading import Thread,current_thread

#Creating a target function
def greet(msg=None,seq=None):
    print(f"This is your new or child thread:- {current_thread().ident}")               #Identifier is used to find the process id
    for items in range(seq):
        print(msg)

#Create a thread object here
thread2 = Thread(target=greet,args=("hello world",5))

#start the thread 
thread2.start()

mainthread = current_thread().ident
print(f"This is your Main Thread {mainthread}")


    
    