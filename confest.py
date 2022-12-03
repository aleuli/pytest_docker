import pytest


@pytest.fixture(scope="module")
def set_up():
    print("Start test")
    yield
    print("Finish test")
