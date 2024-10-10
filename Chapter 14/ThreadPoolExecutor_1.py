                                                    ## Basic Thread Pool Executor ##

from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep


# Define a simple function that simulates a task
def multiply(x:int,y:int):
    sleep(3)            ##2 second delay
    return x * y

def main():
    ##Creating a Thread Pool Executor
    with ThreadPoolExecutor(max_workers=2) as executor:

        ##Submiting the task to the executor
        Futures = [executor.submit(multiply,i,2)for i in range(1000)
                ]
        
        ##Retriving the result from the list
        for future in Futures:
            print(f"This is the future or return object {future.result()}")

###Calling the main function
if __name__ == "__main__":
    main()

##The submit method is used to schedule a callable (function) to be executed asynchronously.
#It returns a Future object, which represents the execution of the callable and allows you to check its status or get the result.


