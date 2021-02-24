# 对自动化浏览器框架的一个简单封装

代理功能需要使用docker  
docker run -p 8000:8000 cz5424/ipproxypool 

安装chrome浏览器和chromedevice(对应版本)  
将chromedevice.exe置于(默认地址)C:\Program Files\Google\Chrome\Application\chromedriver.exe  

安装python3.7环境  
pip install fake-useragent  
pip install selenium
pip install mitmproxy

## 安装mitmproxy可能出现的问题
https://stackoverflow.com/questions/63383400/error-cannot-uninstall-ruamel-yaml-while-creating-docker-image-for-azure-ml-a  
即是删除 python3.7/site-packages/ruamel*  

个人的docker服务器地址为192.168.88.97