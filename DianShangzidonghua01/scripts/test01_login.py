import unittest

from parameterized import parameterized

from base.get_driver import GetDriver
from page.page_login import PageLogin
from tool.read_txt import read_txt
from tool.get_log import GetLog


# 获取日志器
log = GetLog().get_log()


def get_data():
    # 新建空列表
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1::]


class TestLogin(unittest.TestCase):
    driver = None

    # 初始化方法
    @classmethod
    def setUpClass(cls):
        # 获取driver对象
        cls.driver = GetDriver().get_driver()
        # 实例化获取PageLogin对象
        cls.login = PageLogin(cls.driver)
        # 点击登录连接
        cls.login.page_click_login_link()

    # 结束方法
    @classmethod
    def tearDownClass(cls):
        # 关闭driver
        GetDriver().quit_driver()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, success, expect):
        # 调用登录组合业务方法
        self.login.page_login(username, pwd, code)
        # 判断是否为正向
        if success == "True":
            try:
                # 获取昵称
                nickname = self.login.page_get_nickname()
                print("昵称为：", nickname)
                self.assertEqual(expect, nickname)
                # 点击安全退出
                self.login.page_click_logout()
                # 点击登录连接
                self.login.page_click_login_link()
            except Exception as e:
                log.error(e)
        # 否则
        else:
            try:
                # 获取异常提示信息
                error_msg = self.login.page_get_error_info()
                print("错误提示异常信息：", error_msg)
                self.assertEqual(expect, error_msg)
            except Exception as e:
                # 截图
                self.login.base_get_image()
                print("错误原因：" ,e)
                # 日志
                log.error(e)
                # 抛异常
                raise
            finally:
                # 点击异常提示框按钮
                self.login.page_click_error_btn()
