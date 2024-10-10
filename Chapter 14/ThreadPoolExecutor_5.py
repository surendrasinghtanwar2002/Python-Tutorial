                                                    ## Using Multiple Iterables ##
from concurrent.futures import ThreadPoolExecutor
from time import sleep

##Square Function
def square(x:int,y:int):
    sleep(2)
    return x*y

##calling the main thread 
if __name__ == '__main__':
    my_list1= [1,2,3,10,22]
    my_list2= [3,4,5,7,8]
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(square,my_list1,my_list2)

     # Output the results
    print("Sum results:")
    for result in results:
        print(result)