# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/9 17:21
@Author  : 梅迁
@FileName: tran.py
@SoftWare: PyCharm
"""

from flask import Flask, request as rq
from coor_zhuanhuan import *


app = Flask(__name__)


@app.route('/pointTransform', methods=['POST'])
def hello_world():
    a = rq.json
    b = transform_algorithm(a)
    return b



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5004)
