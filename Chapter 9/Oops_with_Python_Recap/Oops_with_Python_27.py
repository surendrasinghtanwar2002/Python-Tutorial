## In this section we will practise Protected Method ##

class Student:
    def __init__(self,name,age,mobile_no) -> None:
        self.name = name
        self.age = age
        self.mobile_no = mobile_no
    
    def display_method(self):
        return f"Student name is {self.name} and age is {self.age} and mobile no is {self.mobile_no}"
    
    def _college_data(self):
        print("This is Protected method which should not be accessed outside the class")



##Creating the object
t1 = Student(name="Surendra",age=24,mobile_no=11515515)
t1._college_data()
