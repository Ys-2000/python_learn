from types import MethodType

class Student(object):
    def set_age(self, age): # 定义一个函数作为实例方法
        self.age = age

s = Student()
# s.name = 'Michael'      # 动态给实例绑定一个属性
# print(s.name)


# s.set_age = MethodType(Student.set_age, s)  # 给实例绑定一个方法

s.set_age(25)   # 调用实例方法
print(s.age)    # 测试结果

s2 = Student()
# s2.set_age = MethodType(Student.set_age, s2)  # 给实例绑定一个方法

s2.set_age(12)
print(s2.age)


