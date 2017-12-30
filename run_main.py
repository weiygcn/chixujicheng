import os
import unittest
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import HTMLTestRunner

currentPath = os.getcwd()


def add_case(caseName='case', rule='test*.py'):
    '''第一步，加载所有的测试用例'''
    casePath = os.path.join(currentPath, caseName)  # 用例文件夹
    '''如果不存在case文件夹，就自动创建一个'''
    if not os.path.exists(casePath):
        os.mkdir(casePath)
    print('Test Case Path:%s' % casePath)
    '''定义discover方法的参数'''
    discover = unittest.defaultTestLoader.discover(
        casePath, pattern=rule, top_level_dir=None)
    print(discover)
    return discover


def runCase(allCase, reportName='report'):
    '''第二步，执行所有的测试用例，并把结果写入HTML测试报告中'''
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportPath = os.path.join(currentPath, reportName)  # c测试报告文件夹
    if not os.path.exists(reportPath):
        os.mkdir(reportPath)
    reportAbsPath = os.path.join(reportPath, now + 'result.html')
    print('report path %s' % reportPath)
    fp = open(reportAbsPath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title=u'自动化测试报告，测试结果如下：', description=u'用例执行情况：')

    '''调用addCase函数返回值'''
    runner.run(allCase)
    fp.close()


def getReportFile(reportPath):
    '''第三步,获取最新的测试报告'''
    lists = os.listdir(reportPath)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(reportPath, fn)))
    print(u'最新测试生成的报告：' + lists[-1])
    # 找到最新生成的报告文件
    reportFile = os.path.join(reportPath, lists[-1])
    return reportFile


def sendMail(sender, psw, receiver, smtpserver, reportFile, port):
    '''第四步，发送最新的测试报告内容'''
    with open(reportFile, 'rb') as f:
        mailBody = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mailBody, _subtype='html', _charset='utf-8')
    msg['Subject'] = u'自动化测试报告'
    msg['from'] = sender
    msg['to'] = 'psw'
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(reportFile, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except BaseException:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')


if __name__ == '__main__':
    allCase = add_case()  # 1,加载用例
    # 生成测试报告的路径
    runCase(allCase)  # 2，执行用例
    # 获取最新测试报告文件
    reportPath = os.path.join(currentPath, 'report')  # 测试报告文件夹
    reportFile = getReportFile(reportPath)  # 3，获取最新的测试报告
    # 配置邮箱
    from config import readConfig

    sender = readConfig.sender
    psw = readConfig.psw
    smtpServer = readConfig.smtpServer
    port = readConfig.port
    receiver = readConfig.receiver
    sendMail(sender, psw, receiver, smtpServer, reportFile, port)  # 4，最后一步发送报告
