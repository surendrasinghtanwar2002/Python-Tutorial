##declaring a existing user information for checking the user input
_user_list = ["surendrasinghtanwar667@gmail.com","hackerzone@gmail.com","jack@gmail.com","atulsharma@gmail.com","admin@gmail.com"]

###declaring avilable Ip address for telnet connection in the list
_telnet_server = ["192.168.1.1", "192.168.2.1", "192.168.3.1", "192.168.4.1"]

##collecting user email address
user_id = input("Enter your user email address for telent connection: ") or _user_list[4]

##collecting server Ip address
server_Address=input("Enter your Telnet Server IP Address: ") or _telnet_server[0]

if user_id in _user_list and server_Address in _telnet_server:
    print("Your telnet connection is performed succesfully with", user_id,server_Address)

else:
    if (user_id in _user_list != user_id):
        print("The user is not vaild", user_id, "Please try again")
    elif (server_Address in _telnet_server != server_Address):
        print("The telent server IP address does not exist", server_Address,"Please give another server Address")
    else:
        print("Server is being down due to some reason or heavy traffic is being there")
