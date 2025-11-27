import pytest
from src.factorial_fibonachi import (factorial_default,
                                     factorial_recursive,
                                     fibonachi_default,
                                     fibonachi_recursive)

def test_factorial_default():
    """Проверяет итеративную функцию факториала."""
    assert factorial_default.factorial_default(5) == 120
    assert factorial_default.factorial_default(1) == 1
    assert factorial_default.factorial_default(0) == 1

def test_factorial_recursive():
    """Проверяет рекурсивную функцию факториала."""
    assert factorial_recursive.factorial_recursive(5) == 120
    assert factorial_recursive.factorial_recursive(1) == 1
    assert factorial_recursive.factorial_recursive(0) == 1

def test_fibonachi_default():
    """Проверяет итеративную функцию Фибоначчи."""
    assert fibonachi_default.fibonachi_default(0) == 0
    assert fibonachi_default.fibonachi_default(1) == 1
    assert fibonachi_default.fibonachi_default(2) == 1
    assert fibonachi_default.fibonachi_default(3) == 2
    assert fibonachi_default.fibonachi_default(7) == 13

def test_fibonachi_recursive():
    """Проверяет рекурсивную функцию Фибоначчи."""
    assert fibonachi_recursive.fibonachi_recursive(0) == 0
    assert fibonachi_recursive.fibonachi_recursive(1) == 1
    assert fibonachi_recursive.fibonachi_recursive(2) == 1
    assert fibonachi_recursive.fibonachi_recursive(3) == 2
    assert fibonachi_recursive.fibonachi_recursive(7) == 13