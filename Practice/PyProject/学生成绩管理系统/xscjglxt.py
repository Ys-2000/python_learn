import os

# raw string 避免转义字符带来的问题
filename = r"E:\my\study\bianc\python\Practice\PyProject\学生成绩管理系统\students.txt"


def main():
    while True:
        menu()  # 调用菜单函数
        choice = int(input('请选择:'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                # answer = input('请确定要退出系统?y/n:')
                # if answer == 'y' or answer == 'Y':
                    print('谢谢你的使用')
                    break
                # else:
                #     continue
            elif choice == 1:
                insert()        # 新增
            elif choice == 2:
                search()        # 查询
            elif choice == 3:
                delete()        # 删除
            elif choice == 4:
                modify()        # 修改
            elif choice == 5:
                sort()          # 排序
            elif choice == 6:
                total()         # 统计学生总人数
            elif choice == 7:
                show()          # 显示所有学生信息
        else:
            print('请正确输入数字！')


def menu():
    print('=========================学生成绩管理系统=========================')
    print('----------------------------功能模块----------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('-------------------------------------------------------------')


# 插入学生信息功能
def insert():
    stu_lst = []
    while True:
        no = int(input('请输入学号（例如1001）:'))
        if not no:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            c = int(input('请输入C语言成绩:'))
            python = int(input('请输入Python的成绩:'))
            java = int(input('请输入Java的成绩:'))
        except:
            print('输入无效，请重新输入！')
            continue
        student = {'id': no, 'name': name, 'C语言': c, 'Python': python, 'Java': java}
        stu_lst.append(student)
        save(stu_lst)
        print('信息录入成功！')
        stu_lst.clear()
        choice = input('是否继续？y/n:')
        if choice == 'y' or choice == 'Y':
            continue
        else:
            break


# 存储列表数据
def save(lst):
    try:
        # w是覆盖，a是追加
        with open(filename, 'a', encoding='utf-8') as stu_txt:
            for item in lst:
                stu_txt.write(str(item) + '\n')  # write()来写入文件
    except:
        print("保存失败")


# 定义查找学生信息函数
def search():
    search_qurry = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):        # 用于检查给定路径是否存在
            choice = int(input('Id查询请按1，名字查询请按2:'))
            if choice == 1:
                id = int(input('请输入学生id:'))
            elif choice == 2:
                name = input('请输入学生姓名:')
            else:
                print('输入有误，重新输入！')
                search()
            with open(filename, 'r', encoding='utf-8') as file:     # 标示符'r'表示读
                student_lst = file.readlines()  # readlines()读取文件中的所有行并以列表形式返回
                # 循环列表 当列表id等于要查找的id，把当前循环的列表添加到search_qurry列表；
                for item in student_lst:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            search_qurry.append(d)
                    elif name != '':
                        if d['name'] == name:
                            search_qurry.append(d)
            show_student(search_qurry)
            search_qurry.clear()        # clear()清空列表中的所有元素
        a = input('是否继续查找？y/n:')
        if a == 'y' or 'Y':
            continue
        else:
            break


# 显示学生成绩列表
def show_student(lst):
    if len(lst) == 0:
        print('列表中无此学生的信息')
        return
    student_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(student_title.format('ID', '姓名', 'C语言成绩', 'Python成绩', 'Java成绩', '绩点'))
    student_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(student_data.format(item.get('id'), item.get('name'), item.get('C语言'), item.get('Python'), item.get('Java'),
                                  round((int(item.get('C语言')) + int(item.get('Python')) + int(item.get('Java')) - 180) / 30,
                                        2)))


# 删除学生信息功能
def delete():
    while True:
        student_id=int(input('请输入学生的id:'))
        if student_id:
            if os.path.exists(filename):    # 用于检查给定路径是否存在
                with open(filename,'r',encoding='utf-8') as file:
                    student_old = file.readlines()      # readlines()读取文件中的所有行并以列表形式返回
            else:
                student_old=[]
            flag=False      # 判断是否找到要删除的学生信息
            # 检查之前从文件中读取的学生信息是否存在，如果存在（即不为空列表），则执行下面的代码
            if student_old:
                with open(filename,'w',encoding='utf-8') as files:
                    for item in student_old:
                        # 将字符串格式的学生信息转换为字典格式，存储在变量 d 中
                        d = dict (eval (item))
                        # 检查当前学生信息的学号是否与要删除的学号student_id 不同，如果不同，则将该学生信息写入文件中，相当于删除了该学生信息
                        if d['id']!=student_id:         # 当前循环的列表值不等于要删除的id,把值写入文件
                            files.write(str(d)+'\n')
                        else:
                            # 如果找到要删除的学号，将 flag 置为 True，表示已经找到该学生信息
                            flag=True
                    if flag:
                        print (f'学号为{student_id}的学生信息已删除！')
                    else:
                        print (f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生记录')
                break
            show()
            choice = input ('是否继续？y/n:')
            if choice == 'y':
                continue
            else:
                break


# 显示文本中的数据
def show():
    student_lst=[]
    if os.path.exists(filename):        # 用于检查给定路径是否存在
        with open(filename,'r',encoding='utf-8') as file:
            student=file.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存学生数据！')


# 修改学生信息
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student_lst=file.readlines()
    else:
        return
    student_id=int(input('请输入学生id:'))
    with open(filename,'w',encoding='utf-8') as file1:
        for item in student_lst:
            d = dict(eval(item))
            if d['id'] == student_id:
                # print(f'已经找到id为{student_id}的学生')
                while True:
                    try:
                        d['name'] = input('请输入学生姓名:')
                        d['C语言'] = int(input('请输入C语言成绩:'))
                        d['Python'] = int(input('请输入Python的成绩:'))
                        d['Java'] = int(input('请输入Java的成绩:'))
                    except:
                        print('输入的信息有误，重新输入！！')
                    else:
                        break
                file1.write(str(d)+'\n')
                print('修改信息成功！！！！！！！')
            else:
                file1.write(str(d)+'\n')
        switch = input ('是否要修改信息？y/n:')
        if switch == 'y':
            modify()

# 排序
def sort():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_lst = file.readlines()
        student_new = []
        for item in student_lst:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    switch = int(input('排序方式（0.升序，1.降序）'))
    if switch == 0:
        switch_bool = False
    elif switch == 1:
        switch_bool = True
    else:
        print('输入错误！')
        sort()
    choice = input('请选择排序方式（1.C语言成绩，2.Python成绩，3.Java成绩）')
    if choice == '1':
       student_new.sort(key=lambda x:int(x['C语言']),reverse=switch_bool)
    elif choice == '2':
       student_new.sort (key=lambda x: int (x ['Python']), reverse=switch_bool)
    elif choice == '3':
       student_new.sort (key=lambda x: int (x ['Java']), reverse=switch_bool)
    else:
       print('选择错误！重新输入')
       sort()
    show_student(student_new)


# 统计学生总人数
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            students=file.readlines()
            if students:
                print('系统内有{}个学生'.format(len(students)))
            else:
                print('系统内无学生记录！')
    else:
        print('暂未保存学生信息！')

if __name__ == '__main__':                # 程序开始运行
    main()

