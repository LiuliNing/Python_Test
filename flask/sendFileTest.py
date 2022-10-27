# 导入Flask类
import os

from flask import Flask, request as rq,send_file
import coordinationTransform as a
# 实例化，可视为固定格式
app = Flask(__name__)


# 接口测试
@app.route('/sendfile', methods=['GET'])
def sendfile():
    # os.open("E://cad2svg//1.svg")
    print(1)
    return send_file("E://cad2svg//1.svg")

# 启动web应用，端口为5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)