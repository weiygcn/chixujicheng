import requests
import time
try:
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    url = 'http://i.51job.com/resume/ajax/refresh_resume.php?0.5460826682813431&jsoncallback=jQuery183049724354932948645_1514880368768&ReSumeID=321042072&lang=c&_=1514880875325'
    url2 = 'https://i.zhaopin.com/ResumeCenter/MyCenter/RefreshResume?resumeId=221970864&resumenum=JM302291601R90250002000&version=1&language=1&t=1514881737833'
    url3 = 'https://c.liepin.com/resume/refreshresume.json'
    countNum = 1
    while True:
        resp1 = requests.get(url, headers=Headers, verify=True)
        getTime1 = time.ctime()
        print('刷新第【{}】次-51简历-时间【{}】-响应code：【{}】'.format(countNum,
                                                        getTime1, resp1.status_code))
        time.sleep(60)
        resp2 = requests.get(url2, headers=Headers, verify=True)
        getTime2 = time.ctime()
        print('刷新第【{}】次-智联简历-时间【{}】-响应code：【{}】'.format(countNum,
                                                        getTime2, resp2.status_code))
        countNum += 1
except Exception as e:
    raise e
