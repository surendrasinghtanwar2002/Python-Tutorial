## In this section we will Practise Basic Private Method in a class ##
class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age

    def __display(self):            ##Private Method
        print(f"My name is {self.name} and my age is {self.age}")
        return "Private method called"
    
    def public_display(self):
        self.__display()            ##Accessing private method inside the class
        return "We are calling the public method"

##Creating the object heree
c1 = Person(name="Suresh",age=24)
c1.public_display()
print(c1._Person__display())
