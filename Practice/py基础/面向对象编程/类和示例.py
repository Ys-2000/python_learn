class Student(object):      # (object)，表示该类是从哪个类继承下来的
    def __init__(self,name,score):  # self，表示创建的实例本身
        # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score

    # 打印名称
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 打印名称与分数
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    # 修改分数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


uzi = Student('jzh', 90)            # 创建一个实例
jiejie = Student('zlj', 70)         # 创建一个实例

print(uzi.get_name())           # 查询名称
print(uzi.print_score())        # 调用print_score方法打印分数
print(jiejie.get_grade())       # 调用get_grade方法获取等级


# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender == 'male':
            self.__gender = gender
        elif gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad score')
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

print(bart.set_gender('male'))