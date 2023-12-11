import xlwt

book = xlwt.Workbook('te')

sheet = book.add_sheet("qwe")
sheet.write(0, 0, '编号')
sheet.write(0, 1, '姓名')
sheet.write(0, 2, '成绩')

sheet.write(1, 0, '1')
sheet.write(1, 1, 'xx')
sheet.write(1, 2, '66')

book.save('text.xls')
