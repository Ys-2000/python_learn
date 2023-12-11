import time,random
import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

url = 'https://app.swguancha.com/client/v1/cPublic/consumer/baseInfo'
session = requests.session()
session.headers = {
    "Content-Type":"application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
page_a = range(1,11)
for page in page_a:
    data = {
    'current':page,
    'dimensionTime':'2019',
    'levelType':'2',
    'propertyCode':["DISTRICT_PROP_GJ025_RJDQSCZZ", "DISTRICT_PROP_GJ117_NMSYGGQDCYYCLS", "DISTRICT_PROP_GJ001_NMHJRK"],
    'size':'6',
    }
    # 浏览器处理的json没有空格，python处理的有空格，使用separators参数去除空格
    response =session.post(url=url,data=json.dumps(data,separators=(',',':')))


    # 把密钥处理成字节
    key = 'QV1f3nHn2qm7i3xrj3Y9K9imDdGTjTu9'.encode('utf-8')
    aes = AES.new(key=key,mode=AES.MODE_ECB)
    # response.text得到的是base64，需要使用base64.b64decode()处理成字节，然后在解密
    ming = aes.decrypt(base64.b64decode(response.text))
    # 去掉填充
    ming = unpad(ming,16)
    # 把明文处理成字符串
    s = ming.decode('utf-8')
    # 把json字符串转换成字典
    dic = json.loads(s)

    for i in dic['data']['data']:
        cityName = i['cityName']
        print(cityName)
        for a in i['simpleVOList']:
            simpleName = a['simpleName']
            propertyValue = a['propertyValue']
            valueUnit = a['valueUnit']
            print(simpleName,propertyValue+valueUnit)
        print("**"*20)
        sleep_time = random.uniform(1, 3)  # 生成 1 到 3 秒的随机小数延时
        time.sleep(sleep_time)
    print(f"第{page}页已爬取完成")