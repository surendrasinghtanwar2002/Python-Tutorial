
                                                    ## In this we have practised encapsulation with Private Method ##

from time import sleep

class Bank:
    def __init__(self) -> None:
        self.bank_name = "Bank_of Baroda"
        self.__bank_balance = 2800000000
    
    def withdraw(self,withdraw_amount:int):
        if withdraw_amount:
            print("Wait we are processing to your account")
            self.__bank_balance -= withdraw_amount
            sleep(2)            ##Delay for 2 second
            print("Your withdraw is succesful Please visit again")
    
    def deposit(self,deposit_amount:int):
        if deposit_amount:
            print("Wait we are processing with your transcation")
            self.__bank_balance+=deposit_amount
            sleep(2)                ##Delay for 2 second
            print("We have completed your deposit request")

    def __bank_balance_display(self):           ##This is private method
        return(f"Your bank balance is {self.__bank_balance}")
    

    def manager_account(self):
        user_name = input("Enter your Username:- ")
        user_pass = input("Enter your Password:-")
        if  user_name and user_pass:
            print(f"Your bank balance is {self.__bank_balance}")
        else:
            print(f"Your are not a valid user")


##Creating the instance or object
user1 = Bank()
print(user1.__dict__)
print(user1._Bank__bank_balance_display())
            