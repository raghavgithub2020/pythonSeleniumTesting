import pytest

# py.test /reports/report.html


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Raghav","Rahul","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Rahul","Ragahv"), ("firefox","Amilineni"), ("safari","Naidu")])
def crossBrowser(request):
    return request.param
