import json
import requests


# 确定目标
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
# 发送请求
requests = requests.get(url, headers=header)
html = json.loads(requests.text)        # 把json数据转换成python对象

print(html['hero'])







# 解析数据


# 保存数据