                            ## Overriding the built in function of the python Part 2## 

#The __len__ method allows you to define the behavior of the len() function for instances of your class.

class Shopping:
    def __init__(self,bucket1,bucket2,bucket3) -> None:
        self.clothes = bucket1
        self.electronics = bucket2
        self.other = bucket3
    
    def __len__(self):
        return len(self.clothes)+len(self.electronics)+len(self.other)


obj1 = Shopping(bucket1=["tshirt","shirt","jeans","cargo"],bucket2=["mobile","earphone","charger"],bucket3=["chair","charger"])

print(len(obj1))