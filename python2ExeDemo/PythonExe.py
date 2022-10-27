# 导入Flask类
import json
from flask import Flask, request as rq

# 实例化，可视为固定格式
app = Flask(__name__)


# 接口测试
@app.route('/test', methods=['GET'])
def hello_world():
    return rq.values


def test(json_data1, json_data2):
    print(json_data1)
    print(json_data2)
    return json_data1


# 启动web应用，端口为5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
