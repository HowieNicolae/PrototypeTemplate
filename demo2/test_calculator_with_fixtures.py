from calculator import add, subtract, multiply, divide
import pytest


@pytest.fixture
def nums():
    a = 73
    b = 42
    c = 9  # change this to 10
    return a, b, c


def test_add(nums):
    a, b, c = nums
    assert add(a, b) == 115
    assert add(a, c) == 82
    assert add(b, c) == 51


def test_subtract(nums):
    a, b, c = nums
    assert subtract(a, b) == 31
    assert subtract(a, c) == 64
    assert subtract(b, c) == 33


def test_multiply(nums):
    a, b, c = nums
    assert multiply(a, b) == 3066
    assert multiply(a, c) == 657
    assert multiply(b, c) == 378


def test_divide(nums):
    a, b, c = nums
    assert divide(a, b) == 1.7380952380952381
    assert divide(a, c) == 8.111111111111111
    assert divide(b, c) == 4.666666666666667
    # what about div/0??
