                            ## In this section we will pracitse of semaphore method in threading system ##
from threading import *
from time import sleep
import random
import os

##Max number of printer machine
max_printer_capability = 10
##Creating the semaphore object
semaphore = Semaphore(max_printer_capability)

##Creating the function
def printing_machine(printer_connection_queue_no):
    try:
        print(f"Printer Connection que is trying to connect {printer_connection_queue_no}")
        with semaphore:
            print(f"Printing queue no {printer_connection_queue_no} have been choosed for the priting ...")
            sleep(random.randint(8,9))              ##sleeping for random number
            print(f"Printing queue no {printer_connection_queue_no} have been printed and they are releasing the memory")
    except Exception as e:
        print(f"This is the exception of the program {e}")

##Main Function
def main():
    threads_list = []
    try:
        os.system("cls")
        print("We will call the loop here for creating the threads")
        user_input = int(input("Enter your number of threads you want to create (eg:-10,20,30,50):- "))
        for i in range(user_input):
            user = Thread(target=printing_machine,args=(i,),name=f"User_Thread {i}")
            threads_list.append(user)
            user.start()

        ##waiting for the all thread to be complete
        for thread in threads_list:
            thread.join()              
        
        print(f"After completing all the thread main thread will be executed \n{main_thread}".center(120))

    except Exception as e:
        print(f"This is the exception of the function {e}")

##Calling the main function
if __name__ == "__main__":
    main()