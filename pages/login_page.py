from selenium.webdriver.common.by import By
from common.base_page import BasePage
from conf import Setting


class LoginPage(BasePage):
    """登录页面"""
    url = '/Index/login.html'
    mobile_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    login_locator = (By.XPATH, "//button[contains(text(), '登录')]")
    error_info_locator = (By.XPATH, '//div[@class="form-error-info"]')
    invalid_info_locator = (By.CLASS_NAME, "layui-layer-content")

    def get(self):
        """访问登录页面"""
        login_url = Setting.host + self.url
        self.driver.get(login_url)

    def login(self, username, pwd):
        """登录操作"""
        self.get()

        # 手机号输入框
        user_elem = self.get_element(*self.mobile_locator)
        user_elem.send_keys(username)

        # 密码输入框
        pwd_elem = self.get_element(*self.pwd_locator)
        pwd_elem.send_keys(pwd)

        # 登录按钮
        login_button = self.get_element(*self.login_locator)
        login_button.click()

    def get_error_msg(self):
        """获取错误信息"""
        error_elem = self.get_element(*self.error_info_locator)
        return error_elem.text

    def get_invalid_msg(self):
        """获取未授权信息"""
        invalid_elem = self.get_element(*self.invalid_info_locator)
        return invalid_elem.text
