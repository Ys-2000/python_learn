from selenium import webdriver
import time

browser = webdriver.Edge()
browser.get('https://www.zhihu.com/explore')
browser.maximize_window()        # 将当前的浏览器窗口最大化
# 这里就利用 execute_script 方法将进度条下拉到最底部，然后弹出 alert 提示框。所以说有了这个方法，基本上 API 没有提供的所有功能都可以用执行 JavaScript 的方式来实现了。
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom!!!")')
time.sleep(2)
browser.switch_to.alert.dismiss()       # 关闭弹窗
time.sleep(5)
browser.close()
browser.quit()       # 关闭所有窗口并退出浏览器