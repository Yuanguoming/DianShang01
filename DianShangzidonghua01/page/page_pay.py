from base.base import Base
import page


class PagePay(Base):
    # 点击 我的订单
    def page_click_my_order(self):
        self.base_click(page.pay_my_order)

    # 点击 立即支付
    def page_click_now_payment(self):
        # 必须切换窗口
        self.base_switch_to_window(page.pay_title_my_order)
        # 点击立即支付按钮
        self.base_click(page.pay_now_payment)

    # 货到付款
    def page_pay_on_delivery(self):
        # 必须切换窗口
        self.base_switch_to_window(page.pay_title_pay_on)
        # 选择货到付款
        self.base_click(page.pay_on_delivery)

    # 确认支付方式
    def page_confirm_payment(self):
        self.base_click(page.pay_confirm_payment)

    # 获取支付结果
    def page_get_payment_result(self):
        return self.base_get_text(page.pay_get_result)

    # 组合业务方法
    def page_pay(self):
        self.page_click_my_order()
        self.page_click_now_payment()
        self.page_pay_on_delivery()
        self.page_confirm_payment()
