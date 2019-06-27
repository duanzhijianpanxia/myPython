'''
使用代理访问百度
'''

from urllib import request,error

if __name__ == '__main__':

    url = 'http://www.baidu.com'

    # 代理常用网址：
    # www.xicidaili.com
    # www.goubanjia.com
    # 基本使用步骤：
    # 1.设置代理地址
    Proxy = {'http': '124.250.26.129:8080'}
    # 2.创建ProxyHandler
    Proxy_handler = request.ProxyHandler(Proxy)
    # 3.创建Opener
    openner = request.build_opener(Proxy_handler)
    # 4.安装Opener
    request.install_opener(openner)

    # 现在如果访问url，则使用代理服务器
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)