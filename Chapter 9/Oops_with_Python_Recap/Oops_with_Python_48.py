                                                ## __len__(self) Magic methods in python ##

##method that defines how to determine the length of an object using the built-in len() function

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __len__(self):
        return len(self.name)


##Creating the instance
t1 = Person("surendra",25)

print(len(t1))


