"""测试登录功能
流程:
    1，启动浏览器，打开url;
    2, 定位用户名；
    3， 输入用户名；
    4， 定位密码；
    5， 输入密码；
    6， 定位登录按钮；
    7， 点击登录按钮；
    8，定位错误信息断言
"""
import time
import unittest
from library.ddt import data, ddt
from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.test_data import login_data_error, login_data_invalid, login_data_success


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self) -> None:
        self.driver.quit()

    @data(*login_data_error)
    def test_login_username_is_empty(self, test_info):
        # 预期结果
        expected = test_info["expected"]
        # 实际结果
        LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
        # 断言
        error_msg = LoginPage(self.driver).get_error_msg()
        try:
            self.assertEqual(error_msg, expected)
        except AssertionError as e:
            raise e

    @data(*login_data_invalid)
    def test_login_invalid_user(self, test_info):
        expected = test_info['expected']
        LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
        invalid_msg = LoginPage(self.driver).get_invalid_msg()
        try:
            self.assertEqual(invalid_msg, expected)
        except AssertionError as e:
            raise e

    @data(*login_data_success)
    def test_login_success_user(self, test_info):
        expected = test_info['expected']
        LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
        # 跳转到首页
        # 定位首页的元素
        # 隐式等待能不能等待新页面出现
        # 显示等待，强制等待，等待新页面出现
        time.sleep(0.3)

        account_msg = HomePage(self.driver).get_user_info()
        try:
            self.assertEqual(account_msg, expected)
        except AssertionError as e:
            raise e
