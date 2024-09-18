                                                    ## In this section we will practise multhreading  method is_alive()##
#(1)is_alive()
#(2)main_thread()
#(3)active_count()
#(4)enumerate()
#(5)get_native_id()

##Importing the modules
from threading import Thread,current_thread

##creating the target function for each thread
def func1():
    for items in range(41):
        print("I am function 1")

def func2():
    for items in range(41):
        print("I am function 2")

def func3():
    for items in range(41):
        print("I am function 3")


##creating thread object for each target function
t1 = Thread(target=func1)
t2 = Thread(target=func2)
t3 = Thread(target=func3)

##validating the threads current status
print(f"Before t1 status {t1.is_alive()}")
print(f"Before t2 status {t2.is_alive()}")
print(f"Before t3 status {t3.is_alive()}")

##starting all the threads
t1.start()
t2.start()
t3.start()

##valind the thread after the start of the threads
print(f"current t1 status {t1.is_alive()}")
print(f"current t2 status {t2.is_alive()}")
print(f"current t3 status {t3.is_alive()}")

##passing the join method to put the main function to the wait statement until and unless the child threads completes their process
t1.join()
t2.join()
t3.join()

##after completing all the thread process now checking the current thread status
print(f"After completion t1 status {t1.is_alive()}")
print(f"After completion t2 status {t2.is_alive()}")
print(f"After completion t3 status {t3.is_alive()}")



