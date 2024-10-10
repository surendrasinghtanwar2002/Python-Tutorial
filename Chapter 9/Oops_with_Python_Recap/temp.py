from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

# Print colored text
print(Fore.RED + 'This is red text')
print(Fore.GREEN + 'This is green text')
print(Fore.BLUE + 'This is blue text')

# Print colored background
print(Back.YELLOW + 'This has a yellow background')

# Reset style
print(Style.RESET_ALL + 'Back to normal text')





from functools import wraps

def connection_manager(cls):
    """Class decorator to manage Netmiko connections."""
    
    @wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)  # Create an instance of the class
        instance.connect()  # Establish connection
        try:
            yield instance  # Yield the instance for usage
        finally:
            instance.disconnect()  # Ensure disconnection

    return wrapper

@connection_manager
class NetworkDevice:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        """Establish a connection to the device."""
        try:
            self.connection = ConnectHandler(
                device_type=self.device_type,
                host=self.host,
                username=self.username,
                password=self.password
            )
            print(f"Connected to {self.host}")
        except Exception as e:
            print(f"Failed to connect to {self.host}: {e}")

    def disconnect(self):
        """Disconnect from the device."""
        if self.connection:
            self.connection.disconnect()
            print(f"Disconnected from {self.host}")

    def send_command(self, command):
        """Send a command to the device."""
        if self.connection:
            return self.connection.send_command(command)
        else:
            print("Connection is not established.")

# Usage
if __name__ == "__main__":
    device_info = {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "password"
    }

    with NetworkDevice(**device_info) as device:
        output = device.send_command("show ip interface brief")
        print(output)


from netmiko import ConnectHandler
import logging

# Setting up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_actions(cls):
    """Class decorator to log actions taken on NetworkDevice."""
    
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            logging.info(f"Initialized {self.__class__.__name__} for {self.host}")

        def connect(self):
            logging.info(f"Connecting to {self.host}")
            try:
                super().connect()
                logging.info(f"Successfully connected to {self.host}")
            except Exception as e:
                logging.error(f"Failed to connect to {self.host}: {e}")

        def disconnect(self):
            logging.info(f"Disconnecting from {self.host}")
            super().disconnect()
            logging.info(f"Disconnected from {self.host}")

        def send_command(self, command):
            logging.info(f"Sending command: '{command}' to {self.host}")
            result = super().send_command(command)
            logging.info(f"Received response from {self.host}: {result}")
            return result

    return Wrapped

@log_actions
class NetworkDevice:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        """Establish a connection to the device."""
        if not self.connection:
            self.connection = ConnectHandler(
                device_type=self.device_type,
                host=self.host,
                username=self.username,
                password=self.password
            )

    def disconnect(self):
        """Disconnect from the device."""
        if self.connection:
            self.connection.disconnect()
            self.connection = None

    def send_command(self, command):
        """Send a command to the device."""
        if self.connection:
            return self.connection.send_command(command)
        else:
            raise ConnectionError("Connection is not established.")

# Usage
if __name__ == "__main__":
    device_info = {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "password"
    }

    device = NetworkDevice(**device_info)
    device.connect()
    output = device.send_command("show ip interface brief")
    print(output)
    device.disconnect()
