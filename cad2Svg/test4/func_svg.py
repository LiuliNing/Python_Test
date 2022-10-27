# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/6 14:56
@Author  : 梅迁
@FileName: func_svg.py
@SoftWare: PyCharm
"""
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons import odafc
from ezdxf.addons.drawing.config import Configuration
from flask import request
import os
import logging

logging.basicConfig(filename='logger.log',
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
                    level=logging.INFO,
                    filemode='a',
                    datefmt='%Y-%m-%d %H:%M:%S')


# 功能：将DWG文件保存为DXF格式（以文件路径的方式读取文件）
def dwg_dxf(import_path, export_path):
    """
    实现将DWF格式的文件保存为DXF格式文件
    :param import_path:dwg文件导入路径
    :param export_path:dxf文件导出的路径
    :return:经过格式转换后的文件
    """
    logging.info('将dwg文件另存为dxf')
    try:
        dd = odafc.readfile(rf"{import_path}")
    except Exception as err:
        logging.error("dwg文件读取失败")
        print(err.__class__.__name__ + ":", err)
    else:
        logging.error("dwg文件读取成功")
        dd.saveas(rf"{export_path}")
        return dd


# DWG转DXF（文件流的方式读取文件）
def dwg_dxf_stream(params_file):
    """
    实现以数据流的方式读入DWG格式数据，并将其转化为.DXF格式数据
    :param params_file:DWG文件名
    :return:转为DXF格式之后的文件
    """
    dd = odafc.readfile(params_file)
    dd.save()
    return dd


# 将.dxf文件保存为.svg文件
def svg_transform(doc, export_file_path):
    """
    实现将.dxf文件保存为.svg文件功能
    :param doc: dxf文件
    :param export_file_path: .svg文件导出路径
    :return: 转换后的.svg格式文件
    """
    logging.info('进行svg格式转换')
    doc.styles.new('svgText', dxfattribs={'font': 'SimHei.ttf'})
    msp = doc.modelspace()
    for e in msp:
        if e.dxftype() == 'MTEXT' and len(list(e.text)) > 25:
            font_num = int((e.dxfattribs()['width']) / e.dxfattribs()['char_height'] * 0.8)
            new_text = list(e.text)
            for i in range(0, len(new_text), font_num):
                new_text.insert((i + font_num), '\n')
            e.text = ''.join(new_text)
    my_config = Configuration.defaults()
    my_config = my_config.with_changes(lineweight_scaling=0.0, min_lineweight=0.1)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
    fig.savefig(export_file_path, config=my_config)
    logging.info('完成svg文件转换')


# DWG文件转SVG文件
def main(handle_type, file_iport, file_eport):
    """
    实现DWG转SVG文件功能
    :param handle_type: 操作类型（0：文件， 1：文件流）
    :param file_iport:DWG文件导入路径
    :param file_eport:SVG文件导出路径
    :return:转换后的SVG文件
    """
    if int(handle_type) == 0:
        dxf_doc = dwg_dxf(file_iport, file_eport)
        svg_transform(dxf_doc, f"{file_eport}.svg")
    elif int(handle_type) == 1:
        param_file = request.files['file']
        dxf_doc = dwg_dxf_stream(param_file.stream)
        folder = file_eport
        if not os.path.exists(folder):
            os.makedirs(folder)
            file_name_res = f"{folder}//svg_res.svg"
            svg_transform(dxf_doc, file_name_res)
        else:
            file_name_res = f"{folder}//svg_res.svg"
            svg_transform(dxf_doc, file_name_res)
    else:
        return f'handle_type is error, must be 0 or 1'