# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/9 17:21
@Author  : 梅迁
@FileName: tran.py
@SoftWare: PyCharm
"""
# 导入Flask类
from flask import Flask, request as rq
from coor_zhuanhuan import *

# 实例化，可视为固定格式
app = Flask(__name__)


# 接口测试
@app.route('/pointTransform', methods=['POST'])
def hello_world():
    a = rq.json
    b = transform_algorithm(a)
    return b


# 启动web应用，端口为5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)
