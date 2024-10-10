                                                            ## Inheritance Class Class 2 ##

##This is parent class
class Parent:
    def __init__(self) -> None:
        self.car = "Maruti Suzuki"
        self.home = "2 BHK House"

##This is the child class
class child_class(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.car = "BMW"


##Creating the instance for the parent class
parent1 = Parent()
print("This is parent instance")
print(parent1.car)
print(parent1.home)

##Creating the instance for child class
child1 = child_class()
print("This is child instance")
print(child1.car)
print(child1.home)
