                            ## In this section we are practising the __call__ method in python ##

from typing import Any

class CachedMultiplication:
    def __init__(self) -> None:
        self.cahce={}
    
    def __call__(self,x:Any,y:Any) -> Any:
        if (x,y) not in self.cahce:
            print(f"Calculation {x} and {y}")
            self.cahce[(x,y)] = x * y
        return self.cahce[(x,y)]


##Creating the instance of the class
t1 = CachedMultiplication()

print(t1(x=10,y=20))
print(t1(x=10,y=20))

t2 = CachedMultiplication()
print(t2(x=10,y=20))