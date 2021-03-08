import json
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from fake_useragent import UserAgent
from selenium import webdriver

target = []
target.append(
    'https://learnywhere.cn/bb/activity/article/2020/0619/news?feat=u48881869&key=84b1c1b7b59d42358273118af6d1ea6a&share_platform=wechat&from=singlemessage')

def random_user_agent(chrome_options):
    ua = UserAgent()
    USER_AGENT = ua.chrome
    chrome_options.add_argument("--User-Agent=" + USER_AGENT)


def process_request(ip, port, delete_url):
    options = webdriver.ChromeOptions()
    random_user_agent(options)
    options.add_argument("--proxy-server=%s:%s" % (ip, port))
    # 开发者模式
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 新版本chrome反爬
    options.add_argument("--disable-blink-features=AutomationControlled")

    # 这里实现将启动页面影藏
    options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\sin7590\AppData\Local\Google\Chrome\Application\chromedriver.exe',
        options=options)
    try:
        for i in target:
            driver.get(i)
        print("success:%s" % ip)
    except:
        print("driver.get(target) error:%s" % ip)
    requests.get(delete_url)
    time.sleep(5)
    driver.quit()  # 关闭进程

if __name__ == '__main__':
    pool = ThreadPoolExecutor(1000)
    r = requests.get('http://192.168.88.97:8000/')
    ip_ports = json.loads(r.text)
    for i in range(0, len(ip_ports)):
        ip = ip_ports[i][0]
        port = ip_ports[i][1]
        pool.submit(process_request, ip, port,'http://192.168.88.97:8000/delete?ip='+ip)
        time.sleep(1)

    r = requests.get('http://192.168.88.97:5010/get_all/')
    ip_ports = json.loads(r.text)
    for i in range(0, len(ip_ports)):
        ip = ip_ports[i]['proxy'].split(':')[0]
        port = ip_ports[i]['proxy'].split(':')[1]
        pool.submit(process_request, ip, port, 'http://192.168.88.97:5010/delete/?proxy=' + ip + ':' + port)
        time.sleep(1)
