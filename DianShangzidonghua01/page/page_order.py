from base.base import Base
import page


class PageOrder(Base):

    # 点击我的购物车
    def page_click_my_cart(self):
        self.base_click(page.order_my_cart)

    # 点击全选
    def page_click_all_select(self):
        # 获取全选按钮元素
        el = self.base_find(page.order_all)
        # 判断是否没有选中
        if not el.is_selected():
            # 条件成立说明没选中，没选中要点击
            el.click()

    # 点击去结算
    def page_click_account(self):
        self.base_click(page.order_account)

    # 提交订单
    def page_submit_order(self):
        # 查找收货人 -->等待收货人加载出来
        self.base_find(page.order_person)
        # 点击提交订单
        self.base_click(page.order_submit)

    # 获取下订单结果
    def page_get_order_result(self):
        return self.base_get_text(page.order_result)

    # 组合业务方法
    def page_order(self):
        self.page_click_my_cart()
        self.page_click_all_select()
        self.page_click_account()
        self.page_submit_order()