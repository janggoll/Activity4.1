import math

def test_sqrt():
    num=25
    assert math.sqrt(num) == 5

def test_square():
    num = 7
    assert num*num == 49

def test_check():
    x = 10

    assert x >=10

def test_multiply():
    x = 1
    y = 20

    assert x*y == 20


def fun(x):
    return x
def test_fun():

    assert fun(1) + 2 == 3


