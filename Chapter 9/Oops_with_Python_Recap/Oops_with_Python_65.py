            ## In this section we will create a new method through out the decorater and inject into the class method ##


## This is our decorater
def decorater(cls):
    cls.greeting = "Hello"                  ## In this we are adding a class attributes

    def welcome_message(self):              ##Creating a new method
        print("This method is being created through out the decorater")
        return cls.greeting
    
    cls.hello = welcome_message             ##Assiging new method to the class
    
    return cls                              ## Return the actual class 

##This is our actual class
@decorater
class myhello:
    def __init__(self) -> None:
        pass

def main():
    t1 = myhello()
    print(t1.hello())

if __name__ == "__main__":
    main()
