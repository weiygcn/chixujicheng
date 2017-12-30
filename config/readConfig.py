import os
import configparser

curPath = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(curPath, 'cfg.ini')
conf = configparser.ConfigParser()
conf.read(configPath, encoding='utf-8')

smtpServer = conf.get('email', 'smtpServer')
sender = conf.get('email', 'sender')
psw = conf.get('email', 'psw')
receiver = conf.get('email', 'receiver')
port = conf.get('email', 'port')
