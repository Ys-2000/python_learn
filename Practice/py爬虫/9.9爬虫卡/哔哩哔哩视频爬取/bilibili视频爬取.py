import re
import requests
import os
import logging




# 更换要下载的B站视频url
# url = "https://www.bilibili.com/video/BV1da4y1k7VQ/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=9c584c7c4ae9bc74660cef42aafea9ae"

url = "https://www.bilibili.com/video/BV17K411a79A/?spm_id_from=333.1007.tianma.6-3-19.click"


def main():

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    headers = {
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    source_code = response.text
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
    os.system("ffmpeg -i audio.m4s -i video.m4s -acodec copy -vcodec copy bilibili.mp4")
    logging.info("视频下载完成!")

if __name__ == '__main__':
    main()