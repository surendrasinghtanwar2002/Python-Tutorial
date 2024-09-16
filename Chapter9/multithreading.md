##from threading import Thread
from threading import Thread,current_thread
from netmiko import ConnectHandler

# Subclassing Thread to handle connections to network devices
class NetmikoThread(Thread):
    def __init__(self, device_params, command):
        Thread.__init__(self)
        self.device_params = device_params
        self.command = command
        self.result = None  # This will hold the command output

    def run(self):
        try:
            print(f"This is your child thread {current_thread()}")
            connection = ConnectHandler(**self.device_params)
            self.result = connection.send_command(self.command)
            connection.disconnect()
        except Exception as e:
            print(f"Failed to connect to {self.device_params['host']}: {e}")

# Device connection parameters
device_1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.100",
    "username": "admin",
    "password": "hackerzone",
}
device_2 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.101",
    "username": "admin",
    "password": "hackerzone",
}
device_3 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.105",
    "username": "admin",
    "password": "hackerzone",
}
device_4 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.103",
    "username": "admin",
    "password": "hackerzone",
}
device_5 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.120",
    "username": "admin",
    "password": "hackerzone",
}
device_6 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.110",
    "username": "admin",
    "password": "hackerzone",
}
device_7 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.115",
    "username": "admin",
    "password": "hackerzone",
}


# List of devices
devices = [device_1, device_2,device_3,device_4,device_5,device_6,device_7]


# Command to be sent to all devices
command = "show ip interface brief"

# Creating thread objects for each device
threads = [NetmikoThread(device, command) for device in devices]

# Start each thread
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print results from all devices
for i, thread in enumerate(threads):
    print(f"Result from device {devices[i]['host']}:")
    print(thread.result)
    print("-" * 40)

print(f"This is my main Thread of the class {current_thread()}")