import requests

url = "https://www.che168.com/nlist/jinan/list/?pvareaid=100533"
# url = "https://www.tupianzj.com/bizhi/DNmeinv/"
resp = requests.get(url)
print(resp.text)