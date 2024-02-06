# 叠加usefixtures
# 如果一个方法或者一个class用例想要同时调用多个fixture，可以使用@pytest.mark.usefixture()进行叠加。
# 注意叠加顺序，先执行的放底层，后执行的放上层。

import pytest


@pytest.fixture()
def test1():
    print('\n开始执行function1')


@pytest.fixture()
def test2():
    print('\n开始执行function2')


@pytest.mark.usefixtures('test1')
@pytest.mark.usefixtures('test2')
def test_a():
    print('---用例a执行---')


@pytest.mark.usefixtures('test2')
@pytest.mark.usefixtures('test1')
class TestCase:

    def test_b(self):
        print('---用例b执行---')

    def test_c(self):
        print('---用例c执行---')


if __name__ == '__main__':
    pytest.main()