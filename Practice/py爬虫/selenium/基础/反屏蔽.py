from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions
import time


option = EdgeOptions()      # 创建了一个 EdgeOptions 对象，用于配置 Edge 浏览器的选项
option.add_experimental_option('excludeSwitches', ['enable-automation'])    # 排除了浏览器的 'enable-automation' 选项，以减少被检测为自动化的风险
option.add_experimental_option('useAutomationExtension', False)     # 禁用了自动化扩展
browser = webdriver.Edge(options=option)    # 创建了一个 Edge WebDriver 实例，并将上述选项应用于浏览器
# browser = webdriver.Chrome()
try:
    # 使用 browser.execute_cdp_cmd 方法，执行了一个 Chrome DevTools Protocol (CDP) 命令，该命令将在每个新文档（页面加载）上执行一个 JavaScript 脚本。这个脚本将浏览器的 navigator.webdriver 属性设置为 undefined，以减少被检测为自动化的风险
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })
    browser.get('https://antispider1.scrape.center/')


finally:
    time.sleep(3)
    browser.close()
    browser.quit()