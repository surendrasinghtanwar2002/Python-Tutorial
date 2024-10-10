                                                ## Advanced Class Decorators with Method Overriding ##


def decorater(cls):
    print("Decorater will being applied here")
    new=  cls
    print("Decorater is being applied please wait")
    print(f"Let chec the object {new}")
    return new


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

    
