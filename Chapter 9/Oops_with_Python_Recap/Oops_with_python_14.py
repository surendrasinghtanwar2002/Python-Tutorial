                                                            ##Inheritance Class 3 

##Parent Class
class Parent:
    def __init__(self) -> None:
        self.Vechile = "Scooter"
        self.house = "2 Bhk"

##Child Class
class Child(Parent):
    pass

child1 = Child()
print(child1.__dict__)
print(child1.Vechile)
print(child1.house)