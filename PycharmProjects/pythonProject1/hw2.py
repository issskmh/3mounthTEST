class Figure:
    unit = 'cm'
    def __init__(self):
        pass



    def calculate_area(self):
        print(F'calculated area: {self.unit}')

    def info(self):
        print(F'info about fugure calculated area:{self.calculate_area()},unit :{self.unit}')


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_area(self):
        if self == 'square' or 'Square':
            print(F' square\'s square{self.__side_length * 2}')

    def info(self):
        if self == 'square' or 'Square':
            print(F'information about {self}: side lenth: {self.__side_length}'
                  F'calculated area: {self.calculate_area()}')

class Rectangle(Figure):
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def calculate_area(self):
        if self == 'Rectangle' or 'rectangle':
          print(f'calculated area:{self.__lenght * self.__width}')

    def info(self):
        if self == 'Rectangle' or 'rectangle':
            print(F'information about {self}: side lenth: {self.__lenght}'
                  F'calculated area: {self.calculate_area()}')

shapes = [Square(4),
    Square(7),
    Rectangle(3,6),
    Rectangle(5,8),
    Rectangle(7,2)
]



for shape in shapes:
    shape.info()