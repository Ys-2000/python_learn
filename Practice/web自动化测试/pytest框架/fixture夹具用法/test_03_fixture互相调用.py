"""
# fixture互相调用
# 如果用例需要用到多个fixture的返回数据，fixture也可以返回一个元祖，list或字典，然后从里面取出对应数据。
"""
import pytest

@pytest.fixture()
def first():
    print("获取用户名")
    a = "hjt"
    return a

@pytest.fixture()
def sencond(first):
    '''psw调用user fixture'''
    a = first
    b = "123456"
    return (a, b)

def test_1(sencond):
    '''用例传fixture'''
    print("测试账号：%s, 密码：%s" % (sencond[0], sencond[1]))

    assert sencond[0] == "hjt"




if __name__ == '__main__':
    pytest.main('-q test_03_fixture互相调用.py')