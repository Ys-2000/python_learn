import requests
import random
import time
import re
import json
import os

# url = https://lol.qq.com/data/info-heros.shtml
# url = 'https://lol.qq.com/data/info-heros.shtml'

# 需要设置USER_AGENT,假装自己是浏览器访问网页
user_agent_list = [
 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
 ]
USER_AGENT = random.choice(user_agent_list)
header = {
 'User-Agent':USER_AGENT
}

class LOLHeroSpider():
   def __init__(self):
       self.header = header
       self.hero_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
       self.hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'
       self.base_path = os.path.join('d:' + os.path.sep, '英雄联盟')    # os.path.sep获取当前操作系统下的路径分隔符
   # 封装请求方法
   def send_get(self, url):
       try:
           response = requests.get(url, headers=self.header)
           # 断言测试
           assert response.status_code == 200, '{}请求失败'.format(url)
           return response
       except Exception as e:
           print(e)
           return None

   # 获得所有的英雄列表
   def hero_list(self):
       # 获取英雄列表
       response = self.send_get(self.hero_list_url)
       if response:
           hero_list_text = response.text  # 获得响应数据
           hero_list_dict = json.loads(hero_list_text)  # 响应数据封装json
           self.process_heroes(**hero_list_dict)  # 调用处理方法
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
   # 单个英雄处理
   def process_hero(self, **hero_info_dict):
       hero = hero_info_dict['hero']
       skins = hero_info_dict['skins']
       for skin in skins:
           if skin['mainImg']:
               skin_content = self.send_get(skin['mainImg']).content
               hero_image_name = '{}.jpg'.format(skin['name'])
               hero_image_dir = os.path.join(self.base_path, hero['name'] + hero['title'])
               self.save_image(hero_image_dir, hero_image_name, skin_content)
       print('hero:{},skins:{}张,处理完成'.format(hero['name'], len(skins)))
       time.sleep(1)

   # 图片保存
   def save_image(self, image_dir, image_name, image_content):
       # 如果目录不存在创建目录
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
    LOLHeroSpider().hero_list()
