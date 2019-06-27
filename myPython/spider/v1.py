from urllib import request

'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':

    url = "https://study.163.com/category/480000003131009"
    # 打开相应URL并且把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果取出来
    # 读取出来的内容为bytes 格式
    html = rsp.read()
    print(type(html))

    # 如果把bytes格式转换成字符串，需要解码
    html = html.decode("utf-8")

    print(html)