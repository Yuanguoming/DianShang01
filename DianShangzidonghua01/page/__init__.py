from selenium.webdriver.common.by import By
"""tpshop临时服务器url"""
url = "http://localhost"
"""以下为登录模块配置数据"""
# 登录连接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 异常提示信息
login_error_info = By.CSS_SELECTOR, ".layui-layer-content"
# 异常提示框 确定
login_error_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
# 获取昵称
login_nickname = By.CSS_SELECTOR, ".userinfo"
# 安全退出
login_logout = By.PARTIAL_LINK_TEXT, "安全退出"

"""以下为购物车配置数据"""
# 回到首页
cart_index = By.CSS_SELECTOR, ".logo>img"
# 输入商品
cart_input_goods = By.CSS_SELECTOR, "#q"
# 点击搜索按钮
cart_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
# 添加购物车 --》跳转详情
cart_add_cart_info = By.CSS_SELECTOR, ".p-btn>a"
# 添加购物车
cart_add_cart = By.CSS_SELECTOR, "#join_cart"
# 获取添加提示信息
cart_add_result = By.CSS_SELECTOR, ".conect-title>span"
# 关闭提示窗口
cart_close_window = By.CSS_SELECTOR, ".layui-layer-close"
# frame 窗口id 此处是个变量
cart_iframe_id = "layui-layer-iframe1"
# frame 窗口name 此处是元素
cart_iframe_element = By.CSS_SELECTOR, "#layui-layer-iframe1"

"""以下为订单模块配置数据"""
# 我的购物车
order_my_cart = By.CSS_SELECTOR, ".c-n"
# 全选
order_all = By.CSS_SELECTOR, ".checkCartAll"
# 去结算
order_account = By.CSS_SELECTOR, ".gwc-qjs"
# 收货人
order_person = By.CSS_SELECTOR, ".consignee>b"
# 提交订单
order_submit = By.CSS_SELECTOR, ".Sub-orders"
# 获取结果
order_result = By.CSS_SELECTOR, ".erhuh>h3"

"""以下为支付模块配置数据"""
# 我的订单
pay_my_order = By.PARTIAL_LINK_TEXT, "我的订单"
# 我的订单 title 注意：此处是个变量
pay_title_my_order = "我的订单"
# 立即支付
pay_now_payment = By.CSS_SELECTOR, ".ps_lj"
# 货到付款页面title
pay_title_pay_on = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
# 货到付款
pay_on_delivery = By.CSS_SELECTOR, '[value="pay_code=cod"]'
# 确认支付方式
pay_confirm_payment = By.CSS_SELECTOR, ".button-confirm-payment"
# 获取支付结果  订单提交成功，我们将在第一时间给你发货！
pay_get_result = By.CSS_SELECTOR, ".erhuh>h3"