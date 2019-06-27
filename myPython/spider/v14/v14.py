'''
打印cookie
不需要进入主页函数了
'''


from urllib import request, parse
from http import cookiejar

# 1. 创建cookie实例
cookie = cookiejar.CookieJar()
# 2. 创建cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 3. 创建http请求管理器
http_handler = request.HTTPHandler()
# 4. 创建https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(https_handler, http_handler,cookie_handler)

# 定义登录函数
def login():
    '''
    负责初次登录
    需要输入用户名和密码，用来获取登录cookie登录凭证
    :return:
    '''

    # 此处url需要从登录form表单的action属性中获取
    url = "http://www.renren.com/PLogin.do"

    # 此处键值需要从登录form的两个对应input中提取name属性
    data = {
        "email" : "15619509989",
        "password" : "123456"
    }
    # 把数进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    login()

    '''
    执行完login函数，会得到授权之后的cookie
    我们尝试把cookie打印出来
    '''
    print(cookie)
    for i in cookie:
        print(type(i))
        print(i)
        for j in dir(i):
            print(j)