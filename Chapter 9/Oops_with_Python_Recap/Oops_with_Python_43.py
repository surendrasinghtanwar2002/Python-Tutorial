from typing import Any


class Addition:
    def __init__(self,first_value) -> None:
        self.first_value = first_value

    def __call__(self, second_value:Any) -> Any:
        return self.first_value + second_value
    


##Creating the instance
t1 = Addition(10)

##Calling the object like a function
print(t1(80))