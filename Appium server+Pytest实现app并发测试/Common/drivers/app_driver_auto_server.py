# _*_ coding：utf-8 _*_
# @Time     : 2022/4/28 11:39
# @Author   : WPH
# @File     : app_driver.py
# @Software : PyCharm

import subprocess
from time import ctime
from appium import webdriver
import yaml

from Common.base.check_port import check_port, release_port
from Config.root_config import CONFIG_PATH, LOG_DIR


class BaseDriver(object):
    """获取driver"""

    def __init__(self, device_info, log):
        with open(CONFIG_PATH, 'r') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
        self.device_info = device_info
        self.log = log
        self.device_port = str(int(self.device_info[0]) + 1)

        cmd = "appium -a {0} -p {1} -bp {2} ".format(
            self.data["ip"],
            self.device_info[0],
            self.device_port
        )
        self.log.info('%s at %s' % (cmd, ctime()))
        if not check_port(self.data["ip"], int(self.device_info[0])):
            release_port(self.device_info[0])
        subprocess.Popen(cmd, shell=True, stdout=open(LOG_DIR + "/" + device_info[0] + '.log', 'a'),
                         stderr=subprocess.STDOUT)

    def get_base_driver(self):
        desired_caps = {
            'platformName': self.data['platformName'],
            'platformVerion': self.data['platformVersion'],
            'udid': self.device_info[1],
            "deviceName": self.device_info[1],
            'noReset': self.data['noReset'],
            'appPackage': self.data['appPackage'],
            'appActivity': self.data['appActivity'],
            "unicodeKeyboard": True
        }
        self.log.info('appium port:%s start run %s at %s' % (
            self.device_info[0],
            self.data["ip"] + ":" + self.device_info[0],
            ctime()
        ))
        driver = webdriver.Remote(
            'http://' + self.data['ip'] + ':' + self.device_info[0] + '/wd/hub',
            desired_caps
        )
        return driver


if __name__ == '__main__':
    pass