"""conftest.py 文件名称是固定的,统一存放 fixture 的地方"""
import pytest
from selenium import webdriver


# 测试夹具, 用来做浏览器的初始化动作, scope="class"相当于unittest的setUpClass
@pytest.fixture(scope="class")
def init_web():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
