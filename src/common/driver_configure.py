"""
Author ：SunJie
"""
# coding:utf-8

from appium import webdriver
import os


class driver_configure():



    def get_driver(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 平台
        self.desired_caps['platformVersion'] = '5.0.2'  # 系统版本
        #self.desired_caps['app'] = 'src/common/KuaiQianBao.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
        self.desired_caps['appPackage'] = 'com.bill99.kuaiqian'     # APK包名
        self.desired_caps['appActivity'] = 'com.bill99.kuaiqian.appmodule.welcome.WelcomeActivity'     # 被测程序启动时的Activity
        self.desired_caps['unicodeKeyboard'] = 'true'   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
        self.desired_caps['resetKeyboard'] = 'true'  # 是否在测试结束后将键盘重轩为系统默认的输入法。
        self.desired_caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
        self.desired_caps['deviceName'] = 'K4PDU15911010493'     # 手机ID
        self.desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
        self.driver = webdriver.Remote("http://10.11.66.127:4723/wd/hub", self.desired_caps)
        return self.driver

    def get_ios_driver(self):
        app = os.path.join(os.path.dirname(__file__),
                           '',
                           'app-KuaiQianBao-V5.0.9.2-Debug.ipa')
        app = os.path.abspath(app)
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'iOS'  # 平台
        self.desired_caps['platformVersion'] = '11.4'  # 系统版本
        self.desired_caps['app'] = app   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
        self.desired_caps['automationName'] = "XCUITest"
        #self.desired_caps['unicodeKeyboard'] = 'true'   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
        #self.desired_caps['resetKeyboard'] = 'true'  # 是否在测试结束后将键盘重轩为系统默认的输入法。
        #self.desired_caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
        self.desired_caps['deviceName'] = '哥哥phone'     # 手机ID
        self.desired_caps['udid'] = '164b2d5afe1eb3852f0a1a61ddbcd7cdf63134d8'
        self.desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
        self.driver = webdriver.Remote("http://10.11.66.127:4723/wd/hub", self.desired_caps)
        return self.driver



