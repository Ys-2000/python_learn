# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Edge()
# try:
#     browser.get('https://www.baidu.com')
#     # input = browser.find_element_by_id('kw')
#     input = browser.find_element(By.ID,'kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)       # 等待直到特定条件满足或超时为止
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))     #等待页面加载完毕并且具有ID为'content_left'的元素出现，然后继续执行后续的操作
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# browser = webdriver.Edge()
wait = WebDriverWait(browser, 20)

def search():
    try:
        browser.get('https://www.taobao.com/')
        # 等待直到特定条件满足或超时为止
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))) #等待页面加载完毕,然后继续执行后续的操作
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div.PageContent--contentWrap--mep7AEm > div.LeftLay--leftWrap--xBQipVc > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > span.next-pagination-display')))
        return total.text
    except TimeoutError:
        return search()


def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div.PageContent--contentWrap--mep7AEm > div.LeftLay--leftWrap--xBQipVc > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > span.next-input.next-medium.next-pagination-jump-input > input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div.PageContent--contentWrap--mep7AEm > div.LeftLay--leftWrap--xBQipVc > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > button.next-btn.next-medium.next-btn-normal.next-pagination-jump-go')))
        input.clear()       # 清除输入框内容
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div.PageContent--contentWrap--mep7AEm > div.LeftLay--leftWrap--xBQipVc > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > div > button.next-btn.next-medium.next-btn-normal.next-pagination-item.next-current'), str(page_number)))
    except TimeoutError:
        next_page(page_number)


def main():
    total = int(search()[-3:])
    for i in range(2, total+1):
        next_page(i)


if __name__ == '__main__':
    main()