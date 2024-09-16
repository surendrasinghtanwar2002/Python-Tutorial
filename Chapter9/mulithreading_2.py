                                                                            ## In this section we will pass the kwargs in the multhithreading ##
##First import the modules
from threading import Thread

#Second create the function to be performed on seperate thread
def greeting(seq,msg):
    try:
       for items in range(seq):
           print(msg)
    except Exception as e:
        print(f"This the exception as",e)

##Creating a thread object and passing the arguments
thread1 = Thread(target=greeting,kwargs={"seq":5,"msg":"hello world"})

##starting the thread
thread1.start()

##Creating another task which will run in the main thread
for items in range(6):
    print("Welcome to the programming language")

