# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/21 22:20
@Author  : 梅迁
@FileName: func_test3.py
@SoftWare: PyCharm
"""
from flask import Flask, request, send_file
from draw_zk import main
import logging
app = Flask(__name__)


@app.route('/py/pointPillar', methods=['POST'])
def json_request():
    req_data = request.get_json()
    expStratumList = req_data['expStratumList']
    projectName = req_data['projectName']
    projectNum = req_data['projectNum']
    pointNum = req_data['expPoint']['pointNum']
    actualPointAltitude = req_data['expPoint']['actualPointAltitude']
    expDiaDiameter = req_data['expDiaDiameter']
    actualPointX = req_data['expPoint']['actualPointX']
    actualPointY = req_data['expPoint']['actualPointY']
    pointStartDate = req_data['expPoint']['pointStartDate']
    pointEndDate = req_data['expPoint']['pointEndDate']
    expNeNumber = req_data['expNeNumber']
    expNeDepth = req_data['expNeDepth']
    waterDepth = req_data['waterDepth']
    waterDate = req_data['waterDate']
    expRoute = req_data['expRoute']
    expRqdList = req_data['expRqdList']
    expSptDepth = req_data['expSptDepth']
    expSptModifyHits = req_data['expSptModifyHits']
    export_route = req_data['expRoute']
    export_route1 = req_data['expRoute1']
    scale = 1000

    logging.info("创建项目属性信息")
    project_attribute = {'projectName': projectName,
                         'projectNum': projectNum,
                         'pointNum': pointNum,
                         'actualPointAltitude': actualPointAltitude,
                         'expDiaDiameter': expDiaDiameter,
                         'actualPointX': actualPointX,
                         'actualPointY': actualPointY,
                         'pointStartDate': pointStartDate,
                         'pointEndDate': pointEndDate,
                         'waterDepth': waterDepth,
                         'waterDate': waterDate}
    logging.info("创建岩芯取样属性")
    try:
        specimen_attribute = {'specimen_num': expNeNumber,
                              'specimen_starts': float(expNeDepth)}
    except Exception as err:
        specimen_attribute = {'specimen_num': expNeNumber,
                              'specimen_starts': None,
                              'specimen_end': None}
        logging.info("岩芯取样属性创建失败")
        print(err.__class__.__name__ + ":", err)
    else:
        logging.info("岩芯取样属性创建成功")
    logging.info("创建钻孔高程数据")
    elevation = [item['actualPointAltitude'] for item in req_data['expStratumList']]
    logging.info("完成钻孔高程数据创建")
    logging.info("创建地质年代成因")

    geo_era_cause = [[item['era'], item['cause']]
                     if ((item['era'] is not None and item['era'] != " ") and
                         (item['cause'] is not None and item['cause'] != " "))
                     else '信息缺失' for item in req_data['expStratumList']]
    logging.info("完成地质年代成因创建")
    logging.info("创建地层岩芯特征描述")
    geo_describe = [item['description'] if item['description'] is not None and " " else "缺少地层相关描述信息" for item
                    in req_data['expStratumList']]
    logging.info("结束地层岩芯特征描述创建")
    logging.info("创建标准贯入属性")
    try:
        inject_attribute = {'inject_hit_number': expSptModifyHits,
                            'top_depth': float(expSptDepth) + 0.3,
                            'bottom_depth': float(expSptDepth)}
    except Exception as err:
        inject_attribute = {'inject_hit_number': expSptModifyHits,
                            'top_depth': None,
                            'bottom_depth': None}
        logging.info("创建标准贯入试验属性失败")
        print(err.__class__.__name__ + ":", err)
    else:
        logging.info("标准贯入试验属性创建成功")
    logging.info("创建岩芯取样属性")
    try:
        rock_attribute = [{'specimen_depth': float(rock_item['actualDepth']),
                           'specimen_rate': float(rock_item['cmr'])}
                          for rock_item in expRqdList]
    except Exception as err:
        rock_attribute = [{'specimen_depth': None,
                           'specimen_rate': None}
                          for _ in expRqdList]
        logging.info("创建岩芯取样属性失败")
        print(err.__class__.__name__ + ":", err)
    else:
        logging.info("岩芯取样属性创建成功")
    main(scale, expStratumList, elevation, geo_era_cause, project_attribute, geo_describe,
         specimen_attribute, inject_attribute, rock_attribute, export_route, export_route1)
    return send_file(expRoute)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
