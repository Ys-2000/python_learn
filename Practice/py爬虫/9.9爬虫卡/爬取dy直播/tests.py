import requests
from bs4 import BeautifulSoup

url = "https://www.douyu.com/gapi/rkc/directory/mixList/2_1/1"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "dy_did=f4cf8872a191a39a5adc9bc400041601; acf_did=f4cf8872a191a39a5adc9bc400041601; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1706243552,1706751279,1708141341; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1708234699",
    "Referer": "https://www.douyu.com/g_LOL",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}

response = requests.get(url,headers=headers)

data = response.json()['data']
