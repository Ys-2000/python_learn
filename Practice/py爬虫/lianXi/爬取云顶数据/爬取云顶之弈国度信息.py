import json, xlwt
import os

import requests

# 创建EXCEL
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个新的 Excel 工作簿
# sheet = book.add_sheet('国度', cell_overwrite_ok=True)  # 创建一个sheet页
# sheet.write(0, 0, '国家')
# sheet.write(0, 1, '特征名称')
# sheet.write(0, 2, '描述')

# def save_to_excel(n,country,name,desc):
#     sheet.write(n, 0, country)
#     sheet.write(n, 1, name)
#     sheet.write(n, 2, desc)


# url = 'https://jcc.qq.com/#/legendDetail/S10/9/1002'
url = 'https://game.gtimg.cn/images/lol/act/jkzlk/js//9/9.3.20-S10/galaxy.js'

response = requests.get(url).text

json = json.loads(response)['data']
cou = []
log = []
n = 1
for i in json:
    name = json[i]['name']                  # 名称
    desc = json[i]['desc']                  # 描述
    country = json[i]['country']            # 国家
    logo = json[i]['logo']                  # logo
    if country not in cou:                  # 检查国家是否已经在列表中
        cou.append(country)                 # 如果没有，将其添加到列表
    if logo not in log:                     # 检查logo是否已经在列表中
        log.append(logo)                    # 如果没有，将其添加到列表

    # save_to_excel(n,country,name,desc)
    n+=1

# book.save('云顶国度介绍.xls')

a_path = os.path.join('d:'+os.path.sep+'云顶')        # os.path.sep获取当前操作系统下的路径分隔符
for a in range(len(cou)):
    img_data = requests.get(log[a]).content
    if not os.path.exists(a_path):
        os.makedirs(a_path)
    b_path = os.path.join(a_path,f'{cou[a]}.jpg')
    with open(b_path, 'wb')as file:
        file.write(img_data)



