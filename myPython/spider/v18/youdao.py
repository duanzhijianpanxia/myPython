'''
破解有道词典
v1
'''

from urllib import request, parse

def youdao(key):

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    '''
    多行快速加引号步骤
    1. ctrl + r:调出正则匹配工具栏
    2. 选中想要匹配部分
    3. 两栏依次填写匹配公式：
    
    4. 勾选三个选项
    5. 替换
    
    
    选取多行开头alt + button1
    '''

    data = {
        'i':' key',
        'from':' AUTO',
        'to':' AUTO',
        'smartresult':' dict',
        'client':' fanyideskweb',
        'salt':' 15615613028207',
        'sign':' 8127ef1b41b5fd99f4edd9f91baa7d0c',
        'ts':' 1561561302820',
        'bv':' d6c3cd962e29b66abe48fcb8f4dd7f7d',
        'doctype':' json',
        'version':' 2.1',
        'keyfrom':' fanyi.web',
        'action':' FY_BY_REALTlME',
    }

    # 参数data需要时bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        # "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "236",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF - 8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1933459386@10108.160.18;OUTFOX_SEARCH_USER_ID_NCOO=1652204480.2389536;JSESSIONID=aaad7w3BQpyeYb0J8qxUw;___rl__test__cookies=1561610962238",
        "Host": "fanyi.youdao.com",
        "Origin": "http: // fanyi.youdao.com",
        "Referer": "http: // fanyi.youdao.com /",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/73.0.3683.86Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode("utf-8")
    print(html)
    with open('rsp.html', 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    youdao("girl")