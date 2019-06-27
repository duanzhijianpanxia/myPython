import urllib


if __name__ == '__main__':
    url = 'https://study.163.com/'

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    # 获取请求的URL信息
    print("URL: {0}".format(rsp.geturl()))
   # 获取http的头信息
    print("Info: {0}".format(rsp.info()))
    # 获取code信息，200代表成功
    print("Code: {0}".format(rsp.getcode()))

    html = rsp.read()

    # 使用get获取值保证不会出错
    html = html.decode()
    print(html)