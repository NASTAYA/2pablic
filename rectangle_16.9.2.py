class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f'Прямоугольник (ширина = {self.width}, высота = {self.height}, площадь = {self.get_area()})'


rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1)
print(rect_2)






