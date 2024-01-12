import requests
from bs4 import BeautifulSoup
import random

def main(num_agents=100, select_random=False):
    url = "https://useragentstring.com/pages/Chrome/"
    resp = requests.get(url).text
    soup = BeautifulSoup(resp,"lxml")
    ul_list = soup.find("div", id="liste").find_all("ul")

    UA_LIST = [ul.find("a").string for ul in ul_list]
    if select_random:
        return random.choice(UA_LIST[:num_agents])
    else:
        return UA_LIST[:num_agents]


if __name__ == '__main__':
    main()