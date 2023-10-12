# xlwt
import xlwt

# 创建一个新的 Excel 工作簿
workbook = xlwt.Workbook()

# 创建一个工作表
worksheet = workbook.add_sheet('My Worksheet')

# 写入数据到工作表
worksheet.write(0, 0, 'Hello')
worksheet.write(0, 1, 'World')

# 保存 Excel 文件
workbook.save('my_excel_file.xls')

print('Excel file saved successfully.')
