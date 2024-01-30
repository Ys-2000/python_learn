import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # 创建 Chrome WebDriver 实例
    driver = webdriver.Chrome()
    yield driver
    # 测试用例执行完毕后关闭 WebDriver
    driver.quit()

def test_example(browser):
    # 在浏览器中打开网页
    browser.get("https://www.example.com")
    # 断言网页标题是否正确
    assert "Example Domain" in browser.title
