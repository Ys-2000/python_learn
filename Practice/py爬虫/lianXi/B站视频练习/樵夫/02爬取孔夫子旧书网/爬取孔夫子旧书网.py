import requests

url = 'https://search.kongfz.com/product_result/'

params = {
    'key': '9787040010251',
    'status':'0',
    '_stpmt':'eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9',
    'pagenum': '2',
    'ajaxdata': '1',
    'type': '1',
    '_': '1701311296956',
}
headers = {
    # 用户的设备
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Referer":"https://search.kongfz.com/product_result/?key=9787040010251&status=0&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9"
}

# 发送请求,带上参数
response = requests.get(url, params=params, headers=headers)
print(response.text)