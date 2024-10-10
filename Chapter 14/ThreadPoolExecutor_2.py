                                                    ## Handling Execption ##
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep


##Basic function for the thread
def divide(x:int,y:int):
    print("We will divide your number")
    sleep(10)                ##Delay for 3 second
    return x /y


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:

        #submting the task to executor 
        Futures = [executor.submit(divide,10,i)for i in range(3,-1,-1)]

        ##Retriving the result of the future object
        for future in as_completed(Futures):
            try:
                result = future.result()  # Get the result, may raise exception
                print(result)
            except ZeroDivisionError:
                print("Caught division by zero!")


##Calling the main function
if __name__ =="__main__":
    main()
