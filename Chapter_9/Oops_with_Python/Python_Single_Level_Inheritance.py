# ##Single Level Inheritance will drivied all the functionalities or method from the parent class

# ##Practise 1

# ##Creating the super class
# class animal:
#     def eat (self):     ##Creating the constructor
#         return("I can eat the food")

# ##now i am creating the another class which will inherit all the functionalities from the parent
# class dog(animal):
#     def __init__(self,name):
#         self.name = name
    
#     def display(self):
#         return(f"My name is {self.name}")


# ##creating the object 
# animaltype = dog(name = "rohu")

# print(animaltype.display())       ##This will print the same class method

# print(animaltype.eat())

# ##Practise 2

# ##Creating the super class
# class university():

#     ##Creating the object constructor
#     def __init__(self):
#         self.universityname = "Poornima"
#         self.courses = "Bac"
#         self.ranking = 19
    
#     ##method to print the details of the object
#     def screenview(self):
#         return f"This is your entire result. University Name:-{self.universityname} University Courses:-{self.courses} University Ranking:- {self.ranking}"
    

# class studentdetails(university):

#     ##creating the object constructor
#     def __init__(self,studentname,studentemail,studentcontact):
#         super().__init__()
#         self.studentname = studentname
#         self.studentemail = studentemail
#         self.studentcontact = studentcontact
    
#     ##Method to print the details of the object
#     def display(self):
#         return f"This is your details of student. Name:-{self.studentname} Email_Address:- {self.studentemail} Contact Number {self.studentcontact}"
    


# ##first create the object for the student details

# student = studentdetails("Mohan","mohan@gmail.com",9468252525)

# print(student.studentname)
# print(student.studentemail)
# print(student.studentcontact)

# print(student.screenview())
# print(student.display())


##Practise 3 
class Carmanufacture:               ##Parent Classs
    def __init__(self) -> None:         ##Here i have created a constructor
        self.carsize = "15foot"
        self.carwindshield = True
        self.cartire = "15*4"

    def assamblingdetails(self):
        return f"First paint the car then only you can continue with another process"

class Toyota(Carmanufacture):           ##Sub Class for the toyota Brand (Inheritance Level 1)

    def __init__(self,modelname) -> None:
        super().__init__()
        self.modelname = modelname


class Fortuner(Toyota):             ##Sub Class for the Fortuner model (Inheritance Level 2)
    def __init__(self,modelname,color,size,price) -> None:
        super().__init__(modelname)
        self.color = color
        self.size = size
        self.price = price
    
    ##Creating a method for the class
    def display(self):
        return f"This is your entire details of the fortuner car {self.color} {self.size} {self.price}" 


car1 = Fortuner("Fortuner","black",15,15000000)

print(car1.assamblingdetails())     ##Calling the class from the above item

print(car1.display())