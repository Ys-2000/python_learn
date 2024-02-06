
#  fixture为session级别是可以跨.py模块调用的，也就是当我们有多个.py文件的用例的时候，如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里。

import pytest

@pytest.fixture(scope='module')
def test1():
    b = '男'
    print('传出了%s, 且在当前py文件下执行一次！！！' % b)
    return b


def test3(test1):
    name = '男'
    print('找到name')
    assert test1 == name


class TestCase:

    def test4(self, test1):
        sex = '男'
        print('找到sex')
        assert test1 == sex









if __name__ == '__main__':
    pytest.main('-q test_08_scope参数session用法.py')