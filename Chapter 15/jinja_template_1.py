from jinja2 import Environment,FileSystemLoader

device_details = {
    "device_type":"router",
    "hostname":"jackson",
    "loopback ip":"192.168.1.100"
}


##Creating the environment for the jinja
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates\\"))

##Getting the template from the folder 
template  = env.get_template("Router_template.txt")

##Render the items to the template
result = template.render(device_type=device_details["device_type"],hostname = device_details["hostname"],loopack_ip = device_details["loopback ip"])

print(f"This is your result of the template ------------> {result}  <-------------")

