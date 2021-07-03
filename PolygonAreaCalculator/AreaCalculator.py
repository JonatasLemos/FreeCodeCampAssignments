class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect_string = "Rectangle Perimeter"

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return (self.width+self.height)*2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        stars = "*"*self.width
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            picture += stars + "\n"
        return picture

    def get_amount_inside(self, polygon):
        if polygon.height <= self.height and polygon.width <= self.width:
            return int(self.get_area()/polygon.get_area())
        return 0

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side):
        self.width = self.height = new_side