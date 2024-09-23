                                                            ## Inheritance Chapter 5 ##


class Mobile_Blue_Print:                ##Parent Class
    def __init__(self) -> None:
        self.ram = "8Gb Ram"
        self.storage = "128Gb"
        print("Parent Class Attributes Called")
    
class Mobile(Mobile_Blue_Print):
    def __init__(self) -> None:
        super().__init__()                ##This will call all the super methods variable
        self.mobile_module = "Iphone XR"
        print("Child Class Attributes Called")


##Creating the instance
mobile1 = Mobile()
print(mobile1.__dict__)
    
