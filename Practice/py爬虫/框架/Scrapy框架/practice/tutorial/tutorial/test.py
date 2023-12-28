# class MyClass:
#     my_class_variable = "类变量"
#
#     @classmethod
#     def class_method(cls, arg1, arg2):
#         print("这是一个类方法")
#         print("参数:", arg1, arg2)
#         print("访问类变量:", cls.my_class_variable)
#
# # 调用类方法
# MyClass.class_method('arg1_value', 'arg2_value')

class MyClass():
    def __init__(self):
        self.my_class_variable = "This is a class variable"

    def class_method(self, arg1, arg2):
        print("This is a class method")
        print("Arguments:", arg1, arg2)
        print("Accessing class variable:", self.my_class_variable)

mc = MyClass()
mc.class_method('arg1_value', 'arg2_value')
