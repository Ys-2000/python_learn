import requests
import brotli


"""
响应头中Content-Encoding: br：这表明响应内容使用了Brotli压缩。因此，在尝试解码内容之前，你需要先对其进行解压缩。
Content-Type: text/html; charset=GB2312：这表明内容使用了GB2312编码。在解压缩之后，你应该使用GB2312编码来解码内容。

在网络传输中，"内容被压缩"指的是数据在发送到客户端之前，通过特定的压缩算法进行了压缩处理，以减少数据大小，加快传输速度。这在处理大量数据的网页或API响应时尤其常见。压缩的内容需要在客户端被解压缩才能正确解读。
在你的案例中，响应头中的 Content-Encoding: br 表示服务器使用了Brotli算法压缩了内容。Brotli是一种广泛使用的压缩算法，特别适用于文本数据的压缩。
为了获取原始数据，你需要在Python中对这个Brotli压缩的内容进行解压缩。这通常可以通过使用相应的解压缩库来实现。例如，使用Python的 brotli 模块：
"""

main_url = "https://www.xqb5200.com/38_38021/"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "Hm_lvt_dfdb6e2e4cbe6169e47615f0e6c44d3d=1705641085; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1705641085; jieqiVisitInfo=jieqiUserLogin%3D1705643099%2CjieqiUserId%3D127425; clickbids=38021,109340; jieqiVisitId=article_articleviews%3D87285%7C38021%7C109340; Hm_lpvt_dfdb6e2e4cbe6169e47615f0e6c44d3d=1705644312; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1705644312",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url=main_url, headers=headers)


# print(response.headers)
# print(response.headers.get('Content-Type'))        # 获取响应内容编码格式

# 解压缩Brotli编码的内容
decompressed_content = brotli.decompress(response.content)

# 使用GB2312编码解码文本
text_content = decompressed_content.decode('gb2312', errors='replace')

print(text_content)




