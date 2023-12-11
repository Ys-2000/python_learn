import base64


# 测试base64存储图片
s = ''
# 需要使用base64.b64decode()将base64数据处理成字节
bs = base64.b64decode(s)
with open('tu.png','wb') as f:
    f.write(bs)


# a = '人生苦短，我学python！'
# # 加密
# b = base64.b64encode(a.encode('utf-8'))
# print(b)
# # 解密
# c = base64.b64decode(b).decode('utf-8')
# print(c)