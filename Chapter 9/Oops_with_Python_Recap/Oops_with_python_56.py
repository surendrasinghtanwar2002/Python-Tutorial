def somethingfunction(cls):
    cls.extraattribute = "Added by the decorator"
    return cls

@somethingfunction
class Myclass:
    def __init__(self) -> None:
        self.myname = "Class instance"
        print("Class instance called here")


##Creating the instance of my class 
t1 = Myclass()
print(t1.extraattribute)

