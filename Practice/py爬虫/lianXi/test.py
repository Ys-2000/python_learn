import requests, json, time, os, random, re

# url = "https://lol.qq.com/data/info-heros.shtml"
header = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'
}


class lol_hero():
    def __init__(self):
        self.header = header
        self.hero_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
        self.hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
        self.base_path = os.path.join('d:' + os.path.sep, '英雄联盟')    # os.path.sep获取当前操作系统下的路径分隔符

    # 封装请求方法
    def send_get(self, url):
        try:
            response = requests.get(url, headers = header)
            # 如果断言响应码！=200，触发断言异常，并显示错误信息
            assert response.status_code == 200,'{}请求失败'.format(url)
            return response
        except Exception as e:
            print(e)
            return None


    # 获取首页英雄列表
    def hero_list(self):
        # 获取英雄列表
        response = self.send_get(self.hero_list_url)
        # print(response)
        if response:
            hero_list_text = response.text  # 获得响应数据
            hero_list_dict = json.loads(hero_list_text)  # 响应数据封装json
            # print(hero_list_dict)
            self.process_heroes(**hero_list_dict)  # 调用处理方法.
        else:
            print('英雄列表为空,请检查获取URL:{}'.format(self.hero_list_url))


    # 对英雄列表进行处理
    def process_heroes(self, **hero_list_dict):
        for hero in hero_list_dict['hero']:
            hero_info_url = self.hero_url.format(hero['heroId'])
            resp = self.send_get(hero_info_url)
            if resp:
                hero_info_dict = json.loads(resp.text)
                self.process_hero(**hero_info_dict)
            else:
                print('获取英雄:{}失败,请检查获取URL:{}'.format(hero['name'], self.hero_list_url))
            break


    # 处理单个英雄
    def process_hero(self, **hero_info_dict):
        hero = hero_info_dict['hero']
        skins = hero_info_dict['skins']
        i = 0
        for skin in skins:
            if skin['mainImg']:
                skin_content = self.send_get(skin['mainImg']).content
                hero_image_name = '{}.jpg'.format(skin['name'])
                hero_image_dir = os.path.join(self.base_path, hero['name'] + hero['title'])
                self.save_image(hero_image_dir, hero_image_name, skin_content)
                i+=1
        print('hero:{},skins:{}张,处理完成{}'.format(hero['name'], i, len(skins)))

        sleep_time = random.uniform(1, 3)  # 生成 1 到 3 秒的随机小数延时
        time.sleep(sleep_time)


    # 图片保存
    def save_image(self, image_dir, image_name, image_content):
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




if __name__ == '__main__':
    lol_hero().hero_list()
