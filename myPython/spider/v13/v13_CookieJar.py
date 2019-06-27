from urllib import request, parse, error
from http import cookiejar


# 创建cookiejar实例
cookie = cookiejar.CookieJar()
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler,cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户密码，用来获取登录cookie凭证
    :return:
    '''
    # 此url需要从登录form的action属性中提取
    url = 'http://www.renren.com/PLogin.do'

    # 此键值需要从form的两个对应input中提取name属性
    data = {
        "email" : "15619509989",
        "password" : "123456"
    }

    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建请求对象
    req = request.Request(url, data=data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/971283120/profile"

    try:
        # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
        rsp = opener.open(url)

        html = rsp.read().decode()

        # 写入文件的HTML页面乱码，去网上找了解决问题方法
        # 是因为入是，没有指明编码格式 添加了encoding="utf-8" 问题成功解决
        # 得到经验 有问题还得问度娘
        with open("rsp.html", "w", encoding='utf-8') as f:
            f.write(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)

if __name__ == '__main__':
    login()
    getHomePage()