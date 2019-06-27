'''
爬取百度贴吧--西安科技大学吧
1. 西安科技大学吧主页是 http://tieba.baidu.com/f?&kw=西安科技大学
2. 进去之后，贴吧有很多页
    第一页网址：http://tieba.baidu.com/f?kw=西安科技大学&ie=utf-8&pn=0
    第二页网址：http://tieba.baidu.com/f?kw=西安科技大学&ie=utf-8&pn=50
    第三页网址：http://tieba.baidu.com/f?kw=西安科技大学&ie=utf-8&pn=100
    第四页网址：http://tieba.baidu.com/f?kw=西安科技大学&ie=utf-8&pn=150
    第五页网址：http://tieba.baidu.com/f?kw=西安科技大学&ie=utf-8&pn=200

3. 发现贴吧的页数和后面的pn存在这样的关系：pn=(页数-1)*50 , 根据这个关系猜测每一页显示的内容是五十条

解决办法：
1.准备构建参数字典
    字典包含三部分，kw, ie, pn
2.使用parse构建完整url
3.使用for循环下载
'''
from urllib import request, parse, error


if __name__ == '__main__':

    #1.准备构建参数字典
    qs = {
        "kw": "西安科技大学",
        "ie": "utf-8",
        "pn": 0
    }

    #2.使用parse构建完整的url
    # 假定只需要前十页
    urls = []
    baseurl = "http://tieba.baidu.com/f?"

    for i in range(10):
        # 构建新的qs
        pn = i * 50
        qs['pn'] = str(pn)
        # 把qs编码完成后的url和baseurl进行拼接
        # 拼接完成后转入ruls列表中
        urls.append(baseurl + parse.urlencode(qs))

    print(urls)

    #3. 使用for循环下载（HTML）
    try:
        for url in urls:
            rsp = request.urlopen(url)
            html = rsp.read().decode("utf-8")
            print(url)
            print(html)

            with open(k, "w", encoding="utf-8") as f:
                f.write(url)
                f.write(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)
