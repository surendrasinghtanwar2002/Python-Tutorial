from time import time

def Logger(cls):
    # This function will modify the methods of the class passed to it
    for attr in dir(cls): # Loop through all attributes of the class
        if callable(getattr(cls, attr)) and not attr.startswith("__"):
            # Check if the attribute is callable (i.e., a method) and does not start with "__"
            original_method = getattr(cls, attr) # Get the original method

            def new_method(self, *args, **kwargs):  # Only *args and **kwargs
                print(f"Calling {cls.__name__}.{attr} with arguments {args} and {kwargs}")
                start_time = time()
                result = original_method(self, *args, **kwargs) # Call the original method
                end_time = time()
                print(f"Finished {cls.__name__}.{attr} in {end_time - start_time:.4f} seconds")
                return result

            setattr(cls, attr, new_method) # Replace the original method with the new method
    return cls

@Logger
class Calculator:
    def __init__(self, first_value: int | float, second_value: int | float) -> None:
        self.first_value = first_value
        self.second_value = second_value
        self.total = None
    
    def add(self):
        self.total = self.first_value + self.second_value
        return self.total
    
    def subtraction(self):
        self.total = self.first_value - self.second_value
        return self.total

def main():
    t1 = Calculator(first_value=20, second_value=45)
    print(t1.add())
    print(t1.subtraction())

if __name__ == "__main__":
    main()
