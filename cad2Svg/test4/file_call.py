# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/16 9:27
@Author  : 梅迁
@FileName: file_call.py
@SoftWare: PyCharm
"""
from func_svg import *
from flask import Flask, request, send_file


app = Flask(__name__)


@app.route('/py/cad2Svg', methods=['POST'])
def receive_file():
    type_attr = request.form.get('type')
    file_in_attr = request.form.get('file_in_url')
    file_out_attr = request.form.get('file_out_url')
    main(type_attr, file_in_attr, file_out_attr)
    os.remove(file_out_attr)
    return send_file(fr"{file_out_attr}.svg")


if __name__ == '__main__':
    app.run(host="10.10.6.100", port=5000)
