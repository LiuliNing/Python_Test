# 导入Flask类

from ctypes import cdll

from flask import Flask, request as rq

import flaskTest3

# 实例化，可视为固定格式
app = Flask(__name__)

if __name__ == '__main__':
    print("11")


# 接口测试
@app.route('/test/get', methods=['GET'])
def hello_world():
    print("form:", rq.form)
    print("data:", rq.data)
    print("values:", rq.values)
    print("args:", rq.args)
    print("json:", rq.json)
    cur = cdll.LoadLibrary('flaskTest3.so')
    res = flaskTest3.test(rq.json, rq.json)
    return res


# 启动web应用，端口为5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
