from calculator import add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(6, 7) == 13


def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
