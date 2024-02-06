
# fixture为class级别的时候，如果一个class里面有多个用例，都调用了次fixture，那么此fixture只在此class里所有用例开始前执行一次。

import pytest

@pytest.fixture(scope='class')
def test1():
    b = '男'
    print('传出了%s, 且只在class里所有用例开始前执行一次！！！' % b)
    return b


class TestCase:
    def test3(self, test1):
        name = '男'
        print('找到name')
        assert test1 == name

    def test4(self, test1):
        sex = '男'
        print('找到sex')
        assert test1 == sex










if __name__ == '__main__':
    pytest.main('-q test_06_scope参数class用法.py')