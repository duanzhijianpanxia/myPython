'''
任务要求和v5一样
本案例只是利用Request来实现v5的功能

利用parse模块模拟post请求
分析百度翻译
分析步骤：
1. 打开相应网页并且按下F12
2. 尝试输入单词girl，发现每敲击一个字母后都有请求
3. 请求地址是 http://fanyi.baidu.com/sug
4. 利用network-all-hearders，查看发现，formdata的值是kw:girl
5. 检查返回内容格式，发现返回的是json格式内容==>需要用到json包
'''

from urllib import request, parse
import json

'''
大致流程是：
1. 利用data构造内容，然后urlopen打开
2. 返回一个json格式的结果
3. 结果应该就是girl的释义
'''

baseurl = 'https://fanyi.baidu.com/sug'

# 用来模拟form数据的一定是dict格式
data = {
    'kw':input("Please input what you want to find:")
}

# 需要使用parse模块对data进行编码
data = parse.urlencode(data).encode("utf-8")
print(type(data))

headers = {
    # 因为使用post，至少应该包含content-length字段
    "Content-Length":len(data)
}
# 构造一个Request的实例
req = request.Request(url=baseurl, data=data, headers=headers)

# 因为已经构造了一个Request的请求实例，则所有的请求信息都可以封装在request实例中
rsp = request.urlopen(req)

json_data = rsp.read().decode("utf-8")
print(type(json_data))
print(json_data)

# 把json字符转换成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

# 把json字符转换成字典格式
for item in json_data['data']:
    print(item['k'], " ==> ", item['v'])




