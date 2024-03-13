import pytest

class TestAssertions:

    def test_assertions(self):
        # adding custom messages to denote failure
        assert len("hello") == 5, "length is not equal to 5"

    """
    Pytest also supports advanced assertions for checking data structures, collection contents, and more. 
    For example, assertDictEqual, assertListEqual, assertIn, assertNotIn, etc.Example:
    """
    def test_list_contains_element(self):
        my_list = [1, 2, 3, 4, 5]
        assert 3 in my_list 

        


