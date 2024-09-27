from concurrent.futures import ThreadPoolExecutor
from time import sleep
import threading

# Creating the RLock Object
locker = threading.RLock()

# Device List
device_list = [
    {"device_type": "cisco", "username": "admin", "password": "hackerzone", "host_ip": "192.168.1.100"},
    {"device_type": "cisco", "username": "admin", "password": "hackerzone", "host_ip": "192.168.1.105"},
    {"device_type": "cisco", "username": "admin", "password": "hackerzone", "host_ip": "192.168.1.110"},
    {"device_type": "cisco", "username": "admin", "password": "hackerzone", "host_ip": "192.168.1.115"},
    {"device_type": "cisco", "username": "admin", "password": "hackerzone", "host_ip": "192.168.1.120"},
    {"device_type": "cisco", "username": "admin", "password": "hackerzone", "host_ip": "192.168.1.125"},
]

# Commands List
commands_list = ["show running config", "write", "show ip interface brief"]

# Netmiko Connection object
def netmiko_connection(device_details):
    with locker:  # Use 'with' to automatically manage the lock
        print(f"Connecting to the device {device_details['host_ip']}...")
        sleep(4)  # Simulate connection delay
        return f"Successfully connected to the device {device_details['host_ip']}"

# Send Command object
def command_send(command):
    with locker:  # Use 'with' to automatically manage the lock
        sleep(4)  # Simulate command sending delay
        print(f"Sending command: {command}")
        return f"Command '{command}' sent successfully."

# Calling the main function
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_task1_result = executor.map(netmiko_connection, device_list)
        for result in future_task1_result:  # Print the connection results
            print(result)
        
        future_task2_result = executor.map(command_send, commands_list)
        for result in future_task2_result:  # Print the command results
            print(result)
