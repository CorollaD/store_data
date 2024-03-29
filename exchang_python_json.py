#！ /usr/bin/python3

import json

# Python 字典类型转换为JSON对象
data = {
    'no': 1,
    'name':'Runood',
    'url':'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

# 将 JSON对象转换为Python 字典
data2 = json.loads(json_str)
print("data2['name']:", data2['name'])
print("data2['url]: ", data2['url'])
