                                                    ## In this section we will pracitse the multiple Inheritance Level ##

class A:
    def __init__(self) -> None:
        print("A class Constructor called")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("B class Constructor called")

class C (A):
    def __init__(self) -> None:
        super().__init__()
        print("C class Constructor Called")

class D (B,C):
    def __init__(self) -> None:
        super().__init__()
        print("D class constructor called")


##Creating the instance or object
obj1 = D()
