import requests

page = 1
url = f'https://www.maoyan.com/board/4?offset={page}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
}
response = requests.get(url,headers=headers).text
print(response)