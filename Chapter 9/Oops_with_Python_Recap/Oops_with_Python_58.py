                                            ## in this section we will make the class decorator in python ##
from typing import Any

##Creating a class decorator
class Logger:
    def __init__(self,func) -> None:
        self.func = func
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f"Function name is '{self.func.__name__}' and their Arguments: {args} & keyword arguments is {kwds}")
        result = self.func(*args,**kwds)
        return result

##Creating a function where a class decorator will being applied
@Logger
def greet(age:int,name:str):
    return(f"Hello Mr sir {name}")

#Creating the main function
def main():
    print(greet(24, name="Surendra"))

if __name__ == "__main__":
    main()
    