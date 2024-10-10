from jinja2 import Environment, FileSystemLoader

# Create the environment
env = Environment(loader=FileSystemLoader("E:\\python_netmiko_project_practise\\templates"))

# Specify the template for the rendering
template = env.get_template("Macro_4.txt")

# Rendering the template using the dummy data
device_details = {
    "devices": [
        {
            "device_type": "router",
            "hostname": "Router1",
            "routing_protocol": "ospf",
            "area_number": "0",
            "interfaces": [
                {
                    "name": "GigabitEthernet0/0",
                    "ip_address": "192.168.1.1",
                    "subnet_mask": "255.255.255.0"
                },
                {
                    "name": "GigabitEthernet0/1",
                    "ip_address": "192.168.2.1",
                    "subnet_mask": "255.255.255.0"
                }
            ]
        },
        {
            "device_type": "switch",
            "hostname": "Switch1",
            "vlans": [
                {
                    "vlan_id": "10",
                    "vlan_name": "Sales"
                },
                {
                    "vlan_id": "20",
                    "vlan_name": "Engineering"
                }
            ]
        },
        {
            "device_type": "router",
            "hostname": "Router2",
            "routing_protocol": "eigrp",
            "as_number": "100",
            "interfaces": [
                {
                    "name": "GigabitEthernet0/2",
                    "ip_address": "192.168.3.1",
                    "subnet_mask": "255.255.255.0"
                }
            ]  # Single interface case
        },
        {
            "device_type": "switch",
            "hostname": "Switch2",
            "vlans": [
                {
                    "vlan_id": "30",
                    "vlan_name": "Default"
                }
            ]  # Single VLAN case
        }
    ]
}

# Render the configuration
output = template.module.device_configuration(device_details)

print(output)
