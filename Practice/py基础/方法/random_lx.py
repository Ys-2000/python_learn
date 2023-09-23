import random

# ***--random.choice()用法--***
list = [1,'a','w',87,90]
a = random.choice(list)
print(a)
# 使用random随机生成8位数密码
f = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pwd = ''
for i in range(8):
    pwd += random.choice(f)
print(pwd)

# ***--random.uniform()用法--***
# 使用random随机生成0-10数字并保留2位小数
b = random.uniform(0, 10)
print(f"随机生成0-10数字:{b:.2f}")