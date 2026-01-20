import pytest

@pytest.mark.xfail
def test_first_program():
    print("Second test")

@pytest.mark.smoke
def test_second_credit_card():
    a=4
    b=6
    assert a+2 == b, "Test failed Addition not matched"


@pytest.fixture()
def setup():
    print("I will execute first as a setup fixture")

def test_fixture_demo(setup):
    print("I will execute the steps in Fixture Demo")