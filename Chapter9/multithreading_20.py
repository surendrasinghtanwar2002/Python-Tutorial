                                        ## In this section we will apply the race condition problem and check the output ##
from threading import *
from time import sleep

class Busticket():
    def __init__(self,name,avilable_seat) -> None:
        self.name = name
        self.avilable_seat = avilable_seat
    
    ##bus ticket booking
    def booking(self,need_seats):
        try:
            print(f"Total avilable seats are {self.avilable_seat}")
            if self.avilable_seat >=need_seats:
                self.avilable_seat -= need_seats
                ct = current_thread().name
                print(f"{need_seats} are allocated to {ct}")
            else:
                print(f"Seat are not avilable")
        except Exception as e:
            print(f"This is the exception of the function {e}") 
    

##create the class instance
book = Busticket("Mahalaxmi Travelers",2)

##creating the threads for user
jay1 = Thread(target=book.booking,args=(1,),name="Jay")
Mohan = Thread(target=book.booking,args=(1,),name="Mohan")

##starting the thread
jay1.start()
Mohan.start()
