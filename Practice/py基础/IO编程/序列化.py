# import pickle
# d = dict(name='Bob', age=20, score=88)
# # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
# # pickle.dumps(d)
#
# f = open('dump.txt', 'wb')
# # pickle.dump()方法直接把对象序列化后写入一个file-like Object
# pickle.dump(d, f)
# f.close()
#
# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# JSON
import json
d = dict(name='Bob', age=20, score=88)
# dumps()方法返回一个str，内容就是标准的JSON
a = json.dumps(d)
print(a)
b = json.loads(a)
print(b)

