import requests
from bs4 import BeautifulSoup
from lxml import etree, html

url = "https://sdsbtbiotech.com/product/#ntld"

def bs():
    response = requests.get(url).text
    soup = BeautifulSoup(response,"lxml")
    li_list = soup.find("div", class_="wrap").find("ul",class_="tab-bd").find_all("li")
    for li in li_list:
        dl_list = li.find("div",class_="liebiao").find_all("dl")
        for dl in dl_list:
            dt_list = dl.find_all("dt")
            for dt in dt_list:
                name = dt.find("h4").string
                ts = dt.find("p").string
                print(f"产品: {name}---特色:{ts}")
response = requests.get(url)
tree = etree.HTML(response.text)
li_list = tree.xpath("//div[@class='wrap']/div/ul[@class='tab-bd']/li")

for i in li_list:
    print(i)
