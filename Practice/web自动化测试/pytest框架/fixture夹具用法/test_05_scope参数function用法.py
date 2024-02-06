
# @pytest.fixture（）如果不写参数，参数就是scope="function"，它的作用范围是每个测试用例来之前运行一次，销毁代码在测试用例之后运行。

import pytest

@pytest.fixture()
def test1():
    a = 'leo'
    print('\n传出a')
    return a


@pytest.fixture(scope='function')
def test2():
    b = '男'
    print('\n传出b')
    return b


def test3(test1):
    name = 'leo'
    print('找到name')
    assert test1 == name


def test4(test2):
    sex = '男'
    print('找到sex')
    assert test2 == sex




# #放在类中实现结果也是一样的
# class TestCase:
#     def test3(self, test1):
#         name = 'leo'
#         print('找到name')
#         assert test1 == name
#
#     def test4(self, test2):
#         sex = '男'
#         print('找到sex')
#         assert test2 == sex











if __name__ == '__main__':
    pytest.main('-q test_05_scope参数function用法.py')