from jinja2 import Environment,FileSystemLoader

##Create the Jinja Environment
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates\\"))

##Load the template from the folder
template = env.get_template("Macro_5.txt")

##dumy data 
data = {
    "devices": [
        {
            "device_type": "router",
            "hostname": "Router1",
            "routing_protocol": "ospf",
            "ospf_area_id": "0",
            "router_id": "1.1.1.1",
            "networks": [
                {"ip_address": "192.168.1.0", "wildcard_mask": "0.0.0.255"},
                {"ip_address": "10.0.0.0", "wildcard_mask": "0.255.255.255"}
            ]
        },
        {
            "device_type": "router",
            "hostname": "Router2",
            "routing_protocol": "eigrp",
            "as_number": "100",
            "router_id": "2.2.2.2",
            "networks": [
                {"ip_address": "192.168.2.0", "wildcard_mask": "0.0.0.255"}
            ]
        },
        {
            "device_type": "router",
            "hostname": "Router3",
            "routing_protocol": "rip",
            "router_id": "3.3.3.3",
            "network": ["172.16.0.0", "0.15.255.255"]
        }
    ]
}

##render the template using macro method 
result = template.module.routing_configuration(device_details=data)

##printing the result 
print(f"This is the result of the jinja templating ----------> \n {result}")