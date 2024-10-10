                                                ## In this section we will practise the create a class decorator that modifies the behavior of the existing class ##


##This is the decorater
def decorater(cls):
    class new_changes(cls):             ##This will change the existing class method
        def __int__(self):
            pass
        def hello(self):                ##In this step it overiding its parent class method and creating a new class method
            new_message = "My name is Surendra I am printing..."
            original_message = super().hello()
            return f"This is New message {new_message}  {original_message}"
    return new_changes


##Parent Class
@decorater
class Greeting:
    def __init__(self) -> None:
        pass

    def hello(self):
        return "Hello world"
    
def main():
    t1 = Greeting()
    print(t1.hello())


if __name__ == "__main__":
    main()
