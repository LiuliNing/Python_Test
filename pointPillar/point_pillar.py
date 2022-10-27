# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/18 11:32
@Author  : 梅迁
@FileName: point_pillar.py
@SoftWare: PyCharm
"""
from flask import Flask, request, send_file
from draw_zk import *
from loguru import logger as log

app = Flask(__name__)


@app.route('/py/pointPillar', methods=['POST'])
def graphic_zk():
    log.add("file.log", format="{time} {level} {message}", filter="", level="DEBUG")
    py_zk_datas = request.json
    log.info("pointPillar json数据 {}", request.json)
    scale = 1000
    project_arr = {'project_name': py_zk_datas['projectName'],
                   'project_num': py_zk_datas['projectNum'],
                   'zk_zkbh': py_zk_datas['expPoint']['pointNum'],
                   'zk_kkgc': float(py_zk_datas['expPoint']['actualPointAltitude']),
                   'zk_kkzj': float(py_zk_datas['expDiaDiameter']),
                   'zk_zbx': float(py_zk_datas['expPoint']['actualPointX']),
                   'zk_zby': float(py_zk_datas['expPoint']['actualPointY']),
                   'zk_kgrq': py_zk_datas['expPoint']['pointStartDate'],
                   'zk_jgrq': py_zk_datas['expPoint']['pointEndDate'],
                   'zk_wdswsd': float(py_zk_datas['waterDepth']),
                   'zk_clswrq': py_zk_datas['waterDate']}
    if py_zk_datas['expNeDepth'] == None or " ":
        qy_attr = {'qy_num': py_zk_datas['expNeNumber'], 'qy_start': 1, 'qy_end': float(py_zk_datas['expRqdList'][0]['depth'])}
    else:
        qy_attr = {'qy_num': py_zk_datas['expNeNumber'], 'qy_start': float(py_zk_datas['expNeDepth']), 'qy_end': float(py_zk_datas['expRqdList'][0]['depth'])}
    gc_datas = [float(i['actualPointAltitude']) for i in py_zk_datas['expStratumList']]
    geo_ndcy = [py_zk_datas['expStratumList'][j]['era'] + py_zk_datas['expStratumList'][j]['cause'] if py_zk_datas['expStratumList'][j]['era'] != None and py_zk_datas['expStratumList'][j]['cause'] != None else 'Q4ml' for j in range(len(py_zk_datas['expStratumList']))]
    geo_describ = [k['description'] for k in py_zk_datas['expStratumList']]
    bg_attr = 1

    ys_attr = [{'sd': float(l['actualDepth']), 'qyl': float(l['cmr'])} for l in py_zk_datas['expRqdList']]
    data_svg_algorithm(scale, gc_datas, geo_ndcy, project_arr, geo_describ, qy_attr, bg_attr, ys_attr)
    return send_file("E://cad2svg//1.svg")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
