                                            ## __lt__(self, other) Magic methods in python ##

#this method, you can specify how two objects of your class should be compared when determining if one is less than the other.

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __lt__(self,other):
        if isinstance(other,Person):
            return self.age < other.age
        return NotImplemented                       ##NotImplemented means "I don't know"


##Creating the instance here
t1 = Person("rakesh",24)
t2 = Person("Jagdish",24)

print(t1<t2)
