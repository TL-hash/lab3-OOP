#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 1 (вариант 7).

Используя замыкания функций, объявить внутреннюю функцию, которая на основе 
двух параметров вычисляет площадь фигуры. Какой именно фигуры: треугольника 
или прямоугольника, определяется параметром type внешней функции. Если type 
принимает значение 0, то вычисляется площадь треугольника, а иначе – прямоугольника. 
По умолчанию параметр type должен быть равен 0. Вычисленное значение должно 
возвращаться внутренней функцией. Вызвать внутреннюю функцию замыкания и 
отобразить на экране результат её работы.
"""


def make_area(type=0):
    def area(a, b):
        if type == 0:
            return 0.5 * a * b
        else:
            return a * b

    return area


class Figure:
    def __init__(self, a, b, type=0):
        self.type = type
        self.area_func = make_area(type)
        self.area = self.area_func(a, b)

    #сложение
    def __add__(self, other):
        return self.area + other.area

    #сравнение
    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area


if __name__ == '__main__':
    triangle = Figure(6, 4)
    rectangle = Figure(5, 3, 1)

    #вызов внутренней функции замыкания
    print("Площадь треугольника (6, 4):", triangle.area_func(6, 4))
    print("Площадь прямоугольника (5, 3):", rectangle.area_func(5, 3))

    print("triangle + rectangle =", triangle + rectangle)
    print("triangle == rectangle:", triangle == rectangle)
    print("triangle != rectangle:", triangle != rectangle)
    print("triangle < rectangle:", triangle < rectangle)
    print("triangle > rectangle:", triangle > rectangle)
    print("triangle <= rectangle:", triangle <= rectangle)
    print("triangle >= rectangle:", triangle >= rectangle)
