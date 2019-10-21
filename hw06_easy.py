__author__ = "Гончаров Всеволод Сергеевич"

import math


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Side:

    def __init__(self, point_A: Point, point_B: Point):
        self.A = point_A
        self.B = point_B
        self._Len = None

    def __str__(self):
        return str(self.Len)

    @property
    def Len(self):
        if not self._Len:
            self._Len = round(math.sqrt(((self.B.x - self.A.x) ** 2) + ((self.B.y - self.A.y) ** 2)), 4)
        return self._Len


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.AB = Side(Point(x1, y1), Point(x2, y2))
        self.BC = Side(Point(x2, y2), Point(x3, y3))
        self.CA = Side(Point(x3, y3), Point(x1, y1))
        self._P = None
        self._S = None

    @property
    def P(self):
        if not self._P:
            self._P = self.AB.Len + self.BC.Len + self.CA.Len
        return self._P

    def get_height(self, side):
        return round((math.sqrt(self.P * (self.P - self.AB.Len) * (self.P - self.BC.Len) * (self.P - self.CA.Len)))
                     * 2 / side.Len, 4)

    @property
    def S(self):
        if not self._S:
            self._S = round(self.AB.Len * self.get_height(self.AB) * 0.5, 4)
        return self._S


def create_Triangle():
    return Triangle(1, 1, 3, 5, 5, 1)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.AB = Side(Point(x1, y1), Point(x2, y2))
        self.BC = Side(Point(x2, y2), Point(x3, y3))
        self.CD = Side(Point(x3, y3), Point(x4, y4))
        self.DA = Side(Point(x4, y4), Point(x1, y1))
        self._P = None
        self._H = None
        self._S = None

    def it_is_trapezoid(self):
        if self.BC.A.y == self.BC.B.y and self.DA.A.y == self.DA.B.y:
            return True if self.AB.Len == self.CD.Len else False
        return False

    @property
    def H(self):
        if not self._H:
            self._H = math.sqrt(self.AB.Len ** 2 -
                                ((((self.DA.Len - self.BC.Len) ** 2) + self.AB.Len ** 2 - self.CD.Len ** 2)
                                 / (2 * (self.DA.Len - self.BC.Len))) ** 2)
        return self._H

    @property
    def P(self):
        if not self._P:
            self._P = self.AB.Len + self.BC.Len + self.CD.Len + self.DA.Len
        return self._P

    @property
    def S(self):
        if not self._S:
            self._S = round(self.BC.Len + self.DA.Len * self.H / 2, 4)
        return self._S


def create_Trapezoid():
    return Trapezoid(1, 1, 2, 3, 4, 3, 5, 1)


def main():
    while True:
        print("Введи номер задачи (1-2) или 0 для выхода")
        key = int(input())

        if key == 1:
            triangle = create_Triangle()
            print("Периметр: {}\nВысоты сторон:\nAB: {}\nBC: {}\nCA: {}\nПлощадь: {}".
                  format(triangle.P, triangle.get_height(triangle.AB), triangle.get_height(triangle.BC),
                         triangle.get_height(triangle.CA), triangle.S))
        if key == 2:
            trapezoid = create_Trapezoid()
            if trapezoid.it_is_trapezoid():
                print("Это равнобочная трапеция\nДлины сторон:\nAB: {}\nBC: {}\nCD: {}\nDA: {}\nПериметр: {}\n"
                      "Площадь: {}".format(trapezoid.AB, trapezoid.BC, trapezoid.CD, trapezoid.DA, trapezoid.P,
                                           trapezoid.S))
            else:
                print("Фигура не является равнобочной трапецией")
        elif key == 0:
            break
        else:
            print("Некорректный ввод")


if __name__ == "__main__":
    main()
