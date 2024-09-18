                                                        ## Types of constructor in Python ##

#(1) Parametrised Constructor

class Email:
    def __init__(self,sender_name:str,receiver_name:str,date:str,subject:str,body:str) -> None:
        self.sender_name = sender_name if sender_name else "Surendra Singh Tanwar"
        self.receiver_name = receiver_name
        self.date = date
        self.subject = subject
        self.body = body
        self.salary = 25000
    


                                ## Creating the instance or object ##

##First instance or object
Email1 = Email(sender_name="Surendra",receiver_name="Mohan Krishna Aripa",date="25-08-2024",subject="Computer_Science",body="Regarding the New Computer Installation")
print(Email1.__dict__)          ##This will print the instance attributes value

##Second instance or object
Email2 = Email(sender_name="Rohan",receiver_name="Aripa",date="28-08-2024",subject="Regarding_leave",body="Hello i need the leave")
print(Email2.sender_name)                   ##Priting individual instance attributes/variable value
print(Email2.receiver_name)
print(Email2.date)
print(Email2.subject)
print(Email2.body)
print(Email2.salary)




