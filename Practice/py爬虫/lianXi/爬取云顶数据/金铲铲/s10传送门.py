import requests
from bs4 import BeautifulSoup

url = 'https://game.gtimg.cn/images/lol/act/jkzlk/js//10/10.3.23-S11/galaxy.js'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
response = requests.get(url,headers=headers).json()
data = response['data']
for i in data:
    id = data[i]['id']
    name = data[i]['name']
    desc = data[i]['desc']
    print(id+'---'+name+'---'+desc)