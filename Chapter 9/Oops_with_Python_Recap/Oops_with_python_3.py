                                ## Creating the class instance methods and accessing outside the class ##

from time import sleep
import random

##First Create the class
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


##Creating the instance

user_1 = Email(sender_name="xyz@mail.com",receiver_name="subway@gmail.com",subject="None",body="Hello")
user_2 = Email(sender_name="yahoo@mail.com",receiver_name="starbucks@gmail.com",subject="Order Place",body="need a coffee urgent")
user_3 = Email(sender_name="gmail@mail.com",receiver_name="fortnite@gmail.com",subject="Security Concern",body="Your firewall is being stucked")
user_4 = Email(sender_name="elisa@mail.com",receiver_name="halowins@gmail.com",subject="Party",body="We enjoyed a hallowin party very much")


##printing the instance varible of each object in dictionary format
print(user_1.__dict__)
print(user_2.__dict__)
print(user_3.__dict__)
print(user_4.__dict__)

##printing the individual instance variable of each object or instance
print(f"User 1 sender name:{user_1.email_sender_name} receiver name:{user_1.receiver_name} subjet: {user_1.subjet} body:{user_1.body}")
print(f"User 2 sender name:{user_2.email_sender_name} receiver name:{user_2.receiver_name} subjet: {user_2.subjet} body:{user_2.body}")
print(f"User 3 sender name:{user_3.email_sender_name} receiver name:{user_3.receiver_name} subjet: {user_3.subjet} body:{user_3.body}")
print(f"User 4 sender name:{user_4.email_sender_name} receiver name:{user_4.receiver_name} subjet: {user_4.subjet} body:{user_4.body}")


##Now accessing the class methods 1
print(user_1.send_message())
print(user_2.send_message())
print(user_3.send_message())
print(user_4.send_message())

##Now accessing the class methods 2
print(user_1.add_image())
print(user_2.add_image())
print(user_3.add_image())
print(user_4.add_image())
