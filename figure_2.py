class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

class Square:
    def __init__(self, w):
        self.width = w

class Circle:
    def __init__(self, r):
        self.radius = r


class Par_d:
    def __init__(self, w, ln, h):
        self.width = w
        self.length = ln
        self.height = h


class Figure (Rectangle, Square, Circle, Par_d):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        if isinstance(self, Rectangle):
            return f'Rectangle(width = {self.width}, height ={self.height})'
        if isinstance(self, Square):
            return f'Square(width = {self.width}, height ={self.width})'
        if isinstance(self, Circle):
            return f'Circle(radius = {self.radius})'
        if isinstance(self, Par_d):
            return f'Parallelepiped(width = {self.width}, length = {self.length}, height = {self.height})'
        else:
            print(False)

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(8)
circle_2 = Circle(6)
par_1 = Par_d(3, 4, 5)
par_2 = Par_d(6, 10, 25)

print(rect_1)
print(square_2)
print(circle_2)