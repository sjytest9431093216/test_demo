import pytest
def test_one():
    print("开始执行")
    x = 'this'
    assert 'h' in x

def test_two():
    print("开始执行2")
    x = 'hello'
    assert 'e' in x

if __name__=='__main__':
    pytest.main()


