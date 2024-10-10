                                                                        ## Class variable ##

class Students_details:
    college_name = "Poornima University"
    def __init__(self,Name:str,Age:int,Email:str) -> None:
        self.Name = Name
        self.Age = Age
        self.Email = Email
    
    def Print_Details(self):
        return f"Hello {self.Name} and your age is {self.Age} and your Email Address is {self.Email} and your college name is {self.college_name}"
    
    @classmethod
    def college_name_replacer(cls,new_College_name):
        cls.college_name = new_College_name
        return cls.college_name
    

##Creating instance
student1 = Students_details(Name="Surendra",Age=22,Email="surendrasinghtanwar667@gmail.com")
student2 = Students_details(Name="Harish Paramani",Age=35,Email="harishparmani@gmail.com")
student3 = Students_details(Name="Jitendar",Age=34,Email="jitendarsingh667@gmail.com")
student4 = Students_details(Name="Kamlesh",Age=18,Email="kamleshkumar667@gmail.com")


##Changing the class variable
Students_details.college_name_replacer(new_College_name="Jecrc")


##printing every instance  before the changes
print(f"Before Changes",student1.Print_Details())
print(f"Before Changes",student2.Print_Details())
print(f"Before Changes",student3.Print_Details())
print(f"Before Changes",student4.Print_Details())

##changing the class variable in instance level only
student1.college_name="Poornima University"
student3.college_name="Poornima University"

##printing every instance details after the changes
print(f"After Changes",student1.Print_Details())
print(f"After Changes",student2.Print_Details())
print(f"After Changes",student3.Print_Details())
print(f"After Changes",student4.Print_Details())

