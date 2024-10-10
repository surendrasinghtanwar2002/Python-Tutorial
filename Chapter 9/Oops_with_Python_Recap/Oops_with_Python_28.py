                            ## Overriding the built in function of the python ##

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"Your name is:-{self.name} and your age is {self.age}"

##Creating the object or instance
per = Person(name="Sure",age=24)

print(per)          ##It will print the basic functionalities of print
