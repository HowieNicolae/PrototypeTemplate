from calculator import add, subtract, multiply, divide


def test_add():
    a = 73
    b = 42
    c = 9  # change this to 10
    assert add(a, b) == 115
    assert add(a, c) == 82
    assert add(b, c) == 51


def test_subtract():
    a = 73
    b = 42
    c = 9  # change this to 10
    assert subtract(a, b) == 31
    assert subtract(a, c) == 64
    assert subtract(b, c) == 33


def test_multiply():
    a = 73
    b = 42
    c = 9  # change this to 10
    assert multiply(a, b) == 3066
    assert multiply(a, c) == 657
    assert multiply(b, c) == 378


def test_divide():
    a = 73
    b = 42
    c = 9  # change this to 10
    assert divide(a, b) == 1.7380952380952381
    assert divide(a, c) == 8.111111111111111
    assert divide(b, c) == 4.666666666666667
