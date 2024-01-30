import pytest


def test_one():
    expect = 1      # 期望
    actual = 1      # 实际
    assert expect == actual

def test_two():
    expect = 1
    actual = 2
    assert expect != actual


if __name__ == '__main__':
    pytest.main()       # 运行当前文件所有的测试用例