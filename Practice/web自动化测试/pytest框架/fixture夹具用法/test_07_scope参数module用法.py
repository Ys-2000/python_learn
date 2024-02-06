
# fixture为module时，在当前.py脚本里面所有用例开始前只执行一次。

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
    pytest.main('-q test_07_scope参数module用法.py')