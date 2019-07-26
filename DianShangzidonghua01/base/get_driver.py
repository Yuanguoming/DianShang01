import page
from selenium import webdriver


class GetDriver:
    driver = None
    # 获取dirver
    @classmethod
    def get_driver(cls):
        if not cls.driver:
            # 获取 浏览器驱动对象
            cls.driver = webdriver.Firefox()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(page.url)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空
            cls.driver = None