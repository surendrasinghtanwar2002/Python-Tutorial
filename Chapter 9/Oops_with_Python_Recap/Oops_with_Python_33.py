                                                            ## Class Inheritance ## 

class Car:
    def __init__(self,make:str,model:str) -> None:
        self.make = make
        self.model = model
    
    class Engine:
        def __init__(self,horsepower) -> None:
            self.horsepower = horsepower
        
        def display_info(self):
            return f"Engine horsepower is {self.horsepower}"
    
    def display_info(self):
        return f"Car Model is {self.model}"
    


##Creating the instance
user_1 = Car(make="Maruti Suzuki",model="Maruti 800")
print(user_1.display_info())            ##Accessing outer class methods


##Creating instance of inner class 
Engine_Type = user_1.Engine(1500)
print(Engine_Type.display_info())       ##Accessing inner class methods 
