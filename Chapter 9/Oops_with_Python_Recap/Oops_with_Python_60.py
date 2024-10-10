                         ## in this section we will make the class decorator in python ##

from typing import Any

##Creating the class decorator
class Mydecorator():
    def __init__(self,func) -> None:
        self.func = func
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if kwargs.get("error",False):
            raise ValueError("Your function have some kind of error")
        return self.func(*args,**kwargs)

##Creating the function
@Mydecorator
def data_process(data,error=False):
    return f"Your data {data} is being processing"

def main():
    try:
        print(data_process("sample data"))
        print(data_process("sample data",error =True))
    except Exception as e:
        print(f"This is the exception {e}")

if __name__ =="__main__":
    main()


