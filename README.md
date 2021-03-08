# 对自动化浏览器框架的一个简单封装

## 环境
python3.7
本项目附带的chrome70浏览器以及去除爬虫特征的chromeDrive  
使用了两个docker代理池  

## 安装chrome浏览器和chromedevice(对应版本) 
将chromedriver.exe置于(默认地址)C:\Users\sin7590\AppData\Local\Google\Chrome\Application\chromedriver.exe  

## docker
代理功能需要使用docker  
docker run -p 8000:8000 cz5424/ipproxypool 
docker run -p 6379:6379 redis  
###window下容器proxy_pool访问redis
docker run --env DB_CONN=redis://:@host.docker.internal:6379 -p 5010:5010 jhao104/proxy_pool:latest

## python
pip install fake-useragent  
pip install selenium

## 判断chromeDrive抹除特征是否生效
在打开的浏览器的console中执行window.navigator.webdriver  

## 资料
https://my.oschina.net/u/4589342/blog/4942512
https://zhuanlan.zhihu.com/p/78368287
https://www.jianshu.com/p/dfd1e2753d71
https://blog.zengrong.net/post/use-mitmproxy-2/
https://blog.wolfogre.com/posts/usage-of-mitmproxy