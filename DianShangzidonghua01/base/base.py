from time import sleep

import page
from selenium.webdriver.support.wait import WebDriverWait
import time
from tool.get_log import GetLog


# 获取日志器
log = GetLog().get_log()


class Base:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver
        log.info("获取driver对象：{}".format(self.driver))

    # 查找元素方法
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找:{} 元素, 查找最多时间{}".format(loc, timeout))
        # 显示等待 返回元素
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        log.info("正在点击:{} 元素".format(loc))
        self.base_find(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        log.info("正在获取:{} 元素".format(loc))
        el = self.base_find(loc)
        log.info("正在对:{} 元素清空操作 clear".format(loc))
        # 清空操作
        el.clear()
        log.info("正在对:{} 元素进行输入：{} 值操作".format(loc, value))
        # 输入
        el.send_keys(value)

    # 获取提示信息方法
    def base_get_text(self, loc):
        log.info("正在获取:{} 元素文本值".format(loc))
        return self.base_find(loc).text

    # 判断元素是否存在
    def base_if_is_not_exist(self, loc):
        # 如果存在，返回true, 不存在返回false, 最多等待3秒；
        try:
            log.info("正在判断:{} 元素是否存在".format(loc))
            self.base_find(loc, timeout=3, poll=0.2)
            log.info("{} 元素--存在！".format(loc))
            return True  # 存在
        except:
            log.info("{} 元素--【不存在！】".format(loc))
            return False  # 不存在

    # 截图
    def base_get_image(self):
        log.info("断言错误，正在执行截图操作！")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 切换 frame
    def base_switch_frame(self, frame):
        # frame: id\name\元素 --->只能用元素
        self.driver.switch_to.frame(frame)

    # 恢复默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 打开首页方法
    def base_click_index(self):
        # 不推荐是用方法
        # sleep(2)
        # self.driver.get("http://localhost")

        # 推荐
        self.base_click(page.cart_index)

    # 切换窗口方法
    def base_switch_to_window(self, title):
        log.info("正在切换 title为：{} 的窗口".format(title))
        self.driver.switch_to.window(self.base_get_handle(title))
        log.info("执行切换 title为：{} 的窗口， 完成！！！".format(title))

    # 根据title获取handle方法
    def base_get_handle(self, tiltes):
        # 遍历 所有handler
        handls = self.driver.window_handles
        for handle in self.driver.window_handles:
            log.info("正在遍历 {} -->{}".format(handle, handls))
            # 切换到当前遍历的hander窗口
            self.driver.switch_to.window(handle)
            log.info("正在切换 handle为{} 窗口".format(handle))
            # 获取当前窗口title并判断是否等于 传进来的参数title
            if self.driver.title == tiltes:
                log.info("条件成立，返回handle：{}".format(self.driver.current_window_handle))
                # 条件成立 返回当前页面窗口handle
                return self.driver.current_window_handle