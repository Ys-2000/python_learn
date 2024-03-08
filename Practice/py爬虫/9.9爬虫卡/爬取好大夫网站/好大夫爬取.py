import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def seve(datalist):
    csv_headers = ['医生姓名', '推荐度', '职称', '科室', '疗效', '态度', '擅长', '问诊', '挂号']
    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        writer.writerows(datalist)
    print("保存成功")
    # pd.DataFrame(datalist,columns=datalist).to_csv(f'haodf.csv',index=False,encoding='utf-8-sig')


# 解析科室
def parse_doctor_list(diqu,keshi):
    page = 1
    datalist = []
    while True:
        url = f"https://www.haodf.com/doctor/list-{diqu}-{keshi}.html"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Referer": "https://www.haodf.com/doctor/list-37-kouqiangke-zonghe.html?p=2",
            "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        params = {
            "p": page
        }
        response = requests.get(url, params=params, headers=headers).text
        soup = BeautifulSoup(response, "lxml")
        doclist = soup.find("div",class_="d-doc-list").find("ul",class_="fam-doc-ul").find_all("li")
        if len(doclist) == 0 or page > 3:  # or p>=5设置了另一种停下来得方式  演示效果4页就够了
            break
        for doc in doclist:
            # 医生名称
            doc_name = doc.find("div", class_="d-doc-content").find("span",class_="doc-name").text.strip()
            # 病友推荐度
            tjd = doc.find("div", class_="d-doc-content").find("p").find_all("span",class_="ml5")[1].get_text(strip=True)
            # 职位
            zw = "、".join(doc.find("div", class_="d-doc-content").find("span",class_="ml15").text.strip().split())
            # 医院科室
            yiyuan = doc.find("div", class_="d-doc-content").find("p",class_="mt5").get_text(" ", strip=True)
            # 疗效
            liaoxiao = doc.find("div", class_="d-doc-content").find("div",class_="vote clearfix mt5").find("p",class_="liaoxiao").get_text(strip=True)
            # 态度
            taidu = doc.find("div", class_="d-doc-content").find("div",class_="vote clearfix mt5").find("p",class_="taidu ml20").get_text(strip=True)
            # 擅长
            sc = " ".join(doc.find("div", class_="d-doc-content").find("p",class_="mt5 doc-speciaty").get_text(strip=True).split())
            # 问诊
            zxwz = doc.find("div", class_="d-doc-content").find("span",class_="wenzhen mt5").get_text(strip=True)
            # 挂号
            guahao = doc.find("div", class_="d-doc-content").find("span",class_="guahao mt5").get_text(strip=True)
            datalist.append([doc_name,tjd,zw,yiyuan,liaoxiao,taidu,sc,zxwz,guahao])
        print(page,'done...')
        page += 1
    return datalist


# 获取科室信息
def get_keshi():
    url = "https://m.haodf.com/ndoctor/ajaxfacultylist?randomNumber=021823756060752375"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Referer": "https://www.haodf.com/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    response = requests.get(url, headers=headers).json()
    json = response.get("data")
    for kslist in json:
        keshi = kslist.get("childFaculty")
        for ks in keshi:
            # keshi_id = ks.get("id")
            keshi_key = ks.get("key")
            keshi_name = ks.get("name")
            yield keshi_key



# # 获取全国城市信息
def get_diqu():

    url = "https://m.haodf.com/nindex/home/AjaxAreaList"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Referer": "https://www.haodf.com/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    response = requests.get(url, headers=headers).json()
    diqu_info = response.get("data")
    for diqu in diqu_info:
        diqu_name = diqu.get("placeName")
        diqu_id = diqu.get("placeId")
        yield diqu_id
        # print(diqu_name,diqu_id)
        # for city in diqu.get("children")[1:]:
        #     city_name = city.get("placeShortName")
        #     city_id = city.get("placeId")
        #     diqu_list.append(city_id)
        #     # print(city_name,city_id)


if __name__ == '__main__':
    for diqu in get_diqu():
        for keshi in get_keshi():
            datalist = parse_doctor_list(diqu, keshi)
            seve(datalist)
            print(f"{diqu},{keshi}存储完成")
            break
        break