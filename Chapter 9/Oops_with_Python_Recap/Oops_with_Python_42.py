                                ## In this section we will practise the __call__ method in python ##

from typing import Any

class My_decorator:
    def __init__(self) -> None:
        pass
    def __call__(self, a:Any,b:Any) -> Any:
        print("We are calling the internal function of the object")
        c = a+b
        print(f"We have calculated the sum of two number")
        return c
    

##Creating the instance 
t1 = My_decorator()

# Calling the instance like a function
print(t1(10,20))