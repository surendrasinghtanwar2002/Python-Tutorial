                                                        ## In this section we will create the thread for the class methods and static methods ##

##Import the moduels 
from threading import Thread,current_thread

##Creating the class 
class example:
    def __init__(self) -> None:
        pass
    
    @staticmethod                               ##static method
    def greet(seq:int):
        print(f"This is the child thread {current_thread()}")
        for items in range(seq):
            print(f"{items} {"Hello world"}")


##Creating the object or instance for the thread
t1 = Thread(target=example.greet,args=(10,))

##starting the thread
t1.start()

#printing the main thread 
print(f"This is my main or current thread {current_thread()}")

