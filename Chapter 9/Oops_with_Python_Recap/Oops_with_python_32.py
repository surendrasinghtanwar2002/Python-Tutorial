class Shape:
    def area(self, radius: float) -> float:  # For circles
        return 3.14 * radius * radius

    def area(self, length: float, width: float) -> float:  # For rectangles
        return length * width

    def area(self, base: float, height: float) -> float:  # For triangles
        return 0.5 * base * height

# Example usage
shape = Shape()
print(shape.area(5))  # Circle with radius 5
print(shape.area(4, 6))  # Rectangle with length 4 and width 6
print(shape.area(3, 4))  # Triangle with base 3 and height 4
