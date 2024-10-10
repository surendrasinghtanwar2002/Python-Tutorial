                                                        ## Inheritance Class 4 ##

class Parent:
    def __init__(self,vechile_details:str,vechile_no:int) -> None:
        self.vechile = vechile_details
        self.vechile_no = vechile_no
    
    def print_details(self):
        return f"This is your car details {self.vechile} and vechile no is {self.vechile_no}"

class Child_Class(Parent):
    def __init__(self, vechile_details: str, vechile_no: int) -> None:
        super().__init__(vechile_details, vechile_no)                           ##In this method we will access the parent class attributes and pass value according to us


##Creating the child class
child1 = Child_Class(vechile_details="BMW",vechile_no=2580)
print(child1.__dict__)

