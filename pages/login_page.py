from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, pwd):
        """登录操作"""
        login_url = "http://120.78.128.25:8765/Index/login.html"
        self.driver.get(login_url)

        # 手机号输入框
        mobile_locator = (By.NAME, 'phone')
        user_elem = self.driver.find_element(*mobile_locator)
        user_elem.send_keys(username)

        # 密码输入框
        pwd_locator = (By.NAME, 'password')
        pwd_elem = self.driver.find_element(*pwd_locator)
        pwd_elem.send_keys(pwd)

        # 登录按钮
        login_locator = (By.XPATH, "//button[contains(text(), '登录')]")
        login_button = self.driver.find_element(*login_locator)
        login_button.click()

    def get_error_msg(self):
        """获取错误信息"""
        error_info_locator = (By.XPATH, '//div[@class="form-error-info"]')
        error_elem = self.driver.find_element(*error_info_locator)
        return error_elem.text

    def get_invalid_msg(self):
        """获取未授权信息"""
        invalid_info_locator = (By.CLASS_NAME, "layui-layer-content")
        invalid_elem = self.driver.find_element(*invalid_info_locator)
        return invalid_elem.text
