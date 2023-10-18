import requests

url = 'https://game.gtimg.cn/images/lol/act/jkzlk/js//9/9.3.20-S10/equip.js'
json = requests.get(url).json()['data']
for i in json:
    name = json[i]['name']                  # 名称
    basicDesc = json[i]['basicDesc']        # 作用
    type = json[i]['type']                  # 类型
    desc = json[i]['desc']                  # 描述
    print(name,basicDesc,desc,type)
print(json)