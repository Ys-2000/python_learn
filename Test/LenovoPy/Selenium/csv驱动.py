import csv
import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        with open('testdata.csv') as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                username = row[0]
                password = row[1]
                self.driver.get('http://specmaplinux.shuwantech.com/_builder')
                self.driver.find_element_by_name('username').send_keys(username)
                self.driver.find_element_by_name('password').send_keys(password)
                self.driver.find_element_by_name('action').click()
                # 验证登录是否成功，根据实际业务逻辑编写
                self.assertIn('0316', self.driver.page_source)
