from jinja2 import Environment,FileSystemLoader

##Creating the environment for the jinja
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates"))

##specify the template to render  on the screen
template = env.get_template("Macro.txt")

##Render the items according to the dummy data
dummy_data = {"interface":"Gigabit_Ethernet0/0"}

command = template.module.show_interface_status(dummy_data["interface"])

print(f"This is the output of the command --------------------->{command}")