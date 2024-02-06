"""
# 使用多个fixture
# 如果用例需要用到多个fixture的返回数据，fixture也可以返回一个元祖，list或字典，然后从里面取出对应数据。
"""
import pytest

@pytest.fixture()
def test1():
    a = 'leo'
    b = '123456'
    print('传出a,b')
    return (a, b)


def test2(test1):
    u = test1[0]
    p = test1[1]
    assert u == 'leo'
    assert p == '123456'
    print('元祖形式正确')


if __name__ == '__main__':
    pytest.main('-q test_02_使用多个fixture.py')