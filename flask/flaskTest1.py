# 导入Flask类
from flask import Flask, request as rq
import coordinationTransform as a
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

    return rq.json

# 启动web应用，端口为5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)