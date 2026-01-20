import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("I will execute the steps in Fixture Demo")

    def test_fixture_demo1(self):
        print("I will execute the steps in Fixture Demo1")

    def test_fixture_demo2(self):
        print("I will execute the steps in Fixture Demo2")

    def test_fixture_demo3(self):
        print("I will execute the steps in Fixture Demo3")