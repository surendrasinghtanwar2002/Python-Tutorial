##Creating a Atm Machine

##importing necessary modules
import os
from time import sleep

##user balance and their record
Avilable_Balance = 250000

##Acceptable money format or form of the money
amount_acceptable = [500,1000,2000,5000,10000]

##main screen of the atm machine
welcome_message = " Welcome to Axis Bank Machine "
print(welcome_message.center(110,"*"))

##Main screen of the bank 
print("(Press 1) Check Balance")
print("(Press 2) Deposit Money")
print("(Press 3) Withdraw Money")
print("(Press 4) Exit \n")

##making a loop for running until user press wrong value 
try:
    while True:
        sleep(1)
        userinput = int(input("Enter your choice from below list: "))
    
        ##checking condition either the user input is right or not
    
        ##first condition checking
        if userinput <=0:
            print("Please Choose the correct option")
            pass
            
        ##second condition checking
        elif userinput == 1:
            sleep(1)
            os.system('clear')
            print(f"Your current balance is {Avilable_Balance}")
            print("\n (Press Q) Quit")
            print("\n (Press C) Continue")
            user_value = (input("\n Do you want to continue or quit: "))
            if user_value == "q" and user_value == "Q":
                break 
            elif user_value != "q" and user_value =="Q":
                print("Please choose correct option")
            else:
                break
                       
        ##third condition checking
        elif userinput == 2:
            sleep(1)
            os.system('clear')
            deposit_money = int(input("Enter your Deposit money ="))
            if deposit_money in amount_acceptable:
                Avilable_Balance += deposit_money
                message = "Now your balance after succesful deposit is"
                print(message.center(80), Avilable_Balance)
                break
            else:
                if deposit_money not in amount_acceptable:
                    print(f"Your given amount range {deposit_money} is not acceptable")
                else:
                    print("Our Bank is in update status no deposit will being proceed now")
                    
         ##fourth condition checking
        elif userinput == 3:
            sleep(1)
            os.system('clear')
            withdrawl_amount = int(input("Enter your withdrawal amount money range please"))
            if withdrawl_amount in amount_acceptable and withdrawl_amount < Avilable_Balance:
                    Avilable_Balance-= withdrawl_amount
                    succesful_message= "Your amount have been withdrawl succesfully"
                    print(succesful_message.center(80,Avilable_Balance))
                    break
            else:
                if withdrawl_amount not in amount_acceptable:
                    print(f"The withdrawl cannot being proceed {withdrawl_amount}")
                else:
                    print("There is some technical issue in our server please try again after some time")
    ##fifth condition checking
        elif userinput == 4:
                break  
except:
    pass
    
ending_message = "Thank you for coming Visit again"
print(ending_message.center(80,"*"))