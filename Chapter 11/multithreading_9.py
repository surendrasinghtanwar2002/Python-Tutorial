                                            ## Extending the thread class into the new class ##
from threading import Thread
from time import sleep

class NetmikoConnection(Thread):
    def __init__(self,value1,value2):               ##This is instance constructor
        super().__init__()
        self.value1 = value1                        ##This is instance or ojbect variable
        self.value2 = value2
        self.result = None

    ##Creating a method for the class
    def run(self):                          ##This method is overiding the existing thread method
        print("Netmiko Connection have been intialised")
        self.result = self.value1+self.value2
    

t1 = NetmikoConnection(value1= 10,value2=20)

t1.start()

sleep(3)
print(f"This is your result {t1.result}")



    