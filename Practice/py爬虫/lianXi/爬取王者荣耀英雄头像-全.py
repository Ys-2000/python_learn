import requests, os

yx_url = 'https://pvp.qq.com/web201605/js/herolist.json'

def paqu(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    html = requests.get(url, headers=headers)
    return html


# 访问英雄列表
yx_list = paqu(yx_url).json()
for name in yx_list:
    ename = name['ename']  # 英雄id
    cname = name['cname']  # 英雄中文名称

    # 爬取英雄头像
    tx_url = f'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{ename}/{ename}.jpg'
    yx_ename = paqu(tx_url).content
    # 头像存储
    base_path = os.path.join('d:' + os.path.sep, '王者荣耀', '头像')
    # 确保目录存在，如果不存在则创建
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)
    cc_path = os.path.join(base_path, f'{cname}.jpg')
    with open(cc_path,'wb') as file:
        file.write(yx_ename)
        print(f"正在下载英雄 {cname} 的头像...")
