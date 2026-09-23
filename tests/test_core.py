from uem_labs.core import add, greet


def test_add():
    assert add(2, 3) == 5


def test_greet():
    assert greet("Ada") == "Hello, Ada!"
