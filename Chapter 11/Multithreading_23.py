                ## In this section we will perform the the Lock all method release Part 2 ##
from threading import *

##creating a class
class Banking:
    def __init__(self,BankName:str,Bank_Total_Amount:int,threadlocker:object) -> None:
        self.BankName = BankName
        self.Bank_Total_Amount = Bank_Total_Amount
        self.threadlocker = threadlocker

    def Withdrawal(self,withdraw_amount):                       ##method for the class
        try:
            # self.threadlocker.acquire()                         ##this will lock the method for one thread at a time
            print(f" {self.BankName} ".center(120,"*"))
            ct = current_thread().name
            if withdraw_amount <= self.Bank_Total_Amount:
                self.Bank_Total_Amount -= withdraw_amount
                print(f"Your amount have been succesfully completed {ct} with amount of {withdraw_amount}")
            else:
                print(f"Bank Current Balance is {self.Bank_Total_Amount}")
                print(f"Your Bank does not have enough money {ct}")
            # self.threadlocker.release()                         ##releasing the lock for another thread    
        except Exception as e:
            print(f"The exception of the function {e}")


##Creating a thread lock for the object
locker = Lock()

##Creating a instance 
book = Banking(BankName="Julelal Banking",Bank_Total_Amount=15000,threadlocker=locker)

##Creating multiple threads for the user
User_Jay = Thread(target=book.Withdrawal,args=(5000,),name="User_Jay")
User_Manish = Thread(target=book.Withdrawal,args=(1500,),name="User_Manish")
User_Kamlesh = Thread(target=book.Withdrawal,args=(2000,),name="User_Kamlesh")
User_Jagdish = Thread(target=book.Withdrawal,args=(4000,),name="User_Jagdish")
User_Surendra = Thread(target=book.Withdrawal,args=(2500,),name="User_Surendra")
User_Yash = Thread(target=book.Withdrawal,args=(2500,),name="User_Yash")

##starting all the threads
User_Jay.start()
User_Manish.start()
User_Kamlesh.start()
User_Jagdish.start()
User_Surendra.start()
User_Yash.start()