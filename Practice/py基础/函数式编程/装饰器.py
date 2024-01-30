import datetime,time
import functools

def wrapper(fun):
    @functools.wraps(fun)   # 把原始函数的__name__等属性复制到wrapper()函数中
    def inner(*args,**kwargs):
        print("函数开始！")
        f = fun(*args,**kwargs)     # *args,**kwargs  表示可接受所有参数
        print("函数结束！")
        return f
    return inner


@wrapper
def now():
    """我是注释！！"""
    print(datetime.date.today())        # 打印当前日期
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))# 打印当前日期

now()
print(now.__name__)     # 打印函数名
print(now.__doc__)     # 打印函数名

# def tim(fun):
#     def atm(*args,**kwargs):
#         print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
#         fun(*args,**kwargs)
#     return atm
#
#
# @tim
# def punch():
#     print('昵称：两点水  部门：做鸭事业部 上班打卡成功')
#
#
# punch()


# decorator装饰器
# import functools

# def log(func):
#     # @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print(f'call {func.__name__}():')
#         return func(*args, **kw)
#     return wrapper
#
# @log    # @log就相当于 now = log(now)
# def now():
#     print('2015-3-25')
#     return 1



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

