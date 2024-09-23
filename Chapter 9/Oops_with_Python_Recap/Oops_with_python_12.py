                                                                ## Inheritance Practise Class 1##


##This is parent class
class Parent:
    gold_Chain = True
    def __init__(self) -> None:
        self.house_Details = "2bhk"                             ##This are not parametrised constructor
        self.bike = "scooter"

    def print_details(self):
        return f"I am father and i own {self.house_Details} and {self.bike}"


##This is child class
class childclass(Parent):
    my_gold_chain = False
    def __init__(self,Car:str) -> None:
        self.my_car = Car
    def show(self):
        return f"I am son i own my parent house {self.house_Details} as well as their bike {self.bike} but my father cannot own my {self.my_car}"
    

##creating the instance from parent class
first = Parent()
print(first.__dict__)

##creating the instance from the child class
second = childclass(Car="BMW")
print(second.__dict__)
print(Parent.gold_Chain)            ##Accesing parent class variable

print(second.my_gold_chain)