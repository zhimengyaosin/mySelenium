import json
import random
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
from selenium import webdriver

def random_user_agent(chrome_options):
    ua = UserAgent()
    USER_AGENT = ua.chrome
    chrome_options.add_argument("--User-Agent=" + USER_AGENT)

def random_proxy(option):
    # r = requests.get('http://192.168.88.97:8000/?type=0')
    r = requests.get('http://192.168.88.97:8000/')
    ip_ports = json.loads(r.text)
    ip_port = ip_ports[random.randint(0, len(ip_ports))]
    ip = ip_port[0]
    port = ip_port[1]
    url = 'http://%s:%s' % (ip, port)
    option.add_argument('--proxy-server=' + url)
    return ip


def process_request():
    option = webdriver.ChromeOptions()
    random_user_agent(option)
    ip = random_proxy(option)
    # 这里实现将启动页面影藏
    option.add_argument('--headless')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
                              options=option)
    try:
        driver.get('https://httpbin.org/get')
        time.sleep(10)
        print(driver.page_source)
    except:
        requests.get('http://192.168.88.97:8000/delete?ip=%s')
        print('delete error proxy:%s' % ip)
    driver.quit()  # 关闭进程

if __name__ == '__main__':
    count = 50
    pool = ThreadPoolExecutor(count)
    for i in range(0, count):
        pool.submit(process_request)
        time.sleep(1)
