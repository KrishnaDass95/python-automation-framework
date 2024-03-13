"""
Test discovery is the process by which pytest automatically finds and collects test functions and classes in your Python codebase. 
Pytest searches for tests based on certain conventions and configurations. Here's a detailed explanation of how test discovery works:

Default Search Pattern:
By default, pytest searches for test files using the following patterns:

Files starting with test_ (e.g., test_module.py).
Files ending with _test.py (e.g., module_test.py).
Pytest recursively searches for such files starting from the directory where it's invoked.
"""


# Pytest also supports organizing tests within test classes.
# Test classes should be named with a prefix of Test and contain test methods prefixed with test_. Pytest collects and executes these test methods.
import pytest


class TestCalculator:

    def test_add(self):
        assert 3 + 3 == 6

    def test_multiply(self):
        assert 10 * 10 == 100


    @pytest.mark.skip(reason="Temporarily skipped")
    def test_skip(self):
        print("I am skipped")


