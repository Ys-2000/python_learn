import json
import os.path
import requests
import xlwt

# 创建EXCEL
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个新的 Excel 工作簿
sheet = book.add_sheet('云顶强化铭文', cell_overwrite_ok=True)  # 创建一个sheet页
sheet.write(0, 0, '铭文名称')
sheet.write(0, 1, '铭文描述')
sheet.write(0, 2, '强化图标地址')

def save_to_excel(n,name,desc,icon_url):
    sheet.write(n, 0, name)
    sheet.write(n, 1, desc)
    sheet.write(n, 2, icon_url)

url = 'https://game.gtimg.cn/images/lol/act/jkzlk/js//9/9.3.20-S10/hex.js'      # 强化铭文
response = requests.get(url).text
json = json.loads(response)['data']
a_path = os.path.join('d:'+os.path.sep+'云顶'+'/'+'强化铭文icon')
n = 1
for i in json:
    name = json[i]['name']          # 强化铭文名称
    desc = json[i]['desc']          # 强化铭文描述
    icon_url = json[i]['icon']      # 强化铭文icon_url
    save_to_excel(n, name, desc, icon_url)
    n+=1
book.save('强化铭文介绍.xls')
    # # 保存图片
    # img = requests.get(icon_url).content
    # if not os.path.exists(a_path):
    #     os.makedirs(a_path)
    # b_path = os.path.join(a_path, f"{name}.jpg")
    # with open(b_path,'wb') as file:
    #     file.write(img)
