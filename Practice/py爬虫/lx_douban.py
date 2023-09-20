from bs4 import BeautifulSoup
import requests, time, random

def main(page):
    url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
    headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    html = requests.get(url, headers=headers).text

    if html is not None:
        soup = BeautifulSoup(html, 'lxml')  # 使用BeautifulSoup来解析HTML页面
        # save_to_excel(soup)
        # 解析
        list = soup.find(class_='grid_view').find_all('li')     # 找到页面中具有 grid_view 类的元素在到所有的 <li> 元素
        t = 0
        for item in list:
            item_name = item.find(class_='title').string            # 名称
            item_img = item.find('a').find('img').get('src')        # 图片
            item_index = item.find(class_='').string                # ID
            item_score = item.find(class_='rating_num').string      # 分数
            item_author = item.find('p').text                       # 作者
            # item_intr = item.find(class_='inq').string              # 简介
            print('爬取电影：' + item_index + ' | ' + item_name  +' | ' + item_score  +' | ' + item_author)
            # t+=1
            # if t in [20, 50, 80, 100, 120, 150, 180, 220, 240]:
            #     print("等待1s!!!")
            #     time.sleep(1)  # 休眠1秒，可以根据需要调整
        print('抓取完成')
    else:
      print("Failed to fetch HTML from", url)


# 请求豆瓣电影
def request_douban(url):
   try:
       response = requests.get(url)
       if response.status_code == 200:
           return response.text
   except requests.RequestException:
       return None



# page_list = [0,25,50,75,100,125]
for i in range(1, 10):
    main(i)
    sleep_time = random.uniform(1, 3)  # 生成 1 到 3 秒的随机延时
    time.sleep(sleep_time)
