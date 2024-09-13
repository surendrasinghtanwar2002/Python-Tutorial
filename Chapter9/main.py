import packages.arista_devices as arista_modules
import packages.cisco_devices as cisco_modules

print(" This is the main function where i am importing everything ".center(120,"*"))

print(arista_modules.module_1.arista())
print(cisco_modules.module_2.cisco())

