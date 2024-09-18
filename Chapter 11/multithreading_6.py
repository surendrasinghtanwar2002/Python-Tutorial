                                    ## In this section we will create the thread for the methods which are presented in the class ##

#importing the modules
from threading import Thread,current_thread

##Creating a class 
class example:
    def __init__(self) -> None:         ##This is the constructor of the class
        pass

    def greet(self):
        try:
            for items in range(5):
                print(f"This is my child thread {current_thread()}")
                print("Hello world")
        except Exception as e:
            raise(e)


##Creating a object for the class 
e1 = example()

##Creating a object for the thread 
t1 = Thread(target=e1.greet)
t2 = Thread(target=e1.greet)
t3 = Thread(target=e1.greet)
t4 = Thread(target=e1.greet)
t5 = Thread(target=e1.greet)


##Starting all the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


##printing the main thread
print(f"This is my main thread {current_thread()}")
