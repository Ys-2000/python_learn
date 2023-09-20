import hashlib,random
# # MD5
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
#
# print(md5.hexdigest())
#
# # SHA1
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())


# # 练习  设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#
# def login(user, password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     if md5.hexdigest() == db[user]:
#         return True
#     else:
#         return False
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')


# 练习  根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        md5 = hashlib.md5()
        md5.update((password + self.salt).encode('utf-8'))
        self.password = md5.hexdigest()

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def get_md5(user, pws):
    md5 = hashlib.md5()
    md5.update((pws+user.salt).encode('utf-8'))
    return md5.hexdigest()

def login(username, password):
    user = db[username]
    return user.password == get_md5(user, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
import psutil