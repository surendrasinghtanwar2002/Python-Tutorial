                                                    ## __str__(self) Magic methods in python ##

## This method is used to change the object id to any specific string

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"This is person class object which is being used to perform various activity"
    
    def __repr__(self) -> str:
        return f"This is the debugger purpose method for easy debugging"
    
    
##creating the instance
t1 = Person("surendra",24)
print(repr(t1))
