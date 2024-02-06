"""
usefixtures与传fixture区别
如果fixture有返回值，那么usefixture就无法获取到返回值，这个是装饰器usefixture与用例直接传fixture参数的区别。
当fixture需要用到return出来的参数时，只能讲参数名称直接当参数传入，不需要用到return出来的参数时，两种方式都可以。
"""

"""
fixture自动使用autouse=True
当用例很多的时候，每次都传这个参数，会很麻烦。fixture里面有个参数autouse，默认是False没开启的，可以设置为True开启自动使用fixture功能，这样用例就不用每次都去传参了
# autouse设置为True，自动调用fixture功能 示例如下:
"""
import pytest

@pytest.fixture(scope='module', autouse=True)
def test1():
    print('\n开始执行module')


@pytest.fixture(scope='class', autouse=True)
def test2():
    print('\n开始执行class')


@pytest.fixture(scope='function', autouse=True)
def test3():
    print('\n开始执行function')


def test_a():
    print('---用例a执行---')


def test_d():
    print('---用例d执行---')


class TestCase:

    def test_b(self):
        print('---用例b执行---')

    def test_c(self):
        print('---用例c执行---')


if __name__ == '__main__':
    pytest.main()