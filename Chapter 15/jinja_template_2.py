from jinja2 import Environment,FileSystemLoader

##Creating the environment for the jinja
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates\\"))

##Load the actual template into the jinja
template = env.get_template("EIGRP_Configuration_template.txt")

##data for the template 
device_configuration = {
    "device_type":"Router",
    "hostname":"Office_Router",
    "routing_type":"EIGRP",
    "as_number":25,
    "network_list":[("192.168.1.0","0.0.0.255"),("192.168.2.0","0.0.0.255"),("0.0.0.0","255.255.255.255")]
}

##Rendering the template
result = template.render(device_type=device_configuration["device_type"],hostname = device_configuration["hostname"],routing_type=device_configuration["routing_type"],as_number=device_configuration["as_number"],network_list=device_configuration["network_list"])



print(f"This is your entire command output -----------------------> {result}")