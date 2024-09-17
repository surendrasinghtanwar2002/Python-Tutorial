                ## In this section we will pracitse of semaphore method in threading system ##
from threading import *
from time import sleep
import random
max_connection = 100                      ##Max connection limit
sempaphore = Semaphore(max_connection)            ##Creating the semaphore object here

##database connecitivity function
def database_connectivity(connection_no):
    try:
        print(f"This is your current thread {current_thread().name}".center(120,"*"))
        print(f"Thread {connection_no} is acquiring to make the connection.. ")
        ##sempahore condition
        with sempaphore:
            print(f"Thread id {connection_no} have been connected to our database".center(120,"*"))
            sleep(random.randint(15,20))
            print(f"Thread id {connection_no} have released connection to the database".center(120,"!"))

    except Exception as e:
        print(f"This is the exception of the function {e}")

def main():
    ##Creating the loop for multiple thread
    threads = []
    for i in range(180):                ##This is child thread
        user = Thread(target=database_connectivity,args=(i,),name=f"User {i}")
        threads.append(user)
        user.start()

    ##waiting for all thread to be completed
    for thread in threads:
        thread.join()

    ##Printing the main thred here
    print(f"This is your main thread {main_thread()}")
##Calling the main  function
if __name__ == "__main__":
    main()