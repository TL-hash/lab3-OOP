import pytest
from lab3_oop.tasks.task1 import make_area, Figure


def test_make_area_triangle():
    func = make_area(type=0)
    assert func(6, 4) == 12.0


def test_make_area_rectangle():
    func = make_area(type=1)
    assert func(5, 3) == 15


def test_make_area_default():
    func = make_area()
    assert func(10, 2) == 10.0


def test_figure_area():
    triangle = Figure(6, 4)
    rectangle = Figure(5, 3, 1)
    assert triangle.area == 12.0
    assert rectangle.area == 15


def test_figure_add():
    triangle = Figure(6, 4)
    rectangle = Figure(5, 3, 1)
    assert triangle + rectangle == 27.0


def test_figure_comparisons():
    triangle = Figure(6, 4)
    rectangle = Figure(5, 3, 1)

    assert not (triangle == rectangle)
    assert triangle != rectangle
    assert triangle < rectangle
    assert not (triangle > rectangle)
    assert triangle <= rectangle
    assert not (triangle >= rectangle)
