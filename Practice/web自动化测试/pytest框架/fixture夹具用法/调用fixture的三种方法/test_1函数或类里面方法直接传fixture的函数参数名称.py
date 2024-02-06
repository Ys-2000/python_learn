# 1.函数或类里面方法直接传fixture的函数参数名称
import pytest



@pytest.fixture()
def test1():
    print('\n开始执行function')


def test_a(test1):
    print('---用例a执行---')


class TestCase:

    def test_b(self, test1):
        print('---用例b执行')
