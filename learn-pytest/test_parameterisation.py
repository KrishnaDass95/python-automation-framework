"""
Test parametrization is a powerful feature in pytest that allows you to run the same test with multiple sets of inputs.
 This is particularly useful when you want to test a function or method with various input values and ensure 
its correctness across different scenarios. Let's dive into test parametrization:
"""

import pytest

@pytest.mark.parametrize("input, expected", [(1,2), (2,3)])
def test_increment(input, expected):
    assert input + 1 == expected



@pytest.mark.parametrize("input, output", [(2, 1), (3,2)])
def test_decrement(input, output):
    assert input - 1 == output

# you can also combine parameterisation with fixtures
    
def calculate_rect_area(length, width):
    return length * width

# use a fixture to provide the test case with different values

@pytest.fixture(params=[(1,2), (2, 3)])
def rectangle_dimensions(request):
    return request.param


def test_area_calc(rectangle_dimensions):
    length, width = rectangle_dimensions
    calc_area = calculate_rect_area(length, width)
    except_area = length * width
    assert calc_area == except_area
    