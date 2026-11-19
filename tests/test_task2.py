import pytest
from lab3_oop.tasks.task2 import Rational, MAX_SIZE


def test_rational_creation():
    r = Rational("3/4")
    assert str(r) == "3/4"
    assert r.size() == MAX_SIZE

    r_custom = Rational("1/2", size=10)
    assert r_custom.size() == 10


def test_rational_arithmetic():
    r1 = Rational("3/4")
    r2 = Rational("5/6")

    assert str(r1 + r2) == "38/24"

    assert str(r1 - r2) == "-2/24"

    assert str(r1 * r2) == "15/24"

    assert str(r1 / r2) == "18/20"


def test_rational_comparisons():
    r1 = Rational("3/4")
    r2 = Rational("5/6")

    assert (r1 == r2) is False
    assert (r1 != r2) is True
    assert (r1 < r2) is True
    assert (r1 > r2) is False


def test_rational_indexing():
    r = Rational("123/456")

    assert r[0] == 3
    assert r[1] == 2
    assert r[2] == 1


def test_rational_setitem():
    r = Rational("123/456")
    r[0] = 9
    assert str(r) == "129/456"