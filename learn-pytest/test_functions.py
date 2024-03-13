"""
Pytest is a testing framework for Python that allows you to write simple and scalable test cases. 
It is widely used for testing Python code across various applications and domains. 
Pytest provides easy-to-use functionalities for writing tests, running them, and reporting results.
"""

# test files need to be named correctly too 

import pytest

"""
In pytest, tests are written as regular Python functions.
You can identify a test function by prefixing its name with test_ or by using the @pytest.mark decorator. 
Test functions should raise an assertion to indicate whether a test passes or fails.
"""
def test_addition():
    assert 1 + 1 == 2

# make sure you have an assertion at each test
def test_string_length():
    assert len("helllo") == 6


# use decorators to mark and group certain tests
@pytest.mark.smoke
def test_multiply():
    assert 2 * 2 == 4


