                                                    ## in this section we will make the class decorator in python ##
from typing import Any


class DoubleReturnDecorator:
    def __init__(self,function) -> None:
        self.function = function
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"We are calling the decorator for the function:- '{self.function.__name__}' ")
        result = self.function(*args,**kwargs)
        return result*2                         ##It will first get the result of the actual function and then *2 to the result of the function

##Function
@DoubleReturnDecorator
def addition(first_Value,second_value):
    try:
        result = first_Value+second_value
        print(f"The actual result of the function is {result}")
        return result
    except Exception as e:
        print(f"This is the exception of the function",e)
        return False

def main():
    result = addition(first_Value=10,second_value=20)
    print(result)

if __name__ == "__main__":
    main()