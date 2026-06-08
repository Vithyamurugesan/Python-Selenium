import pytest
@pytest.mark.smoke
def test_login():
    assert True

@pytest.mark.regression
def test_payment():
    assert True

@pytest.mark.skip(reason="It is tempor not executed")
def test_example_skip():
        assert 3*3 ==9


@pytest.mark.skipif()
def test_example_skipif():
        assert 3*3 ==9


@pytest.mark.xfail()
def test_example_xfail():
        assert 2*3==7

@pytest.mark.parametrize("test_input,expected",[(1,3),(3,6),(5,7)])
def test_add(test_input,expected):
      assert test_input+2==expected