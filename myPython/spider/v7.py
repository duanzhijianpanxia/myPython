'''
URLError的使用
'''

from urllib import request, error


if __name__ == '__main__':
    url = 'https://www.baiiiiiidu.com/'

    try:

        req = request.Request(url)
        rsp = request.urlopen( req )
        html = rsp.read().decode()
        print(html)
    # URLError 主要是针对，服务器连接失败、没网、不知道指定服务器、是OSError的子类
    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)