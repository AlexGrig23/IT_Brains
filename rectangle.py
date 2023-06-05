
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return f"square {self.length * self.width }"

    def perimeter(self):
        return f"perimeter {2 * (self.length+self.width)}"


rect = Rectangle(5, 10)
print(rect.square())
print(rect.perimeter())
