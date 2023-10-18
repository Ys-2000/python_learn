import requests

url = 'https://game.gtimg.cn/images/lol/act/jkzlk/js//9/9.3.20-S10/chess.js'
response = requests.get(url).json()['data']
for i in response:
    name = response[i]['name']
    skillName = response[i]['skillName']
    skillDesc = response[i]['skillDesc']
    # print(i,name)
print(response)