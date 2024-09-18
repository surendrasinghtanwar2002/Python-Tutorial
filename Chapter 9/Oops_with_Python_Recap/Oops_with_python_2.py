                                                        ## Types of constructor in Python ##

#(2)Non- Parametrised Constructor

class Email:
    def __init__(self,receiver=None) -> None:
        self.email_sender_name = "xyz@gmail.com"
        self.email_receiver_name = receiver
        self.mobile_no = "9460824001"
        self.body = "Hello my name is surendra singh"


##Creating instance the multiple users
user_1 = Email(receiver="surendra@gmail.com")
user_2 = Email(receiver="jackson@gmail.com")
user_3 = Email(receiver="kalilinux@gmail.com")
user_4 = Email(receiver="emily@gmail.com")
user_5 = Email(receiver="jordan@gmail.com")

##printing all the user details in dictionary
print(user_1.__dict__)
print(user_2.__dict__)
print(user_3.__dict__)
print(user_4.__dict__)
print(user_5.__dict__)

##printing instance variable details
print(f"User 1 sender name:{user_1.email_sender_name} receiver name:{user_1.email_receiver_name} mobile no:{user_1.mobile_no} body:{user_1.body}")
print(f"User 2 sender name:{user_2.email_sender_name} receiver name:{user_2.email_receiver_name} mobile no:{user_2.mobile_no} body:{user_2.body}")
print(f"User 3 sender name:{user_3.email_sender_name} receiver name:{user_3.email_receiver_name} mobile no:{user_3.mobile_no} body:{user_3.body}")
print(f"User 4 sender name:{user_4.email_sender_name} receiver name:{user_4.email_receiver_name} mobile no:{user_4.mobile_no} body:{user_4.body}")
print(f"User 5 sender name:{user_5.email_sender_name} receiver name:{user_5.email_receiver_name} mobile no:{user_5.mobile_no} body:{user_5.body}")