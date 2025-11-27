import pytest

import random

from src.sort_algs import (bubble_sort,
                           quick_sort,
                           counting_sort,
                           radix_sort,
                           bucket_sort,
                           heap_sort)

from src.test_cases.test_cases import (rand_int_array,
                                       rand_float_array)

def test_bubble_sort():
    """Проверяет сортировку выбором."""
    lst = rand_int_array(100, -1000, 1000)
    lst_default = sorted(lst)
    lst_reverse = sorted(lst, reverse=True)
    assert bubble_sort.bubble_sort(lst.copy()) == lst_default
    assert bubble_sort.bubble_sort(lst.copy(), cmp="reverse") == lst_reverse

def test_quick_sort():
    """Проверяет быструю сортировку."""
    lst = rand_int_array(100, -1000, 1000)
    lst_default = sorted(lst)
    lst_reverse = sorted(lst, reverse=True)
    assert quick_sort.quick_sort(lst.copy()) == lst_default
    assert quick_sort.quick_sort(lst.copy(), cmp="reverse") == lst_reverse

def test_counting_sort():
    """Проверяет сортировку подсчётом."""
    lst_negative = rand_int_array(100, -1000, 1000)
    lst_positive = rand_int_array(100, 1, 1000)
    test_lst_negative = sorted(lst_negative)
    test_lst_positive = sorted(lst_positive)
    assert counting_sort.counting_sort(lst_negative.copy()) == test_lst_negative
    assert counting_sort.counting_sort(lst_positive.copy()) == test_lst_positive

def test_radix_sort():
    """Проверяет поразрядную сортировку."""
    lst = [''.join(random.choice("0123456789ABCDEF") for _ in range(5)) for _ in range(100)]
    test_lst = sorted(lst)
    assert radix_sort.radix_sort(lst.copy(), base=16) == test_lst

def test_bucket_sort():
    """Проверяет блочную сортировку."""
    lst = rand_float_array(100, 0, 10)
    test_lst = sorted(lst)
    assert bucket_sort.bucket_sort(lst.copy()) == test_lst

def test_heap_sort():
    """Проверяет пирамидальную сортировку."""
    lst = rand_int_array(100, -1000, 1000)
    lst_default = sorted(lst)
    lst_reverse = sorted(lst, reverse=True)
    assert heap_sort.heap_sort(lst.copy()) == lst_default
    assert heap_sort.heap_sort(lst.copy(), cmp="reverse") == lst_reverse
