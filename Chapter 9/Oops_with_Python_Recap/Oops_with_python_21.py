                            ## In this section we will practise the hierarchical level of inheritance ##
import os

##This is the base class or parent class
class Netmiko_Connection:
    def __init__(self) -> None:
        self.netmiko_connection = True                                  ##This is netmiko object (Hypothetical object)
        print("We are calling the netmiko connection class Constructor")
    
    def device_details(self):
        return {
            "device_type":"ios",
            "username":"admin",
            "password":"hackerzone"
        }
    
##This is the child class dereived from parent class
class Configuration_Device(Netmiko_Connection):
    def __init__(self) -> None:
        super().__init__()
        self.commands = ["show ip interface brief","show clock","show running-config"]
        print("Calling the Configuration device class Constructor")
    
    def send_commands(self):
        if self.netmiko_connection:
            print("We have sent all the commands to the specific devices")
        else:
            print("Sorry we are not able to send the commands due to no netmiko connection object")

##This is the child class derieved from the parent class
class Backup_device(Netmiko_Connection):
    def __init__(self) -> None:
        super().__init__()
        print("Calling the Backup Device Class Constructor")
    
    def backup_device(self):
        if self.netmiko_connection:
            print("We are backuping our device using your order")
        else:
            print("Sorry we are not able to backup up your device due to no netmiko connection object")


os.system("clear")

##Creating the object or instance first
taks1 = Backup_device()
print(taks1.device_details())
taks1.backup_device()

##Creating the object or instance second
print("Break Statement".center(140,"*"))
task2 = Configuration_Device()
print(task2.device_details())
task2.send_commands()


