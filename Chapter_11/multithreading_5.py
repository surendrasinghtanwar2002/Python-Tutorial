                                        ## In this section we will create the thread for the methods which are presented in the class ##

##import the module
from threading import Thread,current_thread

##Create the Class and their methods
class Example:
    def __init__(self) -> None:             ##Creating the instance constructor
        pass

    def display_menu(self):
        print(f"This is our child thread derieved from the parent thread {current_thread()}")
        for items in range(5):
            print(f"({items}) {"Hello world"}")
    

##Now creating a thread for the class instance we need to create the object of the class first
e1 = Example()        

#Creating the thread object here
t1 = Thread(target=e1.display_menu)

##Starting the child thread 
t1.start()


print(f"This is my main thread {current_thread()}")


