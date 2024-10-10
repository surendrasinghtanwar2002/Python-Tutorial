                                ## in this section we will make the class decorator in python ##

from time import time
from typing import Any

class TimeDecorator:
    def __init__(self,func:Any) -> None:
        self.func = func
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        start_timer = time()
        result = self.func(*args,**kwargs)
        end_timer = time()
        print(f"Function {self.func.__name__} executed in {end_timer - start_timer} seconds")
        return result

@TimeDecorator
def hello():
    try:
        counter = 0
        for i in range(1000000):
            counter += i
        return counter
    except Exception as e:
        print("Erroor",e)


def main():
    result = hello()
    print(f"This is total counter occured in the function loop {result}")

if __name__ == "__main__":
    main()

