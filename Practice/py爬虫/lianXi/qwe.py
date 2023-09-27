import requests
url = 'https://pvp.qq.com/web201605/js/herolist.json'
html = requests.get(url).json()
print(html)

