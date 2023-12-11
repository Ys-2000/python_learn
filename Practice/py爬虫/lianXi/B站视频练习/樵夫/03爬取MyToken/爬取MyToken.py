import time
import requests
from hashlib import md5
def get_info():
    url = 'https://api.mytokenapi.com/ticker/currencylistforall'
    n = str(int(time.time() * 1000))         # python拿到的时间戳是秒 web前端是毫秒 差了1000倍
    # python计算md5固定操作
    obj = md5()
    obj.update((n+'9527'+n[:6]).encode("utf-8"))
    val = obj.hexdigest()
    params = {
        "pages": "1,1",
        "sizes": "100,100",
        "subject": "market_cap",
        "language": "en_US",
        "timestamp": n,   # 时间戳不能锁死
        "code": val,     # code=时间戳+9527+时间戳前6位的md5加密
        "platform": "web_pc",
        "v": "0.1.0",
        "legal_currency": "USD",
        "international": "1",
    }
    headers = {
        # 用户的设备
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }
    response = requests.get(url, params=params, headers=headers).json()
    # 把返回的json字符串转换为python字典
    # python字典与json相似度99%
    list = response['data']['list']
    for item in list:
        print(item['name'], item['price_display_cny'])


while 1:
    get_info()
    print('-'*10)
    time.sleep(10)
