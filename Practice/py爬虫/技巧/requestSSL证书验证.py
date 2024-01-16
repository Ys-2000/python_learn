import requests

# SSL证书验证
response = requests.get('https://ssr2.scrape.center/', verify=False,timeout=7)    # 使用 verify 参数控制是否验证证书，如果将其设置为 False，在请求时就不会再验证证书是否有效。如果不加 verify 参数的话，默认值是 True，会自动验证。
print(response.status_code)