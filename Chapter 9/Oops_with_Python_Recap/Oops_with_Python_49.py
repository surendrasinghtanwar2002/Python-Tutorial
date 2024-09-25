                                                ## __eq__(self, other) Magic methods in python ##

#special method that defines how to compare two objects for equality using the equality operator (==)

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value,Person):
            return self.name == value.name and self.age == value.age
        


##Instance 
t1 = Person(name="Surendra",age=37)
t2 = Person(name="Surendra",age=37)

print(t1==t2)