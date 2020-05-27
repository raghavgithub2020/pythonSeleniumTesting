# Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
import pytest



@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")
    print("Good Morning")
    print("Good Morning")
    print("Good Morning")
    print("Good Morning")

@pytest.mark.xfail # it will fail the test case and wil not show in report
def test_SecondGreetCreditCard():
    print("Good Morning")
    print("Good Morning")
    print("Good Morning")
    print("Good Morning")
    print("Good Morning")


@pytest.fixture()
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])







