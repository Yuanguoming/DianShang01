import unittest

# 测试类
from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay
from tool.get_log import GetLog

log = GetLog().get_log()


class TestPay(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化PageLogin类并调用登录成功方法
        PageLogin(self.driver).page_login_success()
        # 实例化获取PagePay对象 -->在测试方法中，调用支付业务、断言方法
        self.pay = PagePay(self.driver)
        # 点击首页
        self.pay.base_click_index()

    # 结束方法
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 测试方法
    def test_pay(self):
        try:
            # 调用支付业务方法
            self.pay.page_pay()
            # 断言方法
            self.assertIn("订单提交成功", self.pay.page_get_payment_result())
        except Exception as e:
            # 截图、日志
            self.pay.base_get_image()
            log.error(e)
