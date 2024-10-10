from jinja2 import Environment,FileSystemLoader

##Creating the environment for the jinja templating 
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates\\"))

##Getting the template from the enivronment
template = env.get_template("macro_2.txt")

##Rendering the items as per the interface 
dummy_data = {"interface":["Gig0/1","Gig0/2","Gig0/3","Gig0/4","Gig0/5"]}

result = template.module.show_interface_status(dummy_data["interface"])

print(f"This is your result of the template {result}")
