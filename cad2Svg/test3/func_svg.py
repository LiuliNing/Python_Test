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
from flask import request
import os


# 功能：将DWG文件保存为DXF格式（以文件路径的方式读取文件）
def dwg_dxf(import_path, export_path):
    """
    实现将DWF格式的文件保存为DXF格式文件
    :param import_path:读取到的CAD文件
    :param export_path:DXF文件导出的路径
    :return:经过格式转换后的文件
    """
    dd = odafc.readfile(rf"{import_path}")
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
def svg_transform(dxf_doc, export_file_path):
    """
    实现将.dxf文件保存为.svg文件功能
    :param dxf_doc: dxf文件
    :param export_file_path: .svg文件导出路径
    :return: 转换后的.svg格式文件
    """
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(dxf_doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(dxf_doc.modelspace(), finalize=True)
    fig.savefig(export_file_path)


# DWG文件转SVG文件
def tran_file(type_attr, file_in_attr, file_out_attr):
    """
    实现DWG转SVG文件功能
    :param type_attr:处理DWG文件方式
    :param file_in_attr:DWG文件导入路径
    :param file_out_attr:SVG文件导出路径
    :return:转换后的SVG文件
    """
    if int(type_attr) == 0:
        dxf_doc = dwg_dxf(file_in_attr, file_out_attr)
        svg_transform(dxf_doc, f"{file_out_attr}.svg")
    else:
        param_file = request.files['file']
        dxf_doc = dwg_dxf_stream(param_file.stream)
        file_name_res = f"{file_out_attr}//svg_res.svg"
        if not os.path.exists(file_out_attr):
            os.makedirs(file_out_attr)
        svg_transform(dxf_doc, file_name_res)
