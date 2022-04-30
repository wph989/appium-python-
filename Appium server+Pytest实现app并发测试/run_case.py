# _*_ coding：utf-8 _*_
# @Time     : 2022/4/28 11:41
# @Author   : WPH
# @File     : run_case.py
# @Software : PyCharm

import pytest
import os
from multiprocessing import Pool

# (appium_server 端口号，手机设备名称， 日志名称， allure存放文件， allure_report存放文件）
device_infos = [
                ('4723', 'emulator-5554', '一号测试机', 'allure0', 'allure0_report'),
                ('4725', 'emulator-5556', '二号测试机', 'allure1', 'allure1_report')
]


def main(device_info):
    pytest.main(["--cmdopt={0}".format(device_info),
                 "--alluredir", "./{}".format(device_info[3]), "--clean-alluredir", "-vs"])
    os.system("allure generate {0} -o {1} --clean".format(device_info[3], device_info[4]))


if __name__ == "__main__":
    with Pool(2) as pool:
        pool.map(main, device_infos)
        pool.close()
        pool.join()
