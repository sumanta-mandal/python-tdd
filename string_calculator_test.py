import pytest
from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_return_sum():
    assert add("1,2") == 3

def test_multiple_numbers_return_sum():
    assert add("1,2,3,4") == 10

def test_newline_as_delimiter_one():
    assert add("1\n2,3") == 6

def test_newline_as_delimiter_two():
    assert add("5\n7,3") == 15