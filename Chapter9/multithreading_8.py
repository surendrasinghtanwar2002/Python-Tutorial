                                                ## In this section we will create the thread for class  method ##

##Import the modules
from threading import Thread,current_thread


##Creating the class 
class Example:    
    @classmethod
    def greet(cls,seq):
        print(f"This is your child thread {current_thread()}")
        for items in range(seq):
            print(f"({items}) {"Hello world"}")


##Creating a thread object
t1 = Thread(target=Example.greet, args=(5,))

##Starting the child thread
t1.start()

##printing the main thread 
print(f"This is your main thread {current_thread()}")

