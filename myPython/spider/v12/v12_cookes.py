from urllib import  request, error
import chardet

if __name__ == '__main__':

    url = 'http://www.renren.com/971280070/newsfeed/photo'

    try:
        headers = {"Cookie": "anonymid=jxa267a0-c2vc6g; depovince=GW; _r01_=1; ick_login=babc69b3-fcf3-40b1-8674-c3391ad9de39; t=6e5bb9278060635882c075cdb88af8230; societyguester=6e5bb9278060635882c075cdb88af8230; id=971280070; xnsid=7793c3b5; jebecookies=100e647b-6873-4d35-9755-1435ab2b126b|||||; JSESSIONID=abc19eKEgkNbVc-UdBiUw; ver=7.0; loginfrom=null; jebe_key=e592f0e8-b684-4ab0-9891-7f3e57e23c60%7Cce2fd52ddd2b60ba914770b7fc7c7741%7C1561361925065%7C1%7C1561361925083; wp_fold=0"}
        req = request.Request(url, headers=headers)
        rsp = request.urlopen(req)

        html = rsp.read()
        cs = chardet.detect(html)

        html = html.decode(cs.get("encoding", "utf-8"))
        # print(html)

        # 之所以注释上面的打印函数 是因为在初次调试阶段遇到写出来的HTML页面乱码，尝试打印结果正常，去网上找了解决问题方法
        # 是因为入是，没有指明编码格式 添加了encoding="utf-8" 问题成功解决
        # 得到经验 有问题还得问度娘
        with open("rsp.html", "w", encoding="utf-8") as f:
            f.write(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)