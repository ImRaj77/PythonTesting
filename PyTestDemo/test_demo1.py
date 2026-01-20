# Any pytest file should start with test_ or end _test
# test method names always starts with test
# -k stands for method names execution, -s stands for output, -v stands for more info metadata
# you can run tests with : python3 -m py.test <file_name> -v -s
# you can run tests with : python3 -m pytest <file_name> -v -s
# you can run tests with : python3 -m pytest -k <method-name> -v -s
# you can run tests with : python3 -m py.test -k <method-name> -v -s

# you can mark (tag) tests with @pytest.mark.smoke
# python3 -m pytest -m smoke -v -s    # @pytest.mark.smoke test execution
# @pytest.mark.skip --- It will skip the test case
# @pytest.mark.xfail
# fixtures are used as setup and teardown methods for test cases - write in conftest.py
# write in conftest.py file to generalize fixture and make it available for all the test cases.
# datadriven and parameterization can be done with return statements in tuple format
# When you define fixture scope to class only it will run once before class is initiated and at the end

import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    msg = "Hello"
    assert msg == "Hello", "Test failed because String do not match"

def test_first_program1():
    msg = "Hello"
    assert msg == "Hi", "Test failed because String do not match"

def test_second_credit_card():
    print("Good Morning!")

def test_second_credit_card1():
    print("Good Night!")


def test_cross_browser(cross_browser):
    # print(cross_browser)                    # It will execute 3 times : chrome, firefox, IE
    print(cross_browser[1])