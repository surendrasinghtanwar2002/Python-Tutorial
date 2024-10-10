# Intermediate Class Decorator Concepts
# Decorating the Constructor (__init__)
# You can also modify the class constructor (__init__) using a class decorator.
# This is useful when you want to add behavior during object initialization, such as logging, validation, or modifying attributes.


def Decorator(cls):
    original_init = cls.__init__                    ##Taking constructor variable from the original class (Person)

    def new_init(self,*args,**kwargs):
        print(f"Initializing: {cls.__name__} with arguments: {args} {kwargs}")
        original_init(self,*args,**kwargs)
    
    cls.__init__ = new_init                         ##In this we are passing the new argument to the original argument
    return cls                                      ##Returning the class

@Decorator
class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age

    def person_details(self):
        return f"Person name is {self.name} and person name is {self.age}"


def main():
    t1= Person(name="Surendra",age=28)
    print(t1.person_details())

##Calling the main function
if __name__ == "__main__":
    main()
