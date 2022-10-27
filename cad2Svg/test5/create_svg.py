# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/18 15:58
@Author  : 梅迁
@FileName: create_svg.py
@SoftWare: PyCharm
"""
from ezdxf.addons.drawing.config import Configuration
from ezdxf.addons.drawing import matplotlib


def svg_transform(doc, export_file_path):
    """
    实现将.dxf文件保存为.svg文件功能
    :param doc: modelspace
    :param export_file_path: .svg文件导出路径
    :return: 转换后的.svg格式文件
    """
    msp = doc.modelspace()
    for e in msp:
        if e.dxftype() == 'MTEXT' and len(list(e.text)) > 20:
            font_num = int((e.dxfattribs()['width']) / e.dxfattribs()['char_height'] * 0.8)
            new_text = list(e.text)
            for i in range(0, len(new_text), font_num):
                new_text.insert((i + font_num), '\n')
            e.text = ''.join(new_text)
    doc.styles.new('DescribeText', dxfattribs={'font': 'SimHei.ttf'})
    my_config = Configuration.defaults()
    my_config = my_config.with_changes(lineweight_scaling=0.0, min_lineweight=0.1)
    matplotlib.qsave(doc.modelspace(), rf"{export_file_path}", config=my_config)
