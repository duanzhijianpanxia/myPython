# 不啰嗦直接开始
from urllib import request, error


if __name__ == '__main__':

    url = "http://www.sipo.gov.cn/www"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    # HTTPError 是URLError的一个子类
    # 两者的区别：HTTPError是对应的请求返回码错误，如果返回的是400以上的请求码，则引发HTTPError
    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)