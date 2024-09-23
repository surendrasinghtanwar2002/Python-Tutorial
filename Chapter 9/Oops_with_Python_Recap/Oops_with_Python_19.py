                                ## In this section we will practise level of inheritance ##

##Single Level Inheritance

##This is my first class of the college
class College:
    def __init__(self) -> None:
        self.college_name = "Poornima"
        print("College Class Constructor Called")

##This is my second class of the college
class Student(College):
    def __init__(self,name:str,age:int,mobile_no:int) -> None:
        super().__init__()
        self.studentname = name
        self.age = age
        self.mobile_no = mobile_no
    
    def print_Details(self):
        return f"Hello Mr {self.studentname} and your age is {self.age} and your mobile number is {self.mobile_no} and your college name is {self.college_name}"


##Creating the instance first
stu1 = Student(name="Surendra",age=22,mobile_no=9460824001)
print(stu1.print_Details())

##Creating the instance second
stu2 = Student(name="Jagdish",age=28,mobile_no=123456789)
print(stu2.print_Details())