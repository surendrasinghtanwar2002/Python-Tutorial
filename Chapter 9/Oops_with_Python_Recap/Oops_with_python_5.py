                                        ##In thi section we will practise built in class attributes ##

#(1) __doc__    :- Class Documentation String
#(2)__name__    :- Class name
#(3)__dict__    :- Dictionary containing class's namespace
#(4)__module__  :- Module name in which class is defined
#(5)__bases__   :- List of bases classes   (Not covered yeat)
class Employee:
    '''
        This class is being created for the employee details.

        It will take the name, age, and mobile number while creating the instance.
    '''
    def __init__(self, name, age, mobileno) -> None:     
        self.name = name
        self.age = age
        self.mobileno = mobileno

    def display(self):
        try:
            print(f"Hello your name is {self.name}")
            print(f"Hello your age is {self.age}")
            print(f"Hello your mobile number is {self.mobileno}")
        except Exception as e:
            print(f"This is the exception of the function {e}")

print(f"This will print the doc of the class {Employee.__doc__}")
print(f"This will print the name of the class {Employee.__name__}")
print(f"This will print all the methods and official information of the class \n {Employee.__dict__}")
print(f"This will print the module name in which class is defined {Employee.__module__}")

