import json
import requests

url = 'https://game.gtimg.cn/images/lol/act/jkzlk/js//9/9.3.20-S10/legend.js'
response = requests.get(url).text
json = json.loads(response)['data']

for i in json:
    name = json[i]['name']          # 名称
    alias = json[i]['name2']        # 别名
    desc = json[i]['desc']          # 描述
    print(name,alias,desc)
print(json)
