from openpyxl import Workbook, load_workbook
import openpyxl

# # 1.声明 工作簿
# workBook = openpyxl.Workbook()
#
# # 2.设置 工作簿名称及位置（相对路径 和 绝对路径）
# fileName = 'test.xlsx'      # 相对路径
# # fileName = r"C:\Users\Administrator\Desktop\test.xlsx"        # 绝对路径  r是去转义
#
# # 3.保存。注：若该工作簿已存在，则覆盖
# workBook.save(fileName)

# 1.打开 工作簿
fileName = 'test.xlsx'
workBook = openpyxl.load_workbook(fileName)

# 2.获取要操作的 sheet 对象
sheet = workBook['qwe']

# 3.追加
# sheet.append(['姓名', '性别', '年龄'])
# sheet.append(['张vv', '女', '18'])
# sheet.append(['李四', '男', '19'])
# sheet.append(['王五', '女', '33'])
# sheet.append(['vbn', '女', '23'])

# 3.修改数据，以下几种写法均可
# sheet['A3'] = '我是A3'
# sheet.cell(row=4, column=1).value = 'vvv'
# sheet.cell(row=8, column=1, value='我是A8')

# 4.删除
# sheet.delete_rows(idx=2, amount=2)  # idx 行开始(含)，往下删除 amount 行
# sheet.delete_cols(idx=4, amount=1)  # idx 列开始(含)，往右删除 amount 行

# # 保存后生效
# workBook.save(fileName)
print(sheet['A1'].value)
print(sheet.min_column)
