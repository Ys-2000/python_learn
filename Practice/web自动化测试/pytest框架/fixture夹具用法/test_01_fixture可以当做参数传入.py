"""
# fixture可以当做参数传入
# 定义fixture跟定义普通函数差不多，唯一区别就是在函数上加个装饰器@pytest.fixture()，fixture命名不要以test开头，跟用例区分开。
# fixture是有返回值得，没有返回值默认为None。用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称。
"""
import pytest

@pytest.fixture()
def test1():
    a = 'leo'
    return a


def test_2(test1):
    assert test1 == 'leo'


if __name__ == '__main__':
    pytest.main('-q test_01_fixture可以当做参数传入.py')
