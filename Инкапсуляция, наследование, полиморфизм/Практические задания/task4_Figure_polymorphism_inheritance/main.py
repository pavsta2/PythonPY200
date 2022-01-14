import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

    def __init__(self, a, b):
        self.a = a  # определить конструктор и перегрузить метод area
        self.b = b

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return self.a * self.b



class Circle(Figure):
    """ Производный класс. Круг. """
    PI = 3.14

    def __init__(self, r):
        self.r = r   #определить конструктор и перегрузить метод area

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return self.PI * self.r * 2


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
