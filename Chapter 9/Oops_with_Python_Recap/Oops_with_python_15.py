                                                    ##Inheritance Class 3 ##

##Parent Class
class Parent:
    def __init__(self,vechile_details:str) -> None:
        self.Vechile = vechile_details
        self.house_Details = "2 Bhk"
    
##Child Class
class Child_Class(Parent):
    pass


child1 = Child_Class(vechile_details="Bmw")
print("In this section child class will access all the parent class attributes")
print(child1.Vechile)
print(child1.house_Details)
        