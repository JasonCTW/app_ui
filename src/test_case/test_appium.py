'''
Author ：SunJie
'''
import unittest


from src.common import driver_configure
import time


class test_appium(unittest.TestCase):

    def setUp(self):
        self.driver = driver_configure.driver_configure().get_ios_driver()

    def test_01login(self):
        '''测试登录功能'''
        time.sleep(5)

    def test_02loginOut(self):
        '''测试退出功能'''
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()