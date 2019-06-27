'''
构建代理集群/队列
每次访问服务器，随机抽取一个代理
随机抽取可以使用random.choice

分析步骤
1. 构建代理群
2. 每次访问，随机选取代理并执行
'''
from urllib import request, error
import random

# 使用代理步骤
# 1. 设置代理地址
proxy_list = [
    {"http": "223.241.119.51"},
    {"http": "218.64.69.79"},
    {"http": "112.85.170.101"},
    {"http": "112.247.171.152:8060"},
    {"http": "111.40.84.73:9797"}
]
# 2. 创建proxyhandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)
# 3. 创建opener
opener_list = []
opener = request.build_opener(proxy_handler)
opener_list.append(opener)

url = "http://www.baidu.com"
# 现在如果访问url，则使用代理服务器
try:
    # 4. 安装opener
    opener = random.choice(opener_list)
    request.install_opener(opener)

    req = request.Request(url)
    rsp = request.urlopen(req)
    html = rsp.read().decode("utf-8")
    print(html)

except error.URLError as e:
    print("URLError: ".format(e.reason))
    print("UULError: ".format(e))

except Exception as e:
    print(e)