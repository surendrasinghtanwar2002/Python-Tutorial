                            ## Overriding the built in function of the python Part 3## 

#The __add__ method allows you to define the behavior of the addition operator (+) for instances of your class.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
print(v3)  # Outputs: Vector(7, 10)
