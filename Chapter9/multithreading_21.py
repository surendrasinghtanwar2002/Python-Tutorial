                    ## In this section we will practise one more race condition question ##
from threading import *

##creating a class
class Bank():
    def __init__(self,bankname,bank_amount) -> None:
        self.bankname = bankname
        self.bank_amount = bank_amount
    
    def withdrawal(self,amount):
        try:
            print(f"Welcome to the {self.bankname}")
            if amount <= self.bank_amount:
                print("Yes you can withdraw the amount")
                self.bank_amount -= amount
                ct = current_thread()
                print(f"You withdraws have been performed succesfully {amount} Mr {ct}")
                print(f"The remaining balance of the bank is {self.bank_amount-amount}")
            else:
                print("Amount is not enought for the transcation You need a special permisssion for it")

        except Exception as e:
            print(f"Common Exception as e:- {e}")

##Creating the instance
withdraw = Bank("SBI",2000)

##thread for the each user
Jay = Thread(target=withdraw.withdrawal,args=(1500,),name="Jay")
Manish = Thread(target=withdraw.withdrawal,args=(1000,),name="Manish")
Surendra = Thread(target=withdraw.withdrawal,args=(2000,),name="Surendra")


##start all the thread
Jay.start()
Manish.start()
Surendra.start()


