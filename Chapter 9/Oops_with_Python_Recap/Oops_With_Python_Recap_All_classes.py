#                             ## Type of Constructor Practise ## (Parameterized Constructor,Non Parameterised Constructor) ##

# ## Non Parameterized Constructor ##
# class My_First_Class:
#     def __init__(self) -> None:
#         self.name = "Surendra"
#         self.age = 24
#         self.College_name = "Poornima University"

# class My_Second_Class(My_First_Class):
#     def __init__(self) -> None:
#         super().__init__()
#         self.username= "admin@gmail.com"
#         self.password = "hackerzone"
    
#     def display(self):
#         return{
#             "Name":self.name,
#             "Age":self.age,
#             "College_name":self.College_name,
#             "username": self.username,
#             "password":self.password
#         }

# ##Creating the instance
# d1 = My_Second_Class()
# print(d1.display())

# ## Non Parametrized Constructor overiding ##
# class Parent_Class:
#     def __init__(self) -> None:
#         self.name = "Hariom"
#         self.age = 24
#         self.college_name = "Poornima University"

# class Child_Class(Parent_Class):
#     def __init__(self) -> None:
#         self.name = "Surendra"
#         self.age = 28
#         self.college_name = "JECRC UNIVERSITY"
#     def display(self):
#         return {
#             "username":self.name,
#             "age":self.age,
#             "college_name":self.college_name
#         }

# ##Creating the instance 
# instance = Child_Class()
# print(instance.display())

# ## Non parametrized Constructor ##
# class Parent1:
#     def __init__(self) -> None:
#         self.name = "Surendra"
#         self.age = 24
#         self.college_name = "Poornima University"


# class Subclass(Parent1):
#     def __init__(self) -> None:
#         super().__init__()
#         pass


# ##Creating the instance for the subclass
# t1 = Subclass()
# print(t1.__dict__)



# ## Parameterized Constructor ##
# class Parent2:
#     def __init__(self,name:str,age:int,contact_no:int) -> None:
#         self.name = name
#         self.age = age
#         self.contact_no = contact_no
    
#     def display(self):
#         return {
#             "Name":self.name,
#             "Age":self.age,
#             "Contact No":self.contact_no
#         }

# class Child_Class(Parent2):
#     def __init__(self, name: str, age: int, contact_no: int) -> None:
#         super().__init__(name=name, age=age, contact_no=contact_no)

# ##Creating the instance or object
# t1 = Child_Class(name="Surendra",age=29,contact_no=9460824001)
# print(t1.display())

# ##Creating the instance or object
# t2 = Child_Class(name="Harish Parmani",age=24,contact_no=825252424)
# print(t2.display())
# print(getattr(t2,"name"))
# print(getattr(t2,"age"))
# print(getattr(t2,"contact_no"))


# print(getattr(t1,"name"))
# print(getattr(t1,"age"))
# print(getattr(t1,"contact_no"))



## Parameterized Constructor ## 
class Netmiko_connection:
    netmiko = False
    def __init__(self) -> None:
        pass
    ##Method for performing the action
    @classmethod
    def netmiko_connection_changer(cls):
        cls.netmiko = True
        return cls.netmiko
    
class Command_Send(Netmiko_connection):
    def __init__(self) -> None:
        super().__init__()
    
    def send_command(self):
        if self.netmiko:
            print("Sorry netmiko connection is True We are ready to go")
        else:
            self.netmiko_connection_changer()
            if self.netmiko:
                print("Now your connection is True you can proceed")
            else:
                print(f"Still your connection is not True you can proceed {self.netmiko}")

class Result(Command_Send):
    def __init__(self) -> None:
        super().__init__()
        pass


t1 = Command_Send()
t1.send_command()

##Creating new instance of the result 
t5 = Result()
print(t5.netmiko)


## Accessing parent class class attributes without inheritance ##
class Parent_Class:
    netmiko_connection = "Hello you have got the netmiko connection object"
    def __init__(self) -> None:
        pass
    
    @classmethod
    def netmiko_replacer(cls,value):
        cls.netmiko_connection=value
        return cls.netmiko_connection


class Subclasses:
    def __init__(self) -> None:
        self.netmiko = None

    def Netmiko_connection(self):
        # parent = Parent_Class.netmiko_connection       ##Creating the parent instance
        netmiko_new_object = True
        Parent_Class.netmiko_replacer(value=netmiko_new_object)
        return Parent_Class.netmiko_connection
    
t11 = Subclasses()
print(t11.Netmiko_connection())

## Accessing the 
