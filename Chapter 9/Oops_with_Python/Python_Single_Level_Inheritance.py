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


# ##Practise 3 
# class Carmanufacture:               ##Parent Classs
#     def __init__(self) -> None:         ##Here i have created a constructor
#         self.carsize = "15foot"
#         self.carwindshield = True
#         self.cartire = "15*4"

#     def assamblingdetails(self):
#         return f"First paint the car then only you can continue with another process"

# class Toyota(Carmanufacture):           ##Sub Class for the toyota Brand (Inheritance Level 1)

#     def __init__(self,modelname) -> None:
#         super().__init__()
#         self.modelname = modelname


# class Fortuner(Toyota):             ##Sub Class for the Fortuner model (Inheritance Level 2)
#     def __init__(self,modelname,color,size,price) -> None:
#         super().__init__(modelname)
#         self.color = color
#         self.size = size
#         self.price = price
    
#     ##Creating a method for the class
#     def display(self):
#         return f"This is your entire details of the fortuner car {self.color} {self.size} {self.price}" 


# car1 = Fortuner("Fortuner","black",15,15000000)

# print(car1.assamblingdetails())     ##Calling the class from the above item

# print(car1.display())



# ##Practise 4
# # ##Creating the parent class
# class Transport:
#     def __init__(self, transport_brand, vehicle_type):
#         self.transport_brand = transport_brand
#         self.vehicle_type = vehicle_type
    
#     def transport_info(self):
#         return f"Transport Brand: {self.transport_brand}, Vehicle Type: {self.vehicle_type}"

##Creating another class or subclass which will inherit the functionalities from the parent class
# class Car(Transport):
#     def __init__(self, car_name, car_color, car_year):
#         # Using super() to call the parent class constructor to initialize parent class attributes
#         super().__init__(car_name, car_color)  # Initializes attributes from Transport class
#         # Attribute specific to the Car class
#         self.car_year = car_year  
    
#     def car_info(self):
#         return f"{super().transport_info()}, Car Manufacture Year: {self.car_year}"

# # Creating an instance of the Car class
# my_car = Car("Toyota", "Sedan", 2020)

# # Displaying information
# print(my_car.transport_info()) 
# print(my_car.car_info())  

                                                                    # Practise 5 ##
#Parent Class
class Transport:
    def __init__(self,manufacturer,engine_type) -> None:
        self.manufacturer = manufacturer
        self.engine_type = engine_type
    
    # @staticmethod               ##iT WILL BE DECORATER WHICH NOT REQUIRED ANY DETAILS
    def transport_info(self):
        return f"This is the Transportation service your manufactures is:- '{self.manufacturer}' and your engine type is '{self.engine_type}'"

#Child Class
class car(Transport):
    def __init__(self,manuf,types,year) -> None:            ##Constructor
        super().__init__(manuf,types)                       ##Here we are using the parent constructor attributes
        self.year = year
        
    def car_dispaly(self):
        return f"->>>>>>>>>>{super().transport_info()} Manufacturer Year '{self.year}' "
    

# ##creating the object for the class
# Fortuner = car("Toyota","Deisel",2024)

# ##printing the methods of the car class (Child Class)
# print(Fortuner.car_dispaly())

# ##printing the methods of the transport (Parent Class)
# print(Fortuner.transport_info())


                                                                    ## Practise 5 ##
##Primary class
class Animal:
    def eats(self):
        print("I can eat")

##Secondary Class
class dog(Animal):
    
    ##method for the object
    def eat(self):
        super().eats()
        print("I like to eat bones")

labrador = dog() ##creating an object of the subclases

labrador.eat()



        
        

        

