import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder
from tool.get_log import GetLog

# 获取日志器
log = GetLog().get_log()


class TestOrder(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化 PageLogin 并调用登录
        PageLogin(self.driver).page_login_success()
        # 获取PageOrder对象
        self.order = PageOrder(self.driver)
        # 打开首页
        self.order.base_click_index()

    # 结束方法
    def tearDown(self):
        GetDriver().quit_driver()

    # 测试订单方法
    def test_order(self):
        try:
            # 调用 订单业务流程
            self.order.page_order()
            # 断言
            self.assertIn("订单提交成功", self.order.page_get_order_result())
        except Exception as e:
            # 日志、截图
            log.error(e)
            self.order.base_get_image()