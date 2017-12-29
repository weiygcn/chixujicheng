import requests
import unittest
from common.logger import Log
from case.LoginBlogs import Blogs
import time

class Test(unittest.TestCase):
    log = Log()
    def setUp(self):
        session = requests.session()
        self.blos = Blogs(session)


    def testAddDailyLog(self):
        u'''测试登录用例'''
        self.log.info('--------start----------')
        result = self.blos

        self.Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        self.AddDailyLogURL = 'https://i.cnblogs.com/EditDiary.aspx?opt=1'
        self.AddData = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '4773056F',
            'Editor$Edit$txbTitle': '测试334标题',
            'Editor$Edit$EditorBody': '<p>测试334内容</p>',
            'Editor$Edit$lkbPost': '保存'}
        self.AddReq = self.session.post(
            self.AddDailyLogURL,
            data=self.AddData,
            headers=self.Headers,
            verify=True,
            allow_redirects=True)
        print('########### test02')

    def testTest(self):
        ygwT = time.strftime('%Y_%m_%d_%H_%M_%S')
        print(ygwT)
        print('执行testTest用例')
        self.assertEqual(1, 2, '对比一致')

if __name__ == '__main__':
    unittest.main()