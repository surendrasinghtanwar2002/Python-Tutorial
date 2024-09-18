                        ## In this section we will practise on Lock mechanism to prevent the race condition ##

from threading import *

class BusTicket:
    def __init__(self,bus_travel_name,avilable_seat,locker) -> None:
        self.bus_travel_name = bus_travel_name
        self.avilable_seat = avilable_seat
        self.locker = locker
    
    def Booking(self,seat_book):
        try:
            self.locker.acquire()           ##locking the mechanism
            print(f" Welcome to {self.bus_travel_name} ".center(120,"*"))
            ct = current_thread()
            if seat_book <= self.avilable_seat:
                print(f"You seat have been booked {ct}")
                self.avilable_seat-= seat_book
                print(f"After Transcation of {ct} Left Seats are {self.avilable_seat}")
            else:
                print(f"Sorry your seat cannot be booked {ct} avilable seat are alreay booked")
            self.locker.release()           ##releasing the mechanism

        except Exception as e:
            print(f"This is the exception of the Booking {e}")

##First create the lock object
locker = Lock()

##create the instance of the class
book = BusTicket(bus_travel_name="Harish Travelers",avilable_seat=2,locker=locker)

##Creating the thread object
Jay = Thread(target=book.Booking,args=(1,),name="Jay")
Manish = Thread(target=book.Booking,args=(1,),name="Manish")       
Surendra = Thread(target=book.Booking,args=(1,),name="Surendra")         

##Starting all the threads
Jay.start()
Manish.start()
Surendra.start()