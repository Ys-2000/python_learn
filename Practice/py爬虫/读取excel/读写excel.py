import xlrd
import xlrd2        # xlrd版本太高了 不能操作xlsx表格。。。 xlrd2可以

# 一个workbook就是一个excel
workbook = xlrd2.open_workbook('gp_data.xlsx')
# 找到要读取的sheet
sheet = workbook.sheet_by_name('Sheet2')
# 从表格里读取表头
title_row = sheet.row(0)  # 表头

# print(title_row[1].value)     # 获取表头中第一行的值
# print(sheet.nrows)            # 获取最大行号
# print(sheet.ncols)            # 获取最大列号
lis = []
for i in range(1, sheet.nrows):
    dic = {}                # 用来存每行数据的字典
    data_row = sheet.row(i)     # 拿到每一行数据
    # print(data_row)
    # print('**'*10)
    for j in range(sheet.ncols):     # 列的编号
        cell = data_row[j]
        # print(cell.value)
        if cell.ctype == xlrd.XL_CELL_DATE:     # 如果是日期,需要单独处理
            value = xlrd.xldate_as_datetime(cell.value,0).strftime("%Y-%m-%d")  # strftime格式化时间
        elif cell.ctype == xlrd.XL_CELL_NUMBER:
            value = int(cell.value)
        else:
            value = cell.value
        dic[title_row[j].value] = value     # 把数据放到字典中
    lis.append(dic)
print(lis)