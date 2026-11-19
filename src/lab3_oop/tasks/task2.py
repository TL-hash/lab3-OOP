#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 2 (Вариант 7).

Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно
храниться максимальное для данного объекта количество элементов списка; реализовать
метод size(), возвращающий установленную длину. Если количество элементов списка
изменяется во время работы, определить в классе поле count. Первоначальные значения
size и count устанавливаются конструктором.
В тех задачах, где возможно, реализовать конструктор инициализации строкой.
Реализовать класс Rational, используя два списка из 100 элементов типа int для
представления числителя и знаменателя. Каждый элемент является десятичной цифрой.
Младшая цифра имеет меньший индекс (единицы — в нулевом элементе списка).
Реальный размер списка задается как аргумент конструктора инициализации.
"""

MAX_SIZE = 100  #максимально возможный размер списка


def int_to_list(number, size):
    digits = [0] * size
    i = 0
    while number > 0 and i < size:
        digits[i] = number % 10
        number = number // 10
        i += 1
    return digits


def list_to_int(digits):
    result = 0
    for i in range(len(digits) - 1, -1, -1):
        result = result * 10 + digits[i]
    return result


class Rational:
    def __init__(self, value="0/1", size=MAX_SIZE):
        if size > MAX_SIZE:
            size = MAX_SIZE
        if size < 1:
            size = 1
        self.max_size = size
        self.numerator = [0] * size
        self.denominator = [0] * size
        self.sign = 1
        self.count = 0

        parts = value.split("/")
        num = int(parts[0])
        if len(parts) == 2:
            den = int(parts[1])
        else:
            den = 1
        if den == 0:
            den = 1
        self.set_values(num, den)

    def size(self):
        return self.max_size

    def set_values(self, num, den):
        if num * den < 0:
            self.sign = -1
        else:
            self.sign = 1
        self.numerator = int_to_list(abs(num), self.max_size)
        self.denominator = int_to_list(abs(den), self.max_size)
        self.update_count()

    def update_count(self):
        n = len(str(list_to_int(self.numerator)))
        d = len(str(list_to_int(self.denominator)))
        self.count = max(n, d)

    def get_num(self):
        return list_to_int(self.numerator) * self.sign

    def get_den(self):
        return list_to_int(self.denominator)

    def make(self, num, den):
        return Rational(str(num) + "/" + str(den), self.max_size)

    def __str__(self):
        return str(self.get_num()) + "/" + str(self.get_den())

    def __getitem__(self, index):
        if index >= 0 and index < self.max_size:
            return self.numerator[index]
        return 0

    def __setitem__(self, index, value):
        if index >= 0 and index < self.max_size and value >= 0 and value <= 9:
            self.numerator[index] = value
            self.update_count()

    def __add__(self, other):
        a, b = self.get_num(), self.get_den()
        c, d = other.get_num(), other.get_den()
        return self.make(a * d + c * b, b * d)

    def __sub__(self, other):
        a, b = self.get_num(), self.get_den()
        c, d = other.get_num(), other.get_den()
        return self.make(a * d - c * b, b * d)

    def __mul__(self, other):
        a, b = self.get_num(), self.get_den()
        c, d = other.get_num(), other.get_den()
        return self.make(a * c, b * d)

    def __truediv__(self, other):
        a, b = self.get_num(), self.get_den()
        c, d = other.get_num(), other.get_den()
        if c == 0:
            print("Деление на ноль, результат не изменён")
            return self.make(a, b)
        return self.make(a * d, b * c)

    def compare(self, other):
        a, b = self.get_num(), self.get_den()
        c, d = other.get_num(), other.get_den()
        return a * d - c * b

    def __eq__(self, other):
        return self.compare(other) == 0

    def __lt__(self, other):
        return self.compare(other) < 0

    def __gt__(self, other):
        return self.compare(other) > 0

    def __le__(self, other):
        return self.compare(other) <= 0

    def __ge__(self, other):
        return self.compare(other) >= 0


if __name__ == '__main__':
    r1 = Rational("3/4")
    r2 = Rational("5/6")
    print("r1 =", r1)
    print("r2 =", r2)
    print("size() =", r1.size())
    print("count =", r1.count)

    print("r1 + r2 =", r1 + r2)
    print("r1 - r2 =", r1 - r2)
    print("r1 * r2 =", r1 * r2)
    print("r1 / r2 =", r1 / r2)

    print("r1 == r2:", r1 == r2)
    print("r1 != r2:", r1 != r2)
    print("r1 < r2:", r1 < r2)
    print("r1 > r2:", r1 > r2)
    print("r1 <= r2:", r1 <= r2)
    print("r1 >= r2:", r1 >= r2)

    r3 = Rational("123/457", 10)
    print("r3 =", r3, "size() =", r3.size(), "count =", r3.count)
    print("r3[0] =", r3[0], "r3[1] =", r3[1], "r3[2] =", r3[2])
    r3[0] = 9
    print("после r3[0] = 9:", r3)