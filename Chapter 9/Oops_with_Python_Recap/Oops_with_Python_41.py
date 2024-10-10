                                                ## In this section we will practise on the class abstraction ##

from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(cls) -> None:
        pass

    ##defining the methods here
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def order(self):
        pass

class Electronics(Product):
    def __init__(cls) -> None:
        pass

    def price(self):
        print("The price of the electronics gadets will be present here")
    
    def order(self):
        print("The price of the order will be presented here")

class Clothes(Product):
    def __init__(cls) -> None:
        pass

    def price(self):
        print("The price of the clothing will be present here")
    
    def order(self):
        print("The price of the clothing order will be presented here")

def main():
    t1 = Electronics()
    t1.price()
    t1.order()

    t2 = Clothes()
    t2.price()
    t2.order()


if __name__ == "__main__":
    main()
    





