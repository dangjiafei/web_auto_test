from selenium.webdriver.common.by import By
from common.base_page import BasePage


class HomePage(BasePage):
    user_locator = (By.XPATH, "//a[@href='/Member/index.html']")

    def get_user_info(self):
        """获取账号信息"""
        user_ele = self.get_element(self.user_locator)
        return user_ele.text
