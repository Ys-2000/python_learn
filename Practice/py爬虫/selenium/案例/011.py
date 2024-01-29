# # 电影数据网站，无反爬，数据通过 Ajax 加载，无页码翻页，下拉至底部刷新，适合 Ajax 分析和动态页面渲染爬取。


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://spa3.scrape.center/"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome()
# driver.maximize_window()

try:
    driver.get(url)
    # 等待直到指定的元素出现
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "index"))
    )

    print("等待2秒")
    time.sleep(2)  # 等待页面加载

    # 点击页面空白处
    body = driver.find_element(By.TAG_NAME,"body")
    body.click()

    # 创建一个动作链
    actions = ActionChains(driver)
    print("长按20s")
    # 按住 PageDown 键
    actions.key_down(Keys.PAGE_DOWN, body)

    # 执行动作链
    actions.perform()

    # 等待一段时间，模拟长按持续的时间
    time.sleep(10)  # 你可以根据需要调整等待时间

    # 释放 PageDown 键
    actions.key_up(Keys.PAGE_DOWN, body)
    print("长按结束")
    # 执行动作链
    actions.perform()


    # while True:
    #     # 模拟向下滚动
    #     driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    #     time.sleep(1)  # 等待加载




    # for i in range(5):
    #     # window.scrollTo() 方法用于控制浏览器窗口的滚动。
    #     # 0 表示水平方向的滚动位置，这里设为0表示不进行水平滚动。
    #     # document.body.scrollHeight 表示文档的实际高度，即页面的总高度。通过将垂直滚动位置设置为页面总高度，可以实现将页面滚动到底部的效果
    #     # 等待页面加载（可选）
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # 这段JavaScript代码，现了将页面滚动到底部的操作
    #     time.sleep(2)



    # # 获取页面内容
    # page_content = driver.page_source
    # print(page_content)  # 输出页面内容，可以根据需要进行解析和处理

finally:
    print("3秒后退出")
    time.sleep(3)
    driver.close()
    driver.quit()