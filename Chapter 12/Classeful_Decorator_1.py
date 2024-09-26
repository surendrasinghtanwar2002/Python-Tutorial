                                                    ## From this section we will practise the classeful decorator ##


##Creating a decorator
def Decorater(cls):
    class wrapper(cls):
        def new(self):
            return"This is the new method of the class created by decorater"
    return wrapper


##Existing class
@Decorater
class Hello:
    def __init__(self) -> None:
        pass
    def original(self):
        return "This is the original method of the class"


##Main Function
def main():
    t1 = Hello()
    print(t1.new())
    print(t1.original())

##Calling the main function
if __name__ == "__main__":
    main()