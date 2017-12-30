import requests
import unittest
from common.logger import Log
from case.LoginBlogs import Blogs
from bs4 import BeautifulSoup
import time


class Test(unittest.TestCase):
    log = Log()

    def setUp(self):
        session = requests.session()
        self.blos = Blogs(session)

    def testAddDailyLog(self):
        u'''添加日记'''
        self.log.info('--------start----------')
        self.AddData = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '4773056F',
            'Editor$Edit$txbTitle': '测试1标题',
            'Editor$Edit$EditorBody': '<p>测试334内容</p>',
            'Editor$Edit$lkbPost': '保存'}
        respText = self.blos.addDailyLog(self.AddData)
        soupObj = BeautifulSoup(respText,'html.parser')
        result = soupObj.find_all(class_='MessagePanel')[0].text.strip()
        self.log.info(u'调用增加日志函数的响应结果：%s'%result)
        self.assertEqual(result,u'保存成功')
        self.log.info('-----------end------------')



if __name__ == '__main__':
    unittest.main()
