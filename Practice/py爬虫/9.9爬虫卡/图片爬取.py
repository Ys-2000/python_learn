import requests

url = "https://scpic.chinaz.net/files/default/imgs/2024-01-17/6e67b0fa8bc2b7e2.jpg"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url,headers=headers)

with open("img.jpg","wb") as f:
    f.write(response.content)