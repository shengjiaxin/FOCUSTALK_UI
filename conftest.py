# coding=utf-8
# Author：方柯

import warnings
import pytest


# 配置app连接信息
# 红米
@pytest.fixture(scope='session')
def android_setting():
    warnings.filterwarnings("ignore")
    desired_caps = {"platformName": "Android",
                    "deviceName": "448c1e270510",
                    "platformVersion": "11",
                    'appPackage': 'com.focus.focustalk',
                    'appActivity': 'com.focus.focustalk.MainActivity',
                    "noReset": True,
                    "unicodeKeyboard": True,
                    "resetKeyboard": True,
                    "waitForIdleTimeout": 100
                    }
    return desired_caps

