                                                                    ## In this section we have created a decorater for the class ##
def Decorater(cls):
    class MySecondStage(cls): 
        def __int__(self):
            super().__init__()
        
        def helloworld(self):
            print("We have added decortater above the class")
            super().helloworld()
            print("After the added decorater to the class")
    return MySecondStage

@Decorater
class MyDecorator:
    def __init__(self) -> None:
        pass

    def helloworld(self):
        print("Hello world")


def main():
    t1 = MyDecorator()
    t1.helloworld()

if __name__ == "__main__":
    main()

