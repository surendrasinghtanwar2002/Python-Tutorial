## This is the first parent or base class
class Country:
    def __init__(self) -> None:
        self.country_name = "India"
        print("Country class constructor called")

## This is the second parent or base class
class State_class:
    def __init__(self) -> None:
        self.State = "Rajasthan"
        print("State Class Constructor called")

# This is the child class
class City(Country, State_class):
    def __init__(self) -> None:
        Country.__init__(self)  # Call the Country class constructor
        State_class.__init__(self)  # Call the State_class constructor
        self.City = "Balotra"
    
    def details(self):
        return f"Your city {self.City} is located in {self.State} which is part of country {self.country_name}"

## Creating the instance
obj1 = City()
print(obj1.details())
