                ## In this section we will practise the create a class decorator that modifies the behavior of the existing class ##



##Creating the decorater
def CustomDecorater(cls):
    class Wrapper(cls):                                 ##We are inheriting the netmikoconnection to the wrapper class
        def __init__(self,*args, **kwargs):              ## When a new object is being created from original netmiko connection class those paramter will be passed to this function also 
            super().__init__(*args, **kwargs)
        
        def connection_establishement(self):
            print("We are calling the logger and this logger is being added by decorater".center(120,"*"))
            super().connection_establishement()
        
        def commands_send(self):
            print("We are calling the logger and this logger is being added by decorater")
            super().commands_send()
    return Wrapper


##Parent Class
@CustomDecorater
class Netmiko_Connection:
    def __init__(self,device_type,connection) -> None:
        self.device_type =device_type
        self.connection= connection

    def connection_establishement(self):                   ##First Method
            if self.device_type:
                print("We are connected to the device")
            else:
                print("We are not able to connect to the device")
        
    def commands_send(self):               ##Second Method
            if self.connection:
                print("we have sended the command succesfully")
            else:
                print("We are not able to send the commands successfully")

def main():
    t1 = Netmiko_Connection(device_type="cisco",connection=True)
    t1.connection_establishement()

if __name__ == "__main__":
    main()