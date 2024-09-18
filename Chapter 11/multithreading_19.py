                                    ## In this section we will practise without threading function and threding function time ##



# ##Using the multhread process
# from threading import Thread
from time import time

# ##Creating target function
# def target1_function():
#     try:
#         for items in range(80):
#             print(f"Hello world 80 times")
#     except Exception as e:
#         print(f"This is the exception of teh function 1 {e}")

# ##Creating the target function
# def target2_function():
#     try:
#         for items in range(90):
#             print("Hello world 90 times")
#     except Exception as e:
#         print(f"This is the exception of teh function 1 {e}")


# ##Creating the thread object for the each function
# t1 = Thread(target=target1_function)
# t2 = Thread(target=target2_function)

# starting_time = time()
# t1.start()
# t2.start()
# ending_time = time()
# t1.join()
# t2.join()
# print(f"The total time taken for the exeuction of this both function is {ending_time-starting_time}")



##Without threading process
##Creating target function
def target1_function():
    try:
        for items in range(80):
            print(f"Hello world 80 times")
    except Exception as e:
        print(f"This is the exception of teh function 1 {e}")

##Creating the target function
def target2_function():
    try:
        for items in range(90):
            print("Hello world 90 times")
    except Exception as e:
        print(f"This is the exception of teh function 1 {e}")

##Calling the function
starting_time = time()
target1_function()
target2_function()
ending_time = time()
print(f"The total time taken for the exeuction of this both function is {ending_time-starting_time}")