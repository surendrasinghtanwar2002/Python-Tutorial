from abc import ABC, abstractmethod


class Hello(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def greeting(self):
        pass

    @abstractmethod
    def goodnight(self):
        pass

class MyHello(Hello):
    def __init__(self) -> None:
        super().__init__()
    
    def greeting(self):
        print("Hello world")
    
    def goodnight(self):
        print("Good Night all")
    
def main():
    t1 = MyHello()
    t1.greeting()
    t1.goodnight()


if __name__ == "__main__":
    main()