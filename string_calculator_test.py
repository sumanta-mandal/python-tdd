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

def test_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//|\n3|4|5") == 12
    assert add("//#\n10#20#30") == 60
    assert add("//@\n2@3@4") == 9

def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1,-2"):
        add("-1,-2")

    with pytest.raises(ValueError, match="negative numbers not allowed: -5,-3"):
        add("1,-5,2,-3")
        
    with pytest.raises(ValueError, match="negative numbers not allowed: -4,-2"):
        add("//;\n1;-4;3;-2")

def test_more_than_1000_sum():
    assert add("1,1001") == 1
    assert add("2,1002,567,8765") == 569
    assert add("1234,1001") == 0

def test_test_custom_delimiter_any_length():
    assert add("//[***]\n1***2***3") == 6
    assert add("//[;;]\n1;;2;;3") == 6
    assert add("//[%%%%]\n1%%%%2%%%%3") == 6

def test_test_custom_multiple_delimiter():
    assert add("//[*][%]\n1*2%3") == 6
    assert add("//[***][##]\n1***2##3") == 6
