class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
       return f'Rectangle(width = {self.width}, height ={self.height})'


class Square:
    def __init__(self, w):
        self.width = w

    def __str__(self):
        return f'Square(width = {self.width}, height ={self.width})'


class Circle:
    def __init__(self, r):
        self.radius = r

    def __str__(self):
        return f'Circle(radius = {self.radius})'


class Par_d:
    def __init__(self, w, ln, h):
        self.width = w
        self.length = ln
        self.height = h

    def __str__(self):
        return f'Parallelepiped(width = {self.width}, length = {self.length}, height = {self.height})'


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








