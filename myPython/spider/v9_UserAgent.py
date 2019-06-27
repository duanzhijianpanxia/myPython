'''
UserAgent： 用户代理，简称UA， 属于heads的一部分，服务器通过UA来判断访问者身份
常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
'''
from urllib import request, error


if __name__ == '__main__':

    url = "http://www.baidu.com"

    try:
        # UserAgent方法一：利用headers方法添加
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        # req = request.Request(url, headers=headers)

        # 方法二：利用add_header方法
        req = request.Request(url)
        req.add_header('UserAgent',"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")

        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)