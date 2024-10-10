from jinja2 import Environment,FileSystemLoader

##Creating the environment for the jinja
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates"))

##Speciying the template for the configuration
template = env.get_template("EIGRP_Interface_Configuration.txt")

##Creating dummy data for the device
device_data = {
    "device_type":"router",
    "interface":[("Gigabit_Ethernet0/0","192.168.1.100"),("Gigabit_Ethernet0/1","192.168.1.105"),("Gigabit_Ethernet0/2","192.168.1.110")],
}

##Rendering the template with data \
result = template.render(device_type=device_data["device_type"],interface=device_data["interface"])

print(f"This is the result of the template output --------> {result}")