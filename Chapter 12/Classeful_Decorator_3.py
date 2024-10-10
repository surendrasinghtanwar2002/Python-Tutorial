# Intermediate Class Decorator Concepts
# Decorating the Constructor (__init__)
# You can also modify the class constructor (__init__) using a class decorator.
# This is useful when you want to add behavior during object initialization, such as logging, validation, or modifying attributes.

def Decorater(cls):
    class Wrapper(cls):
        def __int__(self,*args,**kwargs):
            super().__int__(*args,**kwargs)
        
        def person_details(self):
            print("We are adding the wrapper above the method by Decorater")
            result= (super().person_details())
            print(result)
            print("We have added the wrapper below the method by Decorater")
    return Wrapper

@Decorater
class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age

    def person_details(self):
        return f"Person name is {self.name} and age is {self.age}"


def main():
    t1 = Person(name="Surendra",age=24)
    print(t1.person_details())

##Calling the main function
if __name__ == "__main__":
    main()