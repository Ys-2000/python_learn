import xlwings as xw

# 连接到一个打开的Excel应用程序或新建一个
app = xw.App()

# 新建一个工作簿或打开一个已有的工作簿
workbook = app.books.add()  # 新建工作簿

# 选择或添加一个工作表
sheet = workbook.sheets.add('Sheet01')

# 定义文本数据
text_data = [['Name', 'Age','img'],
             ['Alice', 25,''],
             ['Bob', 30,''],
             ['Charlie', 35,''],
             ['David', 40,'']]

# 将文本数据写入工作表
sheet.range('A1').value = text_data

# 添加图片

image_path = 'D:\云顶\强化铭文icon\DD街区.jpg'       # 图片文件的路径
sheet.pictures.add(image_path, name='Image', left=sheet.range('C2').left, top=sheet.range('C2').top)


# 保存工作簿
workbook.save('text_data.xlsx')

# 关闭工作簿
workbook.close()

# 退出Excel应用程序
app.quit()
