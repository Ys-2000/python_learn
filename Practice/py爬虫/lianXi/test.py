import json,os,time,random,re
import requests


# 确定目标
k_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
base_path = os.path.join('d:' + os.path.sep, '英雄联盟')  # os.path.sep获取当前操作系统下的路径分隔符
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


# 发送请求
def send_get(url):
    html = requests.get(url, headers=header)
    return html        # 把json数据转换成python对象

# 保存数据
def save_image(image_dir, image_name, image_content):
    # 如果目录不存在创建目录
    global hero_image_path
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    try:
        hero_image_path = os.path.join(image_dir, re.sub(r'[/|?]', '', image_name))
        # print(hero_image_path)
        with open(hero_image_path, 'wb') as image:
            image.write(image_content)
    except Exception as e:
        print('{}保存失败,错误原因:{}'.format(hero_image_path, e))


# 解析数据
kk = json.loads(send_get(k_url).text)
for hero in kk['hero']:
    hero_info_url = hero_url.format(hero['heroId'])
    h_url = send_get(hero_info_url)
    if h_url:
        hero_info_dict = json.loads(h_url.text)  # 将 JSON 格式的字符串转换为 Python字典对象
        # print(hero_info_dict)
        hero = hero_info_dict['hero']
        skins = hero_info_dict['skins']
        for skin in skins:
            if skin['mainImg']:
                skin_content = send_get(skin['mainImg']).content
                hero_image_name = '{}.jpg'.format(skin['name'])
                hero_image_dir = os.path.join(base_path, hero['name'] + hero['title'])
                save_image(hero_image_dir, hero_image_name, skin_content)
        print('hero:{},skins:{}张,处理完成'.format(hero['name'], len(skins)))
        time.sleep(random.uniform(0, 3))    # 生成 1 到 3 秒的随机小数延时



