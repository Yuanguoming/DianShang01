# 导包
import unittest
import time
from tool.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("../scripts", pattern="test*.py")
# 获取报告存储文件流 调用run方法
with open("../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S")), "wb") as f:
    HTMLTestRunner(stream=f).run(suite)