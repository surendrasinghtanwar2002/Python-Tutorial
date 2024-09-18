                                        ## In this we will learn how to create the threading object and start the thread for target function ##
from threading import Thread

##Creating a function for the thread
def myfunction():
    for items in range(4):
        print('hello world')
    
##Create the thread object
t1 = Thread(target=myfunction)

#Start the thread
t1.start()

for items in range(4):
    print("welcome")