import requests

url = 'https://game.gtimg.cn/images/lol/act/img/js/items/items.js'

json = requests.get(url).json()['items']

for i in json:
    itemId = i['itemId']                    # 装备ID
    name = i['name']                        # 装备名字
    plaintext = i['plaintext']              # 详细说明
    description = i['description']          # 说明
    print(itemId,name,plaintext,description)

# print(json)