# _*_ coding：utf-8 _*_
# @Time     : 2022/4/29 9:17
# @Author   : WPH
# @File     : conftest.py
# @Software : PyCharm
import pytest
from PageObject.login_page import LoginPage

@pytest.fixture(scope="class")
def page_driver(common_driver):
    log = common_driver[1]
    log.info('================ 开始执行 < 登录模块 > 测试用例================')
    global driver
    driver = LoginPage(common_driver)
    yield driver
    log.info('================ 结束 < 登录模块 > 测试用例================')
