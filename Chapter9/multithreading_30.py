                        ## In this section we will practise the thread communication using event method ##

import threading
import random
from time import sleep

##create the event object
event = threading.Event()

##First target function
def task_creator():
    try:
        print("Your task have been started")
        sleep(random.randint(5,6))                ##task should be completed in 5 second
        print("Your task have been completed")
        event.set()
    except Exception as e:
        print(f"This is the exception of the function {e}")

##Second Target function
def notification():
    try:
        event.wait()            ##using the wait method to complete the task first then start the task 2
        if event.is_set():
            sleep(1)
            print(" Hey Hey Hey Your task have been completed succesfully ".center(120,"*"))
    except Exception as e:
        print(f"This is the exception of the function {e}")


##Creating the thread
t1 = threading.Thread(target=task_creator)
t2 = threading.Thread(target=notification)

##Starting the thread
t1.start()
t2.start()

##waiting for the threads to be completed
t1.join()
t2.join()