import page

from base.base import Base


class PageCart(Base):
    # 输入商品
    def page_input_goods(self, goods):
        self.base_input(page.cart_input_goods, goods)

    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click(page.cart_search_btn)

    # 点击添加购物车 -->跳转到商品详情
    def page_click_add_cart_info(self):
        self.base_click(page.cart_add_cart_info)

    # 点击添加购物车
    def page_click_add_cart(self):
        self.base_click(page.cart_add_cart)

    # 获取添加成功信息
    def page_get_success_info(self):
        # 切换frame id：切换会有bug
        # self.base_switch_frame(page.cart_iframe_id)
        # 推荐使用元素 第一步：获取iframe元素
        el = self.base_find(page.cart_iframe_element)
        # 第二步使用元素切换
        self.base_switch_frame(el)
        return self.base_get_text(page.cart_add_result)

    # 关闭窗口
    def page_close_window(self):
        # 恢复默认目录
        self.base_default_content()
        # 点击关闭
        self.base_click(page.cart_close_window)

    # 组合添加购物车业务方法
    def page_cart(self, goods):
        self.page_input_goods(goods)
        self.page_click_search_btn()
        self.page_click_add_cart_info()
        self.page_click_add_cart()