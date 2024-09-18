                                        ## In this section we will practise the thread communication using event method ##

import threading
from time import sleep
import random

##Creating the event object
event = threading.Event()

##Two function or trigger function
def migration_function():
    try:
        print(f" Your thread details:- {threading.current_thread().name} ".center(120,"*"))
        print("Wait we are migrating your database from the Mumbai Region to Delhi Region")
        sleep(random.randint(6,7))
        print("Your data have been succesfuly migrated from one place to another region")
        event.set()                     ##Setting the event flag True
    except Exception as e:
        print(f"This is the exception of the function {e}")

##Second Function or trigger function
def backup_function():
    try:
        event.wait()
        print(f" Your thread details:- {threading.current_thread().name} ".center(120,"*"))
        if event.is_set():
            print("Now we are starting our backup process in 2 second wait for a while")
        else:
            print("Migration is not being performed succesfully so backup server can;t be started")
    except Exception as e:
        print(f"This is the exception of the function {e}")


##Create the thread for the function
migration = threading.Thread(target=migration_function,name="Migration_Thread")
backup = threading.Thread(target=backup_function,name="Backup Thread")

##starting the thread
migration.start()
backup.start()

##waiting for the child thread execution after then main thread should execute 
migration.join()
backup.join()

##Gettting the details of the main thread
print(f"This is the main thread details {threading.main_thread()}")