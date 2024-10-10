from jinja2 import Environment,FileSystemLoader

##Create the jinja environment
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates\\"))

##Loading the template inside the jinja templating 
template = env.get_template('Macro_3.txt')

##rendering the items in the macro function using dummy data
dummy_data = {"interface":["Gigabit_Ethernet0/0","Ethernet0/0","Serial_Link0/0","Fast_Ethernet0/0"]}

result = template.module.show_interface_status(interface= dummy_data["interface"],details = True)

print(f"This is the result of the template --------------> {result} <--------------")