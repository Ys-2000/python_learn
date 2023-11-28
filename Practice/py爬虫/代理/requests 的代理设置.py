import requests

proxy = '123.169.36.67:9999'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy,
}

try:
    response = requests.get('https://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
