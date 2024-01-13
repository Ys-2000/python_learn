import unittest
from selenium import webdriver
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # 使用 Chrome 浏览器
        cls.driver.implicitly_wait(10)   # 隐式等待 10 秒

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_success(self):
        """登录成功测试用例"""
        self.driver.get('http://specmaplinux.shuwantech.com/_builder')
        self.driver.find_element_by_name('email').send_keys('Sw_admin@qq.com')
        self.driver.find_element_by_name('password').send_keys('qwe123')
        self.driver.find_element_by_name('action').click()
        # self.driver.find_element_by_css_selector('button[type="submit"]').click()
        time.sleep(3)   # 等待页面加载
        # 验证是否登录成功，根据实际业务逻辑编写
        self.assertIn('0316', self.driver.page_source)

    def test_login_fail(self):
        """登录失败测试用例"""
        self.driver.get('http://specmaplinux.shuwantech.com/_builder')
        self.driver.find_element_by_name('email').send_keys('Sw_admin@qq.com')
        self.driver.find_element_by_name('password').send_keys('qeasd1223')
        self.driver.find_element_by_name('action').click()
        time.sleep(3)   # 等待页面加载
        # 登录失败断言，验证源代码中包含XX字段
        self.assertIn('登录您的账号', self.driver.page_source)

if __name__ == '__main__':
    unittest.main()
