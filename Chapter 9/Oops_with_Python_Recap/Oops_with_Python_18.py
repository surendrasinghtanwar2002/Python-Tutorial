                                                            ## Inheritance Chapter 6 ##

class Netmiko_connection:               ##This is parent class
    def __init__(self) -> None:
        self.user_name = "static_username"
        self.user_pass = "static_password"
        print("Netmiko Connection Class is being called or base or parent class")
    
    def netmiko_establishement(self):
        if self.user_name:
            print("Connection established",self.user_name)
        else:
            print("Connection is not established due to wrong credentials",self.user_name)
        
class Connection(Netmiko_connection):
    def __init__(self,name:str, password:str) -> None:
        super().__init__()
        self.name = name
        self.password = password
        self.status = True
        print("Connection Class is being called or child class")

##Creating the instance
cnc1 = Connection(name="Surendra",password= input("Enter your password:- "))

print(cnc1.__dict__)            ##This will print the parent and child class details

cnc1.netmiko_establishement()




