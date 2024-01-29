import requests


login_url = "https://login2.scrape.center/login?next=/"

session = requests.session()

login_data  = {
    "username":"admin",
    "password":"admin"
}
session.post(login_url, data=login_data)
main_url = "https://login2.scrape.center/"
response = session.get(main_url)
print(response.text)
