import mysql.connector

# 连接数据库
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='000000',
    database='test'
)


# 创建表格
def create_table():
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        c_score INT,
        python_score INT,
        java_score INT
    )
    ''')
    conn.commit()


# 主函数
def main():
    while True:
        create_table()
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
                insert()  # 新增
            elif choice == 2:
                search()  # 查询
            elif choice == 3:
                delete()  # 删除
            elif choice == 4:
                modify()  # 修改
            # elif choice == 5:
            #     sort()  # 排序
            # elif choice == 6:
            #     total()  # 统计学生总人数
            # elif choice == 7:
            #     show()  # 显示所有学生信息
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


# 新增学生信息
def insert():
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
        cursor = conn.cursor()
        sql = "INSERT INTO students (id,name, c_score, python_score, java_score) VALUES (%s,%s, %s, %s, %s)"
        val = (no,name, c, python, java)
        cursor.execute(sql, val)
        conn.commit()
        print('信息录入成功！')
        choice = input('是否继续？y/n:')
        if choice == 'y' or choice == 'Y':
            continue
        else:
            break


# 删除学生信息
def delete():
    while True:
        student_id=int(input('请输入要删除学生的id:'))
        cursor = conn.cursor()
        delete_query = 'DELETE FROM students WHERE id = %s'
        cursor.execute(delete_query, (student_id,))     # 执行语句
        conn.commit()
        if cursor.rowcount > 0:
            print(f'学号为 {student_id} 的学生信息已删除！')
        else:
            print(f'没有找到学号为 {student_id} 的学生信息')
        choice = input ('是否继续？y/n:')
        if choice == 'y':
            continue
        else:
            cursor.close()
            break


# 修改学生信息
def modify():
    while True:
        student_id = int(input('请输入修改学生的id:'))
        cursor = conn.cursor()  # 创建游标
        # 先查询是否存在该学生信息
        select_query = 'SELECT * FROM students WHERE id = %s'
        cursor.execute(select_query, (student_id,))
        student = cursor.fetchone()
        if student is None:
            print(f'没有找到学号为 {student_id} 的学生信息')
        else:
            print(f'当前学生信息：{student}')
            try:
                new_name = input('请输入学生姓名:')
                new_c = int(input('请输入C语言成绩:'))
                new_python = int(input('请输入Python的成绩:'))
                new_java = int(input('请输入Java的成绩:'))
            except:
                print('输入的信息有误，重新输入！！')
                continue
            # 更新学生信息
            update_query = '''
                    UPDATE students
                    SET name = %s, c_score = %s, python_score = %s, java_score = %s
                    WHERE id = %s
                    '''
            params = (new_name or student[1], new_c or student[2],
                      new_python or student[3], new_java or student[4], student_id)
            cursor.execute(update_query, params)
            conn.commit()
            print(f'学号为 {student_id} 的学生信息已更新！')
            switch = input ('是否要修改信息？y/n:')
            if switch.lower() == 'y':
                continue
            else:
                cursor.close()
                break

# 查询学生信息
def search():
    while True:
        student_id = int(input('请输入查询学生的id:'))
        cursor = conn.cursor()  # 创建游标
        select_query = 'SELECT * FROM students WHERE id = %s'
        cursor.execute(select_query, (student_id,))
        student = cursor.fetchone()
        if student is None:
            print(f'没有找到学号为 {student_id} 的学生信息')
        else:
            print(f'当前学生信息：{student}')

        switch = input('是否要修改信息？y/n:')
        if switch.lower() == 'y':
            continue
        else:
            cursor.close()
            break


if __name__ == '__main__':
    main()

# 关闭数据库连接
conn.close()
