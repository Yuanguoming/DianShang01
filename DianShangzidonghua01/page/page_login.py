from base.base import Base
import page


class PageLogin(Base):
    # 点击登录连接方法
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名 方法
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.base_input(page.login_verify_code, code)

    # 点击登录 按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_error_info)

    # 点击异常提示框 确定按钮
    def page_click_error_btn(self):
        self.base_click(page.login_error_btn)

    # 获取登录后昵称 登录成功
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 点击 安全退出
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 判断是否退出成功 注意：必须将True或False返回
    def page_if_logout_success(self):
        return self.base_if_is_not_exist(page.login_link)

    # 组合业务方法
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()

    # 以下依赖登录成功方法 给：购物车、订单、支付模块使用
    def page_login_success(self, username="13800001111", pwd="123456", code="8888"):
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()