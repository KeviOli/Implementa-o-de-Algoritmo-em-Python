# test_list_sorter.py
import pytest
from list_sorter import ascending_order, descending_order

def test_ascending_order():
    assert ascending_order([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert ascending_order([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ascending_order([2, 4, 6, 8, 10, 12, 14, 16, 18]) == [2, 4, 6, 8, 10, 12, 14, 16, 18]

def test_descending_order():
    assert descending_order([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [9, 6, 5, 5, 4, 3, 2, 1, 1]
    assert descending_order([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert descending_order([2, 4, 6, 8, 10, 12, 14, 16, 18]) == [18, 16, 14, 12, 10, 8, 6, 4, 2]
