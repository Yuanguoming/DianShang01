# 导包
import unittest


# 新建测试类
from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin
from tool.get_log import GetLog

# 获取日志器
log = GetLog().get_log()


class TestCart(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化PageLogin并调用登录方法
        PageLogin(self.driver).page_login_success()
        # 获取PageCart对象
        self.cart = PageCart(self.driver)
        # 回到首页
        self.cart.base_click_index()

    # 结束方法
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 购物测试方法
    def test_cart(self, goods="小米手机", expect="添加成功"):
        try:
            # 调用 购物车组合业务方法
            self.cart.page_cart(goods)
            # 断言
            self.assertIn(expect, self.cart.page_get_success_info())
            # 关闭
            self.cart.page_close_window()
        except Exception as e:
            # 日志、截图
            log.error(e)
            self.cart.base_get_image()