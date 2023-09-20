import functools

# # functools.partial创建一个偏函数的，不需要我们自己定义int2()
# int2 = functools.partial(int, base=2)       # base参数，默认值为10。如果传入base参数，就可以做N进制的转换
#
#
# print(int2('1000000'))

# 定义一个取余函数，默认和2取余；
def mod(x,y=2):
  # 返回 True 或 False
  return x % y == 0

# 假设我们要计算和3取余，如果不使用partial()函数，那么我们每次调用mod()函数时，都要写y=3
# mod(4,y=3)
# mod(6,y=3)

# 使用partial()函数
from functools import partial
mod_3 = partial(mod,y=3)
print(mod_3(4))
print(mod_3(6))

