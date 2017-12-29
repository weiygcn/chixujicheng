import os
import configparser

curPath = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(curPath,'cfg.ini')
conf = configparser.ConfigParser()
conf.read(configPath)

smtpServer = conf.get('email','smtp','smtpServer')
sender = conf.get('email','sender')
psw = conf.get('email','psw')
receiver = conf.get('email','receiver')
port = conf.get('email','port')