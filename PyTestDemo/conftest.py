import pytest


@pytest.fixture(scope="class")
def setup():
    print(" ************ ")
    print("I will execute first as a setup fixture")
    yield           # after yield all the steps will be executed after the tests execution
    print("I will execute at the last")

@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulacademy.com"]

@pytest.fixture(params=[("chrome", "Rahul", "Shetty"), ("firefox", "Rahul", "Shetty"), ("IE", "SS", "Shetty")])
def cross_browser(request):
    return request.param