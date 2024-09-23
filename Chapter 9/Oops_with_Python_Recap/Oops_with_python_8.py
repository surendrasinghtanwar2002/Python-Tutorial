                                                            ## Class variable & method ##

class netmiko_connection:
    netmiko_status = True                                   ##Class variable
    def __init__(self) -> None:
        pass

    def command_status(self):                               ##instance methods
        try:
            print("We are sending your commands")
        except Exception as e:
            print("This is common exception",e)

    @classmethod
    def netmiko_status_change(cls,netmiko_new_status):
        try:
            cls.netmiko_status = netmiko_new_status
            return cls.netmiko_status
        except Exception as e:
            print(f"This is the exception of the function")
    

##Creating an instance
e1 = netmiko_connection()
e2 = netmiko_connection()
print(f"Before changes",e1.netmiko_status)
print(f"Before changes",e2.netmiko_status)

##chaning the netmiko status
netmiko_connection.netmiko_status_change(netmiko_new_status=False)

##printing the latest netmiko status
print(netmiko_connection.netmiko_status)

print(f"After changes",e1.netmiko_status)
print(f"After changes",e2.netmiko_status)


##Chaning the netmiko status for specific instance
e1.netmiko_status= True

print(e1.netmiko_status)               


##printing the global class variable details
print(netmiko_connection.netmiko_status)

print(e2.netmiko_status)
print(e1.netmiko_status)                        ##chaning value for specifc instance
