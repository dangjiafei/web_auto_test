"""conftest.py 文件名称是固定的,统一存放 fixture 的地方"""
import pytest
from selenium import webdriver


# 测试夹具, 用来做浏览器的初始化动作, scope="class"相当于unittest的setUpClass
@pytest.fixture(scope="class")
def init_web():
    """
    # 设置无头浏览器的路径, 如果需要集成jenkins，需要此步骤让jenkins发现浏览器并执行
    from selenium.webdriver import ChromeOptions
    option = ChromeOptions()
    option.binary_location = r"C:\Users\AAA\AppData\Local\Google\Chrome\Application\chrome.exe"
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
