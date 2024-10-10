from typing import Any

class Logger:
    def __init__(self,logger="Log:-") -> None:
        self.Prefix_value = logger
    
    def __call__(self, message:Any) -> Any:
        return self.Prefix_value + message


##Creating the instance or object
t1 = Logger()
t2 = Logger()

print(t1("We are working on Ec2"))
print(t2("Ospf is not working well"))