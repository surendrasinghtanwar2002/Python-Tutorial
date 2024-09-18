                                                                ## Types of variable in the class ##


##Instance variable :- (Using Constructor, Using instance method, outside the class)


##Creating instance variable using constructor

class Student:
    def __init__(self,name:str,age:int,father_name:str,parents_mobile_no:int) -> None:              ##Constructor which will take the arguments while creating the instance or object
        self.name = name
        self.age = age                                                              ##Instance variable
        self.father_name = father_name
        self.parents_mobile_no = parents_mobile_no
    
    def student_display(self):
        return {
            "Student_name":self.name,
            "Student_age":self.age,
            "Student_father_name":self.father_name,
            "Parents_mobile_no":self.parents_mobile_no
        }


##Creating the instance
student_1 = Student(name="Surendra Singh",age=23,father_name="Vikram Singh",parents_mobile_no=94608240001)
student_2 = Student(name="Rohan",age=26,father_name="Mohanlal",parents_mobile_no=123456789)

##using the class methods
print(f"Before Changes in Student 1 details {student_1.student_display()}")
print(student_2.student_display())

student_1.name = "Harish Kumar"
student_1.age = 28
student_1.father_name="Manmohan"
student_1.occupation = "Engineer and he try a various approach to build the game server"                               ##Created outside class instance variable

print(f"After the changes in Student 1 details {student_1.student_display()}")
print(f"Added outside instance variable  '{student_1.occupation}' ")

print(f"Before changes {hasattr(student_1,"occupation")}")                  ##We will get the true output

del student_1.occupation                                ##In this section we will remove the student occupation attributes which were  created outside the class

print(f"After changes {hasattr(student_1,"occupation")}")    







