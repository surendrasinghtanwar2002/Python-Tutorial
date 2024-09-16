                                                        ## Extending the thread class and performing our task ##
from netmiko import ConnectHandler
from threading import Thread,current_thread
from time import sleep
from typing import Any, Iterable, Mapping


##Creating The class which will being extended or inherited from the thread class
class NetmikoConnection_device(Thread):
    def __init__(self,device_Details,commands):
        self.device = device_Details                    ##states manag
        self.commands = commands
        self.result = None
        super().__init__()
    
    ##Overide the run method 
    def run(self):
        try:
            print(f"This is the current thread {current_thread()}")
            connection = ConnectHandler(**self.device)
            result = connection.send_command(self.commands)
            self.result = result            ##Intialising the value
        except Exception as e:
            print(f"This is the exception error {e}")


##devices details
device_1 = {
    "device_type":"cisco_ios",
    "host":"192.168.1.100",
    "username":"admin",
    "password":"hackerzone"
}
device_2 = {
    "device_type":"cisco_ios",
    "host":"192.168.1.101",
    "username":"admin",
    "password":"hackerzone"
}
device_3 = {
    "device_type":"cisco_ios",
    "host":"192.168.1.105",
    "username":"admin",
    "password":"hackerzone"
}
device_4 = {
    "device_type":"cisco_ios",
    "host":"192.168.1.103",
    "username":"admin",
    "password":"hackerzone"
}
device_5 = {
    "device_type":"cisco_ios",
    "host":"192.168.1.120",
    "username":"admin",
    "password":"hackerzone"
}
device_6 = {
    "device_type":"cisco_ios",
    "host":"192.168.1.110",
    "username":"admin",
    "password":"hackerzone"
}
device_7 = {
    "device_type":"cisco_ios",
    "host":"192.168.1.115",
    "username":"admin",
    "password":"hackerzone"
}

##Creating the list for the device
devices = [device_1,device_2,device_3,device_4,device_5,device_6,device_7]

commands = "show ip interface brief"

MyThreads = [NetmikoConnection_device(device_Details=devices,commands=commands ) for devices in devices]


##Starting the thread with the loop
for MyThread in MyThreads:
    MyThread.start()

# Wait for all threads to complete
for MyThread in MyThreads:
    MyThread.join()

# Print results from all devices
for i, thread in enumerate(MyThreads):
    print(f"Result from device {devices[i]['host']}:")
    print(thread.result)
    print("-" * 40)



