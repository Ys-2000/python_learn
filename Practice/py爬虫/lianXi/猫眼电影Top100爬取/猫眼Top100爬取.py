# 目标：爬取排名、电影名、主演、上映时间、上映国家、评分。
# 参考：https://zhuanlan.zhihu.com/p/331711137
# 问题 ：会有滑动验证弹窗

import requests
from bs4 import BeautifulSoup


page = 1
url = f'https://www.maoyan.com/board/4?offset={page}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
}
response = requests.get(url,headers=headers).text
html = BeautifulSoup(response, 'lxml')

yemian = html.find_all(id='app')
print(html)



# if __name__ == '__main__':
#     for i in range(0,11):
#         main(i)