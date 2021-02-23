import json
import random
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from fake_useragent import UserAgent
from selenium import webdriver

def random_user_agent(chrome_options):
    ua = UserAgent()
    USER_AGENT = ua.random
    chrome_options.add_argument("--User-Agent=" + USER_AGENT)

def random_proxy(chrome_options):
    # r = requests.get('http://192.168.88.97:8000/?type=0')
    r = requests.get('http://192.168.88.97:8000/')
    ip_ports = json.loads(r.text)
    ip_port = ip_ports[random.randint(0, len(ip_ports))]
    ip = ip_port[0]
    port = ip_port[1]
    url = 'http://%s:%s' % (ip, port)
    chrome_options.add_argument('--proxy-server=' + url)
    return ip

def process_request():
    chrome_options = webdriver.ChromeOptions()
    random_user_agent(chrome_options)
    ip = random_proxy(chrome_options)
    # 这里实现将启动页面影藏
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
                              chrome_options=chrome_options)
    try:
        driver.get('http://httpbin.org/get')
        print('success %s' % ip)
    except:
        requests.get('http://192.168.88.97:8000/delete?ip=%s' % ip)
        print('delete error proxy:%s' % ip)
    driver.quit()  # 关闭进程

if __name__ == '__main__':
    count = 200
    pool = ThreadPoolExecutor(count)
    for i in range(0, count):
        pool.submit(process_request)
        time.sleep(10)
