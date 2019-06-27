'''
利用request下载页面
自动检测页面的编码格式
'''

import urllib
import chardet


if __name__ == '__main__':
    url = 'http://news.baidu.com/internet'

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    # 利用chardet自动检测编码格式
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)
