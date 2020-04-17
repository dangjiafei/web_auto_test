"""存储每个页面的通用行为"""
import os
from selenium.webdriver.support.select import Select
from common.handle_log import log
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf import Setting


class BasePage(object):
    def __init__(self, driver: Chrome):
        self.driver = driver

    def get_element(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
            return e
        except NoSuchElementException as e:
            log.error("查找元素失败")
            log.exception(e)
            raise e

    def screen_shot(self, error_info):
        """保存截图"""
        img_path = Setting.img_path
        filename = error_info + '.png'
        file = os.path.join(img_path, filename)
        self.driver.save_screenshot(file)
        return file

    def wait_clickable_element(self, locator, timeout=30, poll=0.2):
        """等待元素可以被点击"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.element_to_be_clickable(locator)
            )
            return e
        except TimeoutException as e:
            log.error("时间超时")
            log.exception(e)
            raise e

    def wait_presence_element(self, locator, timeout=30, poll=0.2):
        """等待元素存在页面中,但不一定可见"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_element_located(locator)
            )
            return e
        except TimeoutException as e:
            log.error("时间超时")
            log.exception(e)
            raise e

    def wait_visible_element(self, locator, timeout=30, poll=0.2):
        """等待元素可见"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.visibility_of_element_located(locator)
            )
            return e
        except TimeoutException as e:
            log.error("时间超时")
            log.exception(e)
            raise e

    def user_input(self, name_prop, data):
        """
        用户输入框
        :param name_prop: name的属性
        :param data: 输入的值
        """
        e = self.driver.find_element_by_name(name_prop)
        e.send_keys(data)

    def click(self, locator):
        """click点击"""
        e = self.wait_clickable_element(locator)
        e.click()

    def selector_action(self, locator, data):
        """
        selector动作
        :param locator: 元素定位
        :param data: 选择的value值
        :return:
        """
        try:
            e = self.wait_visible_element(locator)
            select = Select(e)
            select.select_by_value(data)
        except Exception as e:
            log.error("选择框有误")
            log.exception(e)
            raise e

    def switch_i_frame(self, name):
        """i_frame的切换"""
        self.driver.switch_to.frame(name)

    def double_click(self, locator):
        """双击操作"""
        try:
            e = self.wait_clickable_element(locator)
            action = ActionChains(self.driver)
            action.double_click(e)
            action.perform()
        except Exception as e:
            log.error("查找元素失败")
            log.exception(e)
            raise e

    def hover(self, locator):
        """悬停操作"""
        try:
            e = self.wait_visible_element(locator)
            action = ActionChains(self.driver)
            action.move_to_element(e)
            action.perform()
        except Exception as e:
            log.error("查找元素失败")
            log.exception(e)
            raise e

    def right_click(self, locator):
        """右键点击"""
        try:
            e = self.wait_visible_element(locator)
            action = ActionChains(self.driver)
            action.context_click(e)
            action.perform()
        except Exception as e:
            log.error("查找元素失败")
            log.exception(e)
            raise e

    def drag_and_drop(self, locator_one, locator_two):
        """拖拽操作"""
        try:
            start = self.wait_visible_element(locator_one)
            end = self.wait_visible_element(locator_two)
            action = ActionChains(self.driver)
            action.drag_and_drop(start, end)
            action.perform()
        except Exception as e:
            log.error("查找元素失败")
            log.exception(e)
            raise e

    def window_to_bottom(self):
        """窗口滑到底部"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def upload_file(self, locator, file):
        """上传文件"""
        try:
            e = self.wait_visible_element(locator)
            e.send_keys(file)
        except Exception as e:
            log.error("查找元素失败")
            log.exception(e)
            raise e

    def send_js_code(self, locator, js_code):
        """发送js代码"""
        e = self.wait_visible_element(locator)
        self.driver.execute_script(js_code, e)
