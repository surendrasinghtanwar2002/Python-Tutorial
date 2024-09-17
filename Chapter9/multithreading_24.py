                    ## In this section we will perform the RLock and compare the Rlock with normal Lock Mechanism ##
from threading import *

##Creating the class
class Bank:
    def __init__(self,bank_balance:int) -> None:
        self.bank_balance = bank_balance
        self.locker = RLock()
    
    def deposit_amount(self,depositamount):
        self.locker.acquire()               ##Locking the system
        try:
            ct= current_thread().name
            print(f" Welcome to International Banking {ct} ".center(120,"/"))
            print(f"\n Your current balance is {self.bank_balance}")
            print(f"\n Your Deposit balance is {depositamount}")
            self.bank_balance += depositamount
            print(f"\n After Adding the balance to your system {self.bank_balance}")
        except Exception as e:
            print(f"The common exception is {e}")

        self.locker.release()               ##Unlocking the system
    
    def withdrawl_amount(self,withdraw_amount):
        try:
            self.locker.acquire()               ##Locking the system
            ct= current_thread().name
            print(f" Welcome to International Banking {ct} ".center(120,"/"))
            print(f"\n Your current balance is {self.bank_balance}")
            print(f"Your Withdrawl amount is {withdraw_amount}")
            if withdraw_amount <= self.bank_balance:
                print(f"Your amount can be withdraw {withdraw_amount}")
                self.bank_balance -= withdraw_amount
                print(f"After deducting the amount your balance is {self.bank_balance}")
            else:
                print(f"Your Payment cannot be performed due to low amount {self.bank_balance}")
        
        except Exception as e:
            print(f"Common Withdraw amount method error {e}")

        self.locker.release()               ##Unlocking the system


##Creating the instance of the class 
bank = Bank(bank_balance=15000)

##Creating the thread for multiple user for deposting amount
Jackson = Thread(target=bank.deposit_amount,args=(1500,),name="Jackson")
Rosy = Thread(target=bank.deposit_amount,args=(1500,),name="Rosy")
Amilie = Thread(target=bank.deposit_amount,args=(1500,),name="Amilie")
Harry = Thread(target=bank.deposit_amount,args=(1500,),name="Harry")

##Creating the thread for multiple user for withdraw amount
Kamlesh = Thread(target=bank.withdrawl_amount,args=(1500,),name="Kamlesh")
Rakesh = Thread(target=bank.withdrawl_amount,args=(2500,),name="Rakesh")
Jagdish = Thread(target=bank.withdrawl_amount,args=(4500,),name="Jagdish")
Suresh = Thread(target=bank.withdrawl_amount,args=(4500,),name="Suresh")
Surendra = Thread(target=bank.withdrawl_amount,args=(9500,),name="Surendra")

##Starting all the threads of deposit user
Jackson.start()
Rosy.start()
Amilie.start()
Harry.start()

##Starting all the threads of withdrawal user
Kamlesh.start()
Rakesh.start()
Jagdish.start()
Suresh.start()
Surendra.start()



