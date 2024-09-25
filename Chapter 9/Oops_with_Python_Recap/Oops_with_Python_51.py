                        ## __add__(self, other) Magic methods in python ##

## this method is used to add two object or instance variable with each other

class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age
    
    def __add__(self,other_object)->any:
        if isinstance(other_object,Person):
            return self.age + other_object.age
        return NotImplemented


##Creating the instance here
t1 = Person(name="Surendra",age=24)
t2 = Person(name="Rakesh",age=18)

print(t1+t2)
    

