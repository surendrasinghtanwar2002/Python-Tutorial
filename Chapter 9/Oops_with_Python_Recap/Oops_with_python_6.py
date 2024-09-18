                                                                ## In this section we will learn about the isinstance function ##

import random
from time import sleep

class Email:
    def __init__(self,sender_name:str,receiver_name:str,subject:str,body:str) -> None:
        self.email_sender_name = sender_name
        self.receiver_name = receiver_name
        self.subjet = subject
        self.body = body
    
    ##instance method 2
    def send_message(self):
        print(f"Wait we are sending the email to {self.receiver_name}".center(140))
        sleep(random.randint(2,4))
        return(f"Your email have been sent succesfuly !".center(140))

    ##instance method 2
    def add_image(self):
        user_input = input("Do you want to add the image (eg: Yes/No):- ").strip().lower()
        if user_input == "yes":
            print("Your image have been uploaded succesfully")
        else:
            print("We are sending your mail without image")
            self.send_message()


#Creating two object
e1 = Email(sender_name="Surendra@gmail.com",receiver_name="suresh@gmail.com",subject="english",body="i will attend each and every lecutre of the English from today itself")
e2 = Email(sender_name="Surendra@gmail.com",receiver_name="Jackson@gmail.com",subject="Order Decission",body="I am not interested in cold coffee I need a black coffee or a cappuccino")


##checking the whether this object is belong to that specific class or not
if isinstance(e1,Email):
    print("Hurray we are right that this object belong to email class")
else:
    print('I apolise the object does not belong to email class')

if isinstance(e2,Email):
    print("Hurray we are right that this object belong to email class")
else:
    print('I apolise the object does not belong to email class')
