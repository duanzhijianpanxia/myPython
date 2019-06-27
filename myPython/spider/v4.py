from urllib import request, parse
import chardet


'''
掌握对url进行参数编码的方法
要是用parse模块
'''

if __name__ == '__main__':
    url = 'https://www.baidu.com//s?'
    wd = input("Input your keyword:")


    # 要想使用data，需要使用字典结构
    qs = {
        "wd":wd
    }

    # 转换URL编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)


    # 如果直接用可读参数的URL，是不能访问的
    # fullURL = ‘http://www.baidu.com/s?wd=大熊猫'

    rsp = request.urlopen(fullurl)
    html = rsp.read()

    # 利用chardet自动检测编码格式
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))

    # html = html.decode("ascii")

    print(html)