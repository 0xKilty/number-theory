import pytest


def add(x, y):
    return x + y

def test_addition():
    assert add(1, 2) == 3

def test_addition_negative():
    assert add(-1, 1) == 0

def test_addition_float():
    assert add(0.1, 0.2) == pytest.approx(0.3)
