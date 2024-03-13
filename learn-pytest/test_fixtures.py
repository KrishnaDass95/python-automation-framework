"""
Fixtures are functions that provide a baseline setup for your tests. 
They allow you to initialize resources, set up dependencies, or perform cleanup tasks before and after test execution. 
Fixtures play a crucial role in writing clean, maintainable, and reusable test code. Let's delve deeper into fixtures:
"""

"""
Fixtures are defined as regular Python functions decorated with @pytest.fixture.
They can be placed in test modules, conftest.py files, or imported from other modules.
Fixtures are invoked by mentioning their names as arguments to test functions that need them.
"""

import pytest

@pytest.fixture
def setup_data():
    data = {'name' : 'krishna', 'age' : 200}
    return data

# using the fixtures is done by using the funtion name of fixutre as an argument in the test
# Pytest automatically calls the fixture function and passes the return value to the test function.
def test_name(setup_data):
    assert setup_data["name"] == "krishna"


# scope of fixtures can be called on function level, class level, module level and session level
# fixtures are functions that are run before the test to set the test up and then clean afterwards
# they can run in different times based on scope mentioned


@pytest.fixture(scope="function")
def setup_name():
    return "Krishna"


def test_krishna(setup_name):
    assert setup_name == "krishna" , "name no match"


# fixtures can also have a teardown written in them, 
# Fixtures can perform setup tasks before the test and cleanup tasks after the test.
# You can use the yield statement to indicate the start and end of the fixture setup.
# Code after the yield statement serves as the teardown/cleanup logic.

@pytest.fixture
def setup_data_again():
    data = {"comapany" : "<H>"}
    yield data
    # teardown
    print("tearing down")



# fixtures can call other fixtures - known as fixture dependancy

@pytest.fixture()
def database_setup():
    # setup
    print("db setup")
    yield
    print("db teardown")


@pytest.fixture()
def user_setup(database_setup):
    print("user setup")
    yield
    print("user teardown")


@pytest.fixture()
def client_setup(database_setup, user_setup):
    print("cleint setup")

    yield
    print("client teardown")


def test_connections(client_setup):
    print(client_setup)


