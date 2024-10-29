import pytest
from calculator import Calculator
calculator=Calculator()

def test_add():
    assert calculator.add(2,3)== 5

def test_subtract():
    assert calculator.subtract(5,4)== 1

def test_multiply():
    assert calculator.multiply(5,7)== 35

def test_divide():
    assert calculator.divide(6,2)== 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)
