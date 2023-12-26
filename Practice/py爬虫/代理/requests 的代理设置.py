import requests


proxypool_url = 'http://127.0.0.1:5555/random'
def get_random_proxy():

    return requests.get(proxypool_url).text.strip()


# proxy = '123.57.1.16:8029'
proxy = '39.165.0.137:9002'
# proxy = get_random_proxy()
print(proxy)
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
try:
    # response = requests.get('http://httpbin.org/get', proxies=proxies)
    response = requests.get('https://www.baidu.com/', headers=headers, proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

