# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/16 9:27
@Author  : 梅迁
@FileName: file_call.py
@SoftWare: PyCharm
"""
from flask import Flask, send_file
from loguru import logger as log
from func_svg import *

app = Flask(__name__)


@app.route('/py/cad2Svg', methods=['POST'])
def receive_file():
    log.add("file.log", format="{time} {level} {message}", filter="", level="INFO")
    # 参数类型 0 相对路径url（用于同服务器部署时使用） 1 文件流（用于跨服务器部署时使用）
    type_attr = request.form.get('type')
    log.info("type {}", type_attr)
    # 文件相对路径url
    file_in_attr = request.form.get('file_in_url')
    log.info("file_in_attr {}", file_in_attr)
    # 文件临时输出路径
    file_out_attr = request.form.get('file_out_url')
    log.info("file_out_attr {}", file_out_attr)
    # 转换文件
    log.info("转换文件 start ")
    tran_file(type_attr, file_in_attr, file_out_attr)
    log.info("转换文件 end ")
    # 清空临时目录文件
    log.info("清理临时目录 start ")
    os.remove(file_out_attr)
    log.info("清理临时目录 end ")
    log.info("输出文件 start ")
    return send_file(fr"{file_out_attr}.svg", mimetype='.svg')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
