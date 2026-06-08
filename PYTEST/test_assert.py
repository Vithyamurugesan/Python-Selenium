#simple assert
def test_addition():
    assert 2 + 3 == 5

'''def test_sub():
    assert 5-3 ==1
    '''

#assert x==y
def test_equal_assertiom():
    x=5
    y=5
    assert x==y

#assert x!=y
def test_not_equal_assertiom():
    x=5
    y=10
    assert x!=y

#assert x in y 
def test_in_assertiom():
    numbers=[1,2,3,4,5]
    assert 3 in numbers

def test_demo():
    a="vithya"
    b="vithya"
    assert a.__eq__(b)