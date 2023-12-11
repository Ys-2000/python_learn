from bs4 import BeautifulSoup
import requests,time,random,os,re


def seveimg(img_data,img_name,img_path):
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    image_path = os.path.join(img_path, re.sub(r'[/|?]', '', img_name))
    print(f"正在写入<{img_name}>")
    with open(image_path, 'wb') as image:
        image.write(img_data)
        print(f"<{img_name}>写入成功，路径:{image_path}")
        time.sleep(random.uniform(0, 3))  # 生成 1 到 3 秒的随机小数延时


url = 'https://www.sanguosha.com/wallpaper/page/1'
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
response = requests.get(url,headers=headers).text

html = BeautifulSoup(response,'lxml')
list = html.find(class_='wallpaper').find_all('li')
for i in list:
    href = i.find('a')['href']      # 壁纸地址
    name = i.find('p').text.replace('*', '-')         # 壁纸名称
    imgdata = requests.get(href, headers=headers).content   # 请求图片链接，获取二进制图片数据
    image_path = 'd:/英雄杀/壁纸'
    img_name = f"{name}.png"
    seveimg(imgdata,img_name,image_path)

