# 导入Flask类
import json
from flask import Flask, request as rq
import flaskTest3
from ctypes import cdll
# 实例化，可视为固定格式
app = Flask(__name__)


# 接口测试
@app.route('/test', methods=['GET'])
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
