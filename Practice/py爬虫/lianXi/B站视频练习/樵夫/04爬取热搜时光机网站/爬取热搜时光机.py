import requests
import base64
from Crypto.Cipher import AES

url = 'https://api.weibotop.cn/currentitems'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
response = requests.get(url, headers=headers)
mi = response.text
# 解密
# 把base64还原成字节(加密后)
mi_bs = base64.b64decode(mi)
print(mi_bs)
# 进行解密  方案：AES加密的-->用AES解密

