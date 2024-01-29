# import datetime

# def now():
#     print(datetime.date.today())
#
#
# f = now
# print(f.__name__)

# decorator装饰器
import functools

def log(func):
    # @functools.wraps(func)
    def wrapper(*args, **kw):
        print(f'call {func.__name__}():')
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')


# now = log(now)

print(now())


# # 带自定义参数的decorator装饰器
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')

