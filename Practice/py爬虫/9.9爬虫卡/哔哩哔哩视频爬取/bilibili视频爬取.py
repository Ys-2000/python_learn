import re
import requests
import os
import csv
import logging




# # 更换要下载的B站视频url
# url = "https://www.bilibili.com/video/BV17K411a79A/?spm_id_from=333.1007.tianma.6-3-19.click"

# 读取CSV文件中的视频URL
def read_csv_file(file_path):
    videos = []
    with open(file_path, 'r', encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            videos.append(row[0].strip())
    return videos

def remove_invalid_chars(text):
    # valid_chars = r'[\\/:*?"<>|]'

    valid_chars = r'[ \\/:*?"<>|]'                  # 去除了标题中的空格，不然ffmpeg会报错
    return re.sub(valid_chars, '_', text)


def main(url):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    headers = {
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    source_code = response.text
    # print(source_code)

    # 获取标题
    title_pattern = r'<h1 title="(.*?)"'
    tit = re.findall(title_pattern, source_code)[0]
    title = remove_invalid_chars(tit).strip()    # 去除特殊字符

    logging.info(f"正在请求: {url}")
    # 定义正则表达式模式来匹配 baseUrl
    video_pattern = r'"video":\s*\[\s*{[^{}]*?"base_url":\s*"([^"]*)"'
    audio_pattern = r'"audio":\s*\[\s*{[^{}]*?"base_url":\s*"([^"]*)"'

    # 使用正则表达式查找所有匹配的 baseUrl
    video_url = re.findall(video_pattern, source_code)[0]
    audio_url = re.findall(audio_pattern, source_code)[0]

    # 下载视频
    video_response = requests.get(video_url,headers=headers)
    with open("video.m4s","wb") as f:
        f.write(video_response.content)
        logging.info("视频下载完成!")
    # 下载音频
    audio_response = requests.get(audio_url,headers=headers)
    with open("audio.m4s","wb") as f:
        f.write(audio_response.content)
        logging.info("音频下载完成!")

    # 使用ffmpeg合并视频和音频
    # os.system(f"ffmpeg -i audio.m4s -i video.m4s -acodec copy -vcodec copy {title}.mp4")
    os.system(f"ffmpeg -i audio.m4s -i video.m4s -acodec copy -vcodec copy -loglevel quiet {title}.mp4")    # -loglevel quiet不会输出任何日志信息

    logging.info(f"文件名: {title}下载完成!")


if __name__ == '__main__':
    file_path = "url.csv"
    urls = read_csv_file(file_path)
    for url in urls:
        main(url)