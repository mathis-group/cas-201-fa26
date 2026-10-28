class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # def __str__(self):
    #     return f"A rectangle with dimensions ({self.length}, {self.width})"

    # def __add__(self, rect2):
    #     return Rectangle(self.length + rect2.length, self.width + rect2.width)
    
    def square(self):
        if self.length == self.width:
            return True
        else:
            return False

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*self.length + 2*self.width

rect1 = Rectangle(4,3)
print(f"rect1 is a square: {rect1.square()}")
rect2 = Rectangle(4, 4)
print(f"rect2 is a square: {rect2.square()}")
print(f"The area of rect2 is {rect2.area()}")
print(f"The perimeter of rect2 is {rect2.perimeter()}")
    