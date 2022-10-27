# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/13 9:39
@Author  : 梅迁
@FileName: draw_zk.py
@SoftWare: PyCharm
"""
import ezdxf
from create_svg import *
import logging
import math


hole_doc = ezdxf.new('R2000', setup=True)
hole_msp = hole_doc.modelspace()
logging.basicConfig(filename='logger.log',
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
                    level=logging.INFO,
                    filemode='a',
                    datefmt='%Y-%m-%d %H:%M:%S')


hole_doc.styles.new('固定字段文字', dxfattribs={'font': 'SimHei.ttf'})
hole_doc.styles.new('项目信息文字', dxfattribs={'font': 'SimHei.ttf'})


def text_altitude(text_amount, width_mtext, size, h_ratio, v_ratio):
    """
    实现多行文本框宽度及高度计算
    :param text_amount:文本文字的总数目
    :param width_mtext:文本框设置宽度
    :param size:字体高度
    :param h_ratio:水平放大系数
    :param v_ratio:竖向放大系数
    :return:多行文本框的宽度与高度
    """
    logging.info("多行文本框高度及宽度计算")
    font_size = size
    single_height = 1.05 * v_ratio
    single_width = 1 * h_ratio
    h_blank_space = 0.18 * h_ratio
    v_blank_space = 0.75 * v_ratio
    logging.info("计算文字总行数、总高度和总宽度")
    line_num = text_amount * (single_width + h_blank_space) * font_size / (width_mtext * h_ratio)
    line_num = math.ceil(line_num)
    total_height = line_num * (single_height + v_blank_space)
    total_width = width_mtext
    return total_width, total_height


"""
钻孔柱状图表格各角编号
①————②
|          |
④————③
"""


def graphic_zk_frame(gtmsp, pos1, pos2, pos3, pos4, h_ratio, v_ratio):
    """
    实现钻孔柱状图绘制功能
    :param gtmsp: modelspace
    :param pos1: 柱状图顶点①坐标
    :param pos2: 柱状图顶点②坐标
    :param pos3: 柱状图顶点③坐标
    :param pos4: 柱状图顶点④坐标
    :param h_ratio: 横向放大比例
    :param v_ratio: 纵向放大比例
    :return:柱状图外框
    """
    logging.info("绘制钻孔柱状图外框")
    pos1 = (pos1[0] * h_ratio, pos1[1] * v_ratio)
    pos2 = (pos2[0] * h_ratio, pos2[1] * v_ratio)
    pos3 = (pos3[0] * h_ratio, pos3[1] * v_ratio)
    pos4 = (pos4[0] * h_ratio, pos4[1] * v_ratio)
    logging.info("钻孔柱状图横线端点坐标计算")
    h_polyline0 = (pos1, pos2, pos3, pos4, pos1)
    h_polyline1 = ((pos1[0], pos1[1] - 2 * v_ratio), (pos2[0], pos2[1] - 2 * v_ratio))
    h_polyline2 = ((pos1[0], pos1[1] - 4 * v_ratio), (pos2[0], pos2[1] - 4 * v_ratio))
    h_polyline3_1 = ((pos1[0], pos1[1] - 6 * v_ratio), (pos1[0] + 10 * h_ratio, pos1[1] - 6 * v_ratio))
    h_polyline3_2 = ((pos1[0] + 12 * h_ratio, pos1[1] - 6 * v_ratio), (pos2[0], pos1[1] - 6 * v_ratio))
    h_polyline4 = ((pos1[0], pos1[1] - 8 * v_ratio), (pos2[0], pos2[1] - 8 * v_ratio))
    h_polyline5 = ((pos1[0], pos1[1] - 16 * v_ratio), (pos2[0], pos2[1] - 16 * v_ratio))
    logging.info("绘制钻孔柱状图上部竖线端点坐标计算")
    uv_polyline1 = ((pos1[0] + 6 * h_ratio, pos1[1]), (pos1[0] + 6 * h_ratio, pos1[1] - 8 * v_ratio))
    uv_polyline2 = ((pos1[0] + 10 * h_ratio, pos1[1] - 4 * v_ratio), (pos1[0] + 10 * h_ratio, pos1[1] - 8 * v_ratio))
    uv_polyline3 = ((pos1[0] + 12 * h_ratio, pos1[1] - 4 * v_ratio), (pos1[0] + 12 * h_ratio, pos1[1] - 8 * v_ratio))
    uv_polyline4 = ((pos1[0] + 19 * h_ratio, pos1[1] - 2 * v_ratio), (pos1[0] + 19 * h_ratio, pos1[1] - 8 * v_ratio))
    uv_polyline5 = ((pos1[0] + 23 * h_ratio, pos1[1] - 2 * v_ratio), (pos1[0] + 23 * h_ratio, pos1[1] - 8 * v_ratio))
    uv_polyline6 = ((pos1[0] + 28 * h_ratio, pos1[1] - 4 * v_ratio), (pos1[0] + 28 * h_ratio, pos1[1] - 8 * v_ratio))
    uv_polyline7 = ((pos1[0] + 34 * h_ratio, pos1[1] - 4 * v_ratio), (pos1[0] + 34 * h_ratio, pos1[1] - 8 * v_ratio))
    logging.info("绘制钻孔柱状图下部竖线端点坐标计算")
    dv_polyline1 = ((pos1[0] + 2 * h_ratio, pos1[1] - 8 * v_ratio), (pos4[0] + 2 * h_ratio, pos4[1]))
    dv_polyline2 = ((pos1[0] + 4 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 4 * h_ratio, pos4[1]))
    dv_polyline3 = ((pos1[0] + 6 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 6 * h_ratio, pos4[1]))
    dv_polyline4 = ((pos1[0] + 8 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 8 * h_ratio, pos4[1]))
    dv_polyline5 = ((pos1[0] + 10 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 10 * h_ratio, pos4[1]))
    dv_polyline6 = ((pos1[0] + 14 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 14 * h_ratio, pos4[1]))
    dv_polyline7 = ((pos1[0] + 25 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 25 * h_ratio, pos4[1]))
    dv_polyline8 = ((pos1[0] + 28 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 28 * h_ratio, pos4[1]))
    dv_polyline9 = ((pos1[0] + 31 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 31 * h_ratio, pos4[1]))
    dv_polyline10 = ((pos1[0] + 34 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 34 * h_ratio, pos4[1]))
    dv_polyline11 = ((pos1[0] + 37 * h_ratio, pos1[1] - 8 * v_ratio), (pos1[0] + 37 * h_ratio, pos4[1]))
    logging.info("绘制钻孔柱状图框架")
    h_all = [h_polyline0, h_polyline1, h_polyline2, h_polyline3_1, h_polyline3_2, h_polyline4, h_polyline5]
    uv_all = [uv_polyline1, uv_polyline2, uv_polyline3, uv_polyline4, uv_polyline5, uv_polyline6, uv_polyline7]
    dv_all = [dv_polyline1, dv_polyline2, dv_polyline3, dv_polyline4, dv_polyline5, dv_polyline6, dv_polyline7,
              dv_polyline8, dv_polyline9, dv_polyline10, dv_polyline11]
    for hh in h_all:
        gtmsp.add_lwpolyline(points=hh, format='xyb')
    for uvv in uv_all:
        gtmsp.add_lwpolyline(points=uvv, format='xyb')
    for dvv in dv_all:
        gtmsp.add_lwpolyline(points=dvv, format='xyb')


def graphic_outside(gtmsp, pos1, pos2, pos3, pos4, h_ratio, v_ratio):
    """
    绘制图件外框架
    :param gtmsp: modelspace
    :param pos1: 柱状图顶点①坐标
    :param pos2: 柱状图顶点②坐标
    :param pos3: 柱状图顶点③坐标
    :param pos4: 柱状图顶点④坐标
    :param h_ratio: 水平放大系数
    :param v_ratio: 垂直放大系数
    :return: 图件外框架
    """
    logging.info("绘制钻孔柱状图外框架")
    pos1 = (pos1[0] * h_ratio, pos1[1] * v_ratio)
    pos2 = (pos2[0] * h_ratio, pos2[1] * v_ratio)
    pos3 = (pos3[0] * h_ratio, pos3[1] * v_ratio)
    pos4 = (pos4[0] * h_ratio, pos4[1] * v_ratio)
    inside_frame = ((pos1[0] - 16 * h_ratio, pos1[1] + 5 * v_ratio), (pos2[0] + 16 * h_ratio, pos2[1] + 5 * v_ratio),
                    (pos3[0] + 16 * h_ratio, pos3[1] - 2 * v_ratio), (pos4[0] - 16 * h_ratio, pos4[1] - 2 * v_ratio),
                    (pos1[0] - 16 * h_ratio, pos1[1] + 5 * v_ratio))
    outside_frame = ((pos1[0] - 19 * h_ratio, pos1[1] + 6 * v_ratio), (pos2[0] + 17 * h_ratio, pos2[1] + 6 * v_ratio),
                     (pos3[0] + 17 * h_ratio, pos3[1] - 3 * v_ratio), (pos4[0] - 19 * h_ratio, pos4[1] - 3 * v_ratio),
                     (pos1[0] - 19 * h_ratio, pos1[1] + 6 * v_ratio))
    logging.info("使用多段线绘制钻孔柱状图框架")
    gtmsp.add_lwpolyline(points=inside_frame, format='xyb')
    gtmsp.add_lwpolyline(points=outside_frame, format='xyb')


def scale_design(layer_depth):
    """
    对钻孔柱状图填充比例尺进行设计
    :param layer_depth:地层的最大高度
    :return:图例填充比例尺
    """
    depth_option = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    ratio_option = [300, 500, 1000, 1200, 1500, 1600, 2000, 2200, 2500, 2600, 6000, 11000, 13000]
    if layer_depth <= depth_option[0]:
        res = ratio_option[0]
        return res
    elif layer_depth <= depth_option[-1]:
        for i in range(1, len(depth_option)):
            if depth_option[i - 1] < layer_depth <= depth_option[i]:
                res = ratio_option[i]
                return res
            else:
                continue
    else:
        res = layer_depth / 36 * 1000
        return res


def ratio_calculate(pos1, pos4, h_ratio, v_ratio, layer_attribute):
    """
    根据地层厚度及图框大小，计算图案填充比例尺
    :param pos1:边框顶点①
    :param pos4:边框顶点④
    :param h_ratio:横向缩放比例
    :param v_ratio:纵向缩放比例
    :param layer_attribute:地层相关属性数据集合
    :return:图案填充比例尺
    """
    logging.info('根据地层厚度计算比例尺')
    pos1 = (pos1[0] * h_ratio, pos1[1] * v_ratio)
    pos4 = (pos4[0] * h_ratio, pos4[1] * v_ratio)
    total_thickness = round(float(layer_attribute[-1]['layer_depth']), 1)
    total_section = (pos1[1] - 16 - pos4[1]) * v_ratio
    total_section = total_section // 10 * 10
    if total_thickness < total_section:
        hatch_ratio = total_section * 0.6 / total_thickness
    else:
        hatch_ratio = total_section * 0.8 / total_thickness
    print(hatch_ratio)
    return hatch_ratio


def text_write(gtmsp, scale, pos1, pos2, h_ratio, v_ratio, layer_attributes):
    """
    添加钻孔柱状图文字
    :param gtmsp: modelspace
    :param scale: 图件比例尺
    :param pos1: 柱状图顶点①坐标
    :param pos2: 柱状图顶点②坐标
    :param pos2: 柱状图顶点④坐标
    :param h_ratio: 水平放大系数
    :param v_ratio: 垂直放大系数
    :param layer_attributes: 地层属性
    :return: 钻孔柱状图相关文字
    """
    logging.info("添加钻孔柱状图固定字段文字")
    pos1 = (pos1[0] * h_ratio, pos1[1] * v_ratio)
    pos2 = (pos2[0] * h_ratio, pos2[1] * v_ratio)
    hatch_ratio = scale_design(layer_attributes[-1]['layer_depth'])
    gtmsp.add_mtext('钻 孔 柱 状 图', dxfattribs={'insert': ((pos1[0] + pos2[0]) / 2 - 3 * h_ratio, pos1[1] + 2 * v_ratio),
                                             'char_height': 1 * v_ratio, 'width': 23 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext('工程名称',
                    dxfattribs={'insert': (pos1[0] + 0.2 * h_ratio, pos1[1] - 0.5 * v_ratio),
                                'char_height': 0.5 * v_ratio, 'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('工程编号',
                    dxfattribs={'insert': (pos1[0] + 0.2 * h_ratio, pos1[1] - 2.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('孔口高程(m)',
                    dxfattribs={'insert': (pos1[0] + 0.2 * h_ratio, pos1[1] - 4.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('孔口直径(mm)',
                    dxfattribs={'insert': (pos1[0] + 0.2 * h_ratio, pos1[1] - 6.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('坐' + '\n' + '标',
                    dxfattribs={'width': 0.5 * h_ratio, 'char_height': 0.6 * v_ratio,
                                'insert': (pos1[0] + 10.5 * h_ratio, pos1[1] - 5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('钻孔编号',
                    dxfattribs={'insert': (pos1[0] + 19.5 * h_ratio, pos1[1] - 2.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('开工日期',
                    dxfattribs={'insert': (pos1[0] + 19.5 * h_ratio, pos1[1] - 4.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('竣工日期',
                    dxfattribs={'insert': (pos1[0] + 19.5 * h_ratio, pos1[1] - 6.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('稳定水位深度(m)',
                    dxfattribs={'insert': (pos1[0] + 28.2 * h_ratio, pos1[1] - 4.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('测量水位日期',
                    dxfattribs={'insert': (pos1[0] + 28.2 * h_ratio, pos1[1] - 6.5 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 6 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('地' + '\n' + '层' + '\n' + '编' + '\n' + '号',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.5 * v_ratio,
                                'insert': (pos1[0] + 0.6 * h_ratio, pos1[1] - 10.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('时' + '\n' + '代' + '\n' + '成' + '\n' + '因',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.5 * v_ratio,
                                'insert': (pos1[0] + 2.6 * h_ratio, pos1[1] - 10.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('层' + '\n' + '底' + '\n' + '高' + '\n' + '程' + '\n' + '(m)',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.5 * v_ratio,
                                'insert': (pos1[0] + 4.6 * h_ratio, pos1[1] - 10.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('分' + '\n' + '层' + '\n' + '厚' + '\n' + '度' + '\n' + '(m)',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.5 * v_ratio,
                                'insert': (pos1[0] + 6.6 * h_ratio, pos1[1] - 10.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('层' + '\n' + '底' + '\n' + '深' + '\n' + '度' + '\n' + '(m)',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.5 * v_ratio,
                                'insert': (pos1[0] + 8.6 * h_ratio, pos1[1] - 10.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('柱状图',
                    dxfattribs={'insert': (pos1[0] + 11 * h_ratio, pos1[1] - 12 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 3 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext(f'1:{round(hatch_ratio * (scale / 1000))}',
                    dxfattribs={'insert': (pos1[0] + 11.5 * h_ratio, pos1[1] - 14 * v_ratio),
                                'char_height': 0.4 * v_ratio,
                                'width': 2.5 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('岩土名称及其特征',
                    dxfattribs={'insert': (pos1[0] + 17 * h_ratio, pos1[1] - 12 * v_ratio),
                                'char_height': 0.5 * v_ratio,
                                'width': 8 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext('取' + '\n' + '\n' + '样',
                    dxfattribs={'char_height': 0.5 * v_ratio, 'width': 0.4 * h_ratio,
                                'insert': (pos1[0] + 26 * h_ratio, pos1[1] - 10.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('岩' + '\n' + '芯' + '\n' + '采' + '\n' + '样' + '\n' + '率' + '\n' + '%',
                    dxfattribs={'width': 0.1 * h_ratio, 'char_height': 0.5 * v_ratio,
                                'insert': (pos1[0] + 29.2 * h_ratio, pos1[1] - 8.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('RQD',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.4 * v_ratio,
                                'insert': (pos1[0] + 31.8 * h_ratio, pos1[1] - 10.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('%',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.4 * v_ratio,
                                'insert': (pos1[0] + 32 * h_ratio, pos1[1] - 11.5 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('标' + '\n' + '贯' + '\n' + '击' + '\n' + '数',
                    dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.5 * v_ratio,
                                'insert': (pos1[0] + 35 * h_ratio, pos1[1] - 9 * v_ratio), 'style': '固定字段文字'})
    gtmsp.add_mtext('（击数）',
                    dxfattribs={'insert': (pos1[0] + 35 * h_ratio, pos1[1] - 15 * v_ratio),
                                'char_height': 0.2 * v_ratio,
                                'width': 2 * h_ratio, 'style': '固定字段文字'})
    gtmsp.add_mtext(
        '稳' + '\n' + '定' + '\n' + '水' + '\n' + '位' + '\n' + '和' + '\n' + '水' + '\n' + '位' + '\n' + '日' + '\n' + '期',
        dxfattribs={'width': 0.4 * h_ratio, 'char_height': 0.4 * v_ratio,
                    'insert': (pos1[0] + 38 * h_ratio, pos1[1] - 9 * v_ratio), 'style': '固定字段文字'})
    logging.info("固定字段添加完成")


# 项目信息填写
def project_info_write(gtmsp, pos1, elevation, h_ratio, v_ratio, v_ratio_hatch, project_attribute):
    """
    实现项目基本信息填写功能
    :param gtmsp: modelspace
    :param pos1: 柱状图顶点①坐标
    :param elevation: 高程
    :param h_ratio: 水平缩放系数
    :param v_ratio: 垂直缩放系数
    :param v_ratio_hatch: 纵向新变换比例尺
    :param project_attribute: 项目基本信息字典
    :return: CAD钻孔柱状图项目基本信息
    """
    logging.info("填写项目基本信息")
    pos1 = (pos1[0] * h_ratio, pos1[1] * v_ratio)
    gtmsp.add_mtext(project_attribute['projectName'],
                    dxfattribs={'insert': (pos1[0] + 6.5 * h_ratio, pos1[1] - 0.5 * v_ratio),
                                'char_height': 0.6 * v_ratio,
                                'width': 34 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['projectNum'],
                    dxfattribs={'insert': (pos1[0] + 6.5 * h_ratio, pos1[1] - 2.5 * v_ratio),
                                'char_height': 0.6 * v_ratio,
                                'width': 13 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['pointNum'],
                    dxfattribs={'insert': (pos1[0] + 23.5 * h_ratio, pos1[1] - 2.5 * v_ratio),
                                'char_height': 0.6 * v_ratio,
                                'width': 17 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['actualPointAltitude'],
                    dxfattribs={'insert': (pos1[0] + 6.5 * h_ratio, pos1[1] - 4.5 * v_ratio),
                                'char_height': 0.6 * v_ratio,
                                'width': 4 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['expDiaDiameter'],
                    dxfattribs={'insert': (pos1[0] + 6.5 * h_ratio, pos1[1] - 6.5 * v_ratio),
                                'char_height': 0.6 * v_ratio,
                                'width': 4 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['actualPointX'],
                    dxfattribs={'insert': (pos1[0] + 12.5 * h_ratio, pos1[1] - 5 * v_ratio),
                                'char_height': 0.4 * v_ratio,
                                'width': 7 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['actualPointY'],
                    dxfattribs={'insert': (pos1[0] + 12.5 * h_ratio, pos1[1] - 7 * v_ratio),
                                'char_height': 0.4 * v_ratio,
                                'width': 7 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['pointStartDate'],
                    dxfattribs={'insert': (pos1[0] + 23.1 * h_ratio, pos1[1] - 5 * v_ratio),
                                'char_height': 0.3 * v_ratio,
                                'width': 5 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['pointEndDate'],
                    dxfattribs={'insert': (pos1[0] + 23.1 * h_ratio, pos1[1] - 7 * v_ratio),
                                'char_height': 0.3 * v_ratio,
                                'width': 5 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['waterDepth'],
                    dxfattribs={'insert': (pos1[0] + 34.1 * h_ratio, pos1[1] - 4.5 * v_ratio),
                                'char_height': 0.6 * v_ratio,
                                'width': 6 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(project_attribute['waterDate'],
                    dxfattribs={'insert': (pos1[0] + 34.1 * h_ratio, pos1[1] - 6.5 * v_ratio),
                                'char_height': 0.6 * v_ratio,
                                'width': 6 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_mtext(float(elevation[0]) - float(project_attribute['waterDepth']),
                    dxfattribs={'insert': (pos1[0] + 38 * h_ratio, pos1[1] - 15.6 * v_ratio - (
                                float(project_attribute['waterDepth']) - 0.2) * v_ratio_hatch),
                                'char_height': 0.5 * v_ratio_hatch,
                                'width': 3 * h_ratio, 'style': '项目信息文字'})
    gtmsp.add_line(
        start=(pos1[0] + 37 * h_ratio, pos1[1] - 16 * v_ratio - float(project_attribute['waterDepth']) * v_ratio_hatch),
        end=(pos1[0] + 40 * h_ratio, pos1[1] - 16 * v_ratio - float(project_attribute['waterDepth']) * v_ratio_hatch))
    gtmsp.add_mtext(project_attribute['waterDate'],
                    dxfattribs={'insert': (pos1[0] + 37.5 * h_ratio, pos1[1] - 15.6 * v_ratio - (
                                float(project_attribute['waterDepth']) + 1.6) * v_ratio_hatch),
                                'char_height': 0.5 * v_ratio_hatch,
                                'width': 4 * h_ratio, 'style': '项目信息文字'})
    hole_hatch = gtmsp.add_hatch(color=7)
    hole_hatch.paths.add_polyline_path([(pos1[0] + 37 * h_ratio, pos1[1] - 16 * v_ratio - (
                float(project_attribute['waterDepth']) - 1.6) * v_ratio_hatch),
                                        (pos1[0] + (37 + 0.5) * h_ratio, pos1[1] - 16 * v_ratio - (
                                                    float(project_attribute['waterDepth']) - 1.6) * v_ratio_hatch),
                                        (pos1[0] + (37 + 0.25) * h_ratio, pos1[1] - 16 * v_ratio - (
                                                    float(project_attribute['waterDepth']) - 0.8) * v_ratio_hatch),
                                        (pos1[0] + 37 * h_ratio, pos1[1] - 16 * v_ratio - (
                                                    float(project_attribute['waterDepth']) - 1.6) * v_ratio_hatch)],
                                       is_closed=1, flags=1)
    gtmsp.add_line(start=(pos1[0] + (37 - 0.1) * h_ratio,
                          pos1[1] - 16 * v_ratio - (float(project_attribute['waterDepth']) - 0.8) * v_ratio_hatch),
                   end=(pos1[0] + (37 + 0.6) * h_ratio,
                        pos1[1] - 16 * v_ratio - (float(project_attribute['waterDepth']) - 0.8) * v_ratio_hatch))
    gtmsp.add_line(start=(pos1[0] + (37 + 0.05) * h_ratio,
                          pos1[1] - 16 * v_ratio - (float(project_attribute['waterDepth']) - 0.5) * v_ratio_hatch),
                   end=(pos1[0] + (37 + 0.45) * h_ratio,
                        pos1[1] - 16 * v_ratio - (float(project_attribute['waterDepth']) - 0.5) * v_ratio_hatch))
    gtmsp.add_line(start=(pos1[0] + (37 + 0.2) * h_ratio,
                          pos1[1] - 16 * v_ratio - (float(project_attribute['waterDepth']) - 0.2) * v_ratio_hatch),
                   end=(pos1[0] + (37 + 0.3) * h_ratio,
                        pos1[1] - 16 * v_ratio - (float(project_attribute['waterDepth']) - 0.2) * v_ratio_hatch))
    logging.info("项目基本信息填写完成")


# 取样、岩芯取样率、RQD、标贯、稳定水位和水位日期
def rest_info_write(gtmsp, pos1, h_ratio, v_ratio, specimen_attribute, inject_attribute, rock_attribute):
    """
    实现取样、岩芯取样率、RQD、标贯、稳定水位和水位日期样式设计功能
    :param gtmsp:modelspace
    :param pos1:柱状图顶点①坐标
    :param h_ratio:水平缩放系数
    :param v_ratio:垂直缩放系数
    :param specimen_attribute:地层属性
    :param inject_attribute:标贯属性
    :param rock_attribute: 岩芯采样属性
    :return:取样、岩芯取样率、RQD、标贯、稳定水位和水位日期等内容
    """
    logging.info("填写取样、岩芯取样率、RQD、标贯、稳定水位和水位日期等信息")
    pos1 = (pos1[0] * h_ratio, pos1[1] * v_ratio)
    logging.info("绘制岩芯取样率刻度线及刻度值")
    gtmsp.add_line(start=(pos1[0] + 28.6 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 28.6 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('20',
                   dxfattribs={'insert': (pos1[0] + 28.4 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    gtmsp.add_line(start=(pos1[0] + 29.2 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 29.2 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('40',
                   dxfattribs={'insert': (pos1[0] + 29 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    gtmsp.add_line(start=(pos1[0] + 29.8 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 29.8 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('60',
                   dxfattribs={'insert': (pos1[0] + 29.6 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    gtmsp.add_line(start=(pos1[0] + 30.4 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 30.4 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('80',
                   dxfattribs={'insert': (pos1[0] + 30.2 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    logging.info("添加RQD刻度线")
    gtmsp.add_line(start=(pos1[0] + 31.6 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 31.6 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('20',
                   dxfattribs={'insert': (pos1[0] + 31.4 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    gtmsp.add_line(start=(pos1[0] + 32.2 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 32.2 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('40',
                   dxfattribs={'insert': (pos1[0] + 32 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    gtmsp.add_line(start=(pos1[0] + 32.8 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 32.8 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('60',
                   dxfattribs={'insert': (pos1[0] + 32.6 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    gtmsp.add_line(start=(pos1[0] + 33.4 * h_ratio, pos1[1] - 16 * v_ratio),
                   end=(pos1[0] + 33.4 * h_ratio, pos1[1] - 15.4 * v_ratio))
    gtmsp.add_text('80',
                   dxfattribs={'insert': (pos1[0] + 33.2 * h_ratio, pos1[1] - 15.3 * v_ratio), 'height': 0.3 * v_ratio})
    logging.info("上述数据信息填写完成")
    try:
        logging.info("创建取样编号及深度")
        for specimen_i in range(len(specimen_attribute)):
            gtmsp.add_text(specimen_attribute[specimen_i]['specimen_num'],
                           dxfattribs={'insert': (pos1[0] + 26.3 * h_ratio,
                                                  pos1[1] - (16 + float(specimen_attribute[specimen_i][
                                                                            'specimen_start']) - 0.2) * v_ratio),
                                       'height': 0.4 * v_ratio, 'style': '项目信息文字'})
            gtmsp.add_line(start=(pos1[0] + 25 * h_ratio,
                                  pos1[1] - (16 + float(specimen_attribute[specimen_i]['specimen_start'])) * v_ratio),
                           end=(pos1[0] + 28 * h_ratio,
                                pos1[1] - (16 + float(specimen_attribute[specimen_i]['specimen_start'])) * v_ratio))
            gtmsp.add_text(
                f"{'%.2f' % float(specimen_attribute[specimen_i]['specimen_start'])}-{'%.2f' % (float(specimen_attribute[specimen_i]['specimen_start']) + 0.2)}",
                dxfattribs={'insert': (pos1[0] + 25.2 * h_ratio, pos1[1] - (
                            16 + float(specimen_attribute[specimen_i]['specimen_start']) + 0.4) * v_ratio),
                            'height': 0.4 * v_ratio, 'style': '项目信息文字'})
    except Exception as err:
        logging.info("取样编号及深度数据内容创建失败，数据不完整")
        print(err.__class__.__name__ + ":", err)
    else:
        logging.info("取样编号及深度数据内容创建完成")
    logging.info("填写标准贯入试验相关数据信息")
    try:
        for inject_i in range(len(inject_attribute)):
            gtmsp.add_text(f"={inject_attribute[inject_i]['inject_hit_number']}",
                           dxfattribs={'insert': (pos1[0] + 34.3 * h_ratio, pos1[1] -
                                                  (16 + inject_attribute[inject_i]['bottom_depth'] - 0.2) * v_ratio),
                                       'height': 0.4 * v_ratio, 'style': '项目信息文字'})
            gtmsp.add_line(start=(pos1[0] + 34 * h_ratio,
                                  pos1[1] - (16 + inject_attribute[inject_i]['bottom_depth']) * v_ratio),
                           end=(pos1[0] + 37 * h_ratio,
                                pos1[1] - (16 + inject_attribute[inject_i]['bottom_depth']) * v_ratio))
            gtmsp.add_text(
                f"{'%.2f' % (float(inject_attribute[inject_i]['bottom_depth']) - 0.3)}-{'%.2f' % float(inject_attribute[inject_i]['bottom_depth'])}",
                dxfattribs={'insert': (pos1[0] + 34.2 * h_ratio,
                                       pos1[1] - (16 + (inject_attribute[inject_i]['bottom_depth'] -
                                                        inject_attribute[inject_i]['top_depth']) + 0.4) * v_ratio),
                            'height': 0.4 * v_ratio, 'style': '项目信息文字'})
    except Exception as err:
        logging.info("相关数据不全，导致标准贯入试验相关数据信息填写失败")
        print(err.__class__.__name__ + ":", err)
    else:
        logging.info("标准贯入试验相关数据信息填写完成")
    # 岩芯采样率
    logging.info("进行岩芯采样率数据整理及绘制任务")
    rock_attribute.insert(0, {'specimen_depth': 0, 'specimen_rate': int(rock_attribute[0]['specimen_rate'])})
    cal_curve = []
    logging.info("使用多段线绘制岩芯取样线")
    try:
        specimen_depth = 0
        for rock_item in range(len(rock_attribute)):
            cal_curve.append((pos1[0] + (28 + 3 * int(rock_attribute[rock_item]['specimen_rate']) * 0.01) * h_ratio,
                              pos1[1] - (16 + float(specimen_depth)) * v_ratio))
            cal_curve.append((pos1[0] + (28 + 3 * int(rock_attribute[rock_item]['specimen_rate']) * 0.01) * h_ratio,
                              pos1[1] - (16 + float(rock_attribute[rock_item]['specimen_depth'])) * v_ratio))
            specimen_depth = float(rock_attribute[rock_item]['specimen_depth'])
    except Exception as err:
        logging.info("数据类型错误或者数据不全，岩芯取样率曲线绘制失败")
        print(err.__class__.__name__ + ":", err)
    else:
        logging.info("岩芯取样率曲线绘制成功")
    cal_curve.append((pos1[0] + 28 * h_ratio, pos1[1] - (16 + float(rock_attribute[-1]['specimen_depth'])) * v_ratio))
    gtmsp.add_lwpolyline(points=cal_curve, format='xyb', dxfattribs={'color': 1})
    logging.info("使用多段线绘制岩芯取样线完成")


# 地层信息填写
def layers_info_write(gtmsp, pos1, h_ratio, v_ratio, layer_attributes):
    """
    实现地层信息填写功能
    :param gtmsp:modelspace
    :param pos1:柱状图顶点①坐标
    :param h_ratio:水平放大系数
    :param v_ratio:垂直放大系数
    :param layer_attributes:地层信息相关内容
    :return:钻孔柱状图地层信息
    """
    logging.info("填写地层数据信息 ")
    pos1 = (pos1[0] * h_ratio, pos1[1] * v_ratio)
    thickness = 0
    hatch_thickness = 0
    mtext_thickness = 0
    new_mtext_thickness = 0
    hatch_ratio = scale_design(layer_attributes[-1]['layer_depth']) / 1000
    v_ratio_hatch = v_ratio * (1 / hatch_ratio)
    fill_legend = ['ANSI31', 'ANSI36', 'GRAVEL', 'TRIANG', 'ARHBONE', 'GOST_GROUND', 'ANSI31', 'TRIANG', 'ANSI36',
                   'GRAVEL', 'ANSI31', 'ANSI36', 'GRAVEL', 'TRIANG', 'ARHBONE', 'GOST_GROUND', 'ANSI31', 'TRIANG',
                   'ANSI36', 'GRAVEL']*10
    counter = 0
    logging.info('遍历地层属性，写入地层信息')
    for layer_attributes_i in layer_attributes:
        try:
            gtmsp.add_mtext(layer_attributes_i['order_number'], dxfattribs={
                'insert': (
                    pos1[0] + 0.5 * h_ratio,
                    pos1[1] - (15.5 - 0.1) * v_ratio - (
                                float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                'char_height': 0.7 * v_ratio_hatch, 'width': 2 * h_ratio, 'style': '项目信息文字'})
        except Exception as err:
            logging.error("数据类型错误或者值缺失")
            print(err.__class__.__name__ + ":", err)
        try:
            if layer_attributes_i['era_cause'] == '信息缺失':
                gtmsp.add_mtext(layer_attributes_i['era_cause'], dxfattribs={
                    'insert': (
                        pos1[0] + 2.1 * h_ratio,
                        pos1[1] - (15.5 - 0.1) * v_ratio - (
                                float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                    'char_height': 0.8 * v_ratio_hatch, 'width': 2 * h_ratio, 'style': '项目信息文字'})
            else:
                gtmsp.add_mtext(layer_attributes_i['era_cause'][0][0], dxfattribs={
                    'insert': (
                        pos1[0] + 2.1 * h_ratio,
                        pos1[1] - (15.5 - 0.1) * v_ratio - (
                                    float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                    'char_height': 0.8 * v_ratio_hatch, 'width': 2 * h_ratio, 'style': '项目信息文字'})
                gtmsp.add_mtext(layer_attributes_i['era_cause'][0][1:], dxfattribs={
                    'insert': (
                        pos1[0] + 2.4 * h_ratio,
                        pos1[1] - (15.7 - 0.1) * v_ratio - (
                                float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                    'char_height': 0.5 * v_ratio_hatch, 'width': 1 * h_ratio, 'style': '项目信息文字'})
                gtmsp.add_mtext(layer_attributes_i['era_cause'][1], dxfattribs={
                    'insert': (
                        pos1[0] + 2.4 * h_ratio,
                        pos1[1] - (15.3 - 0.1) * v_ratio - (
                                float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                    'char_height': 0.5 * v_ratio_hatch, 'width': 2 * h_ratio, 'style': '项目信息文字'})
        except Exception as err:
            logging.error("地质年代或地质成因缺失")
            print(err.__class__.__name__ + ":", err)
        else:
            logging.error("地质年代及成因填写成功")
        try:
            gtmsp.add_mtext(layer_attributes_i['bottom_elevation'], dxfattribs={
                'insert': (
                    pos1[0] + 4.1 * h_ratio,
                    pos1[1] - (15.5 - 0.1) * v_ratio - (
                                float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                'char_height': 0.6 * v_ratio_hatch, 'width': 2 * h_ratio, 'style': '项目信息文字'})
        except Exception as err:
            logging.error("数据类型错误或者值缺失")
            print(err.__class__.__name__ + ":", err)
        try:
            gtmsp.add_mtext(float(layer_attributes_i['layer_thickness']), dxfattribs={
                'insert': (
                    pos1[0] + 6.5 * h_ratio,
                    pos1[1] - (15.5 - 0.1) * v_ratio - (
                                float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                'char_height': 0.6 * v_ratio_hatch, 'width': 2 * h_ratio, 'style': '项目信息文字'})
        except Exception as err:
            logging.error("数据类型错误或者值缺失")
            print(err.__class__.__name__ + ":", err)
        try:
            gtmsp.add_mtext(layer_attributes_i['layer_depth'], dxfattribs={
                'insert': (
                    pos1[0] + 8.5 * h_ratio,
                    pos1[1] - (15.5 - 0.1) * v_ratio - (
                                float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                'char_height': 0.6 * v_ratio_hatch, 'width': 2 * h_ratio, 'style': '项目信息文字'})
        except Exception as err:
            logging.error("数据类型错误或者值缺失")
            print(err.__class__.__name__ + ":", err)
        try:
            gtmsp.add_line(
                start=(pos1[0], pos1[1] - 16 * v_ratio - (
                            hatch_thickness + float(layer_attributes_i['layer_thickness'])) * v_ratio_hatch),
                end=(pos1[0] + 14 * h_ratio,
                     pos1[1] - 16 * v_ratio - (
                                 hatch_thickness + float(layer_attributes_i['layer_thickness'])) * v_ratio_hatch))
        except Exception as err:
            logging.error("数据类型错误或者值缺失")
            print(err.__class__.__name__ + ":", err)
        logging.info("进行地层图例填充")
        graphic_polyline = gtmsp.add_lwpolyline(
            points=((pos1[0] + 10 * h_ratio, pos1[1] - 16 * v_ratio - hatch_thickness * v_ratio_hatch),
                    (pos1[0] + 14 * h_ratio, pos1[1] - 16 * v_ratio - hatch_thickness * v_ratio_hatch),
                    (pos1[0] + 14 * h_ratio,
                     pos1[1] - 16 * v_ratio - (
                                 float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                    (pos1[0] + 10 * h_ratio,
                     pos1[1] - 16 * v_ratio - (
                                 float(layer_attributes_i['layer_thickness']) + hatch_thickness) * v_ratio_hatch),
                    (pos1[0] + 10 * h_ratio, pos1[1] - 16 * v_ratio - hatch_thickness * v_ratio_hatch)), format='xyb')
        hole_hatch = gtmsp.add_hatch(color=7)
        hole_hatch.set_pattern_fill(fill_legend[counter + 1], scale=0.1 * v_ratio)
        zk_path = hole_hatch.paths.add_polyline_path(graphic_polyline.get_points(format='xyb'))
        hole_hatch.associate(zk_path, [graphic_polyline])
        logging.info("图例填充完成")
        logging.info("岩土名称及其特征")
        describe_length = len(layer_attributes_i['layer_describe'])
        text_width, text_height = text_altitude(describe_length, 9, 0.5, h_ratio, v_ratio)
        mtext_thickness += text_height
        logging.info("添加多行文本")
        if counter == 0:
            gtmsp.add_mtext(layer_attributes_i['layer_describe'],
                            dxfattribs={'width': 8 * h_ratio, 'char_height': 0.3 * v_ratio,
                                        'insert': (pos1[0] + 14.8 * h_ratio,
                                                   pos1[1] - (16 + 0.2) * v_ratio),
                                        'style': '项目信息文字'})
        else:
            gtmsp.add_mtext(layer_attributes_i['layer_describe'],
                            dxfattribs={'width': 8 * h_ratio, 'char_height': 0.3 * v_ratio,
                                        'insert': (pos1[0] + 14.8 * h_ratio,
                                                   pos1[1] - (16 + 1) * v_ratio - new_mtext_thickness * v_ratio_hatch),
                                        'style': '项目信息文字'})
        # 分割线
        thickness += (float(layer_attributes_i['layer_thickness']))
        new_mtext_thickness += text_height
        gtmsp.add_lwpolyline(points=((pos1[0] + 14 * h_ratio, pos1[1] - 16 * v_ratio - thickness * v_ratio_hatch),
                                     (pos1[0] + 14.3 * h_ratio,
                                      pos1[1] - (16 + 0.5) * v_ratio - new_mtext_thickness * v_ratio_hatch),
                                     (pos1[0] + 25 * h_ratio,
                                      pos1[1] - (16 + 0.5) * v_ratio - new_mtext_thickness * v_ratio_hatch)))
        hatch_thickness += float(layer_attributes_i['layer_thickness'])
        counter += 1
    logging.info('地层属性写入CAD完成')


# 实现从获取数据到实现svg文件绘制功能
def main(scale, expStratumList, elevation, geo_era_cause, project_attribute, geo_describe, specimen_attribute,
         inject_attribute, rock_attribute, export_route, export_route1):
    """
    实现从获取数据到实现svg文件绘制功能
    :param scale: 图形缩放比例
    :param elevation: 高程数据信息
    :param geo_era_cause: 地质年代成因
    :param project_attribute: 项目属性
    :param geo_describe: 地层描述
    :param specimen_attribute: 地层属性
    :param inject_attribute: 标贯属性
    :param rock_attribute: 岩芯采样属性
    :param export_route: svg文件导出路径
    :param export_route1: dxf文件导出路径
    :return: SVG格式文件
    """
    logging.info("图形初始定点")
    corner_one = (100, 100)
    corner_two = (140, 100)
    corner_three = (140, 40)
    corner_four = (100, 40)
    logging.info("图形比例尺设置")
    hole_rate = 1000
    change_rate_one = scale / hole_rate
    change_rate_two = scale / hole_rate
    logging.info("生成地层序号")
    layer_order = []
    for i in range(len(expStratumList)):
        layer_order.append(f"({i + 1})")
    logging.info("创建地层信息")
    layer_attributes = []
    esn = 0
    depth_total = 0
    for es in range(len(elevation)):
        depth_total += float(expStratumList[es]['depth'])
        if es != 0 and float(elevation[es-1]) - float(elevation[es]) == 0:
            esn += 0
        else:
            layer_attributes.append(
                {'order_number': layer_order[esn], 'era_cause': geo_era_cause[es],
                 'bottom_elevation': round(float(elevation[es]), 2),
                 'layer_thickness': round(float(expStratumList[es]['depth']), 2),
                 'layer_depth': round(depth_total, 2),
                 'layer_describe': geo_describe[es]})
            esn += 1
    hatch_ratio = scale_design(layer_attributes[-1]['layer_depth']) / 1000
    v_ratio_hatch = change_rate_two * (1 / hatch_ratio)
    logging.info("绘制钻孔柱状图框架")
    graphic_zk_frame(hole_msp, corner_one, corner_two, corner_three, corner_four, change_rate_one, change_rate_two)
    logging.info("钻孔柱状图框架绘制完成")
    logging.info("绘制钻孔柱状图外边框")
    graphic_outside(hole_msp, corner_one, corner_two, corner_three, corner_four, change_rate_one, change_rate_two)
    logging.info("外边框绘制完成")
    logging.info("写入项目主要信息")
    project_info_write(hole_msp, corner_one, elevation, change_rate_one, change_rate_two, v_ratio_hatch,
                       project_attribute)
    logging.info("项目主要信息填写完成")
    logging.info("写入项目剩余信息")
    rest_info_write(hole_msp, corner_one, change_rate_one, change_rate_two, specimen_attribute, inject_attribute,
                    rock_attribute)
    logging.info("项目剩余信息填写完成")
    logging.info("进行文字填写")
    text_write(hole_msp, scale, corner_one, corner_two, change_rate_one, change_rate_two, layer_attributes)
    logging.info("文字内容填写完成")
    logging.info("写入地层信息")
    layers_info_write(hole_msp, corner_one, change_rate_one, change_rate_two, layer_attributes)
    logging.info("地层信息填写完成")
    hole_doc.saveas(export_route1)
    logging.info("将图形保存为DXF格式文件")
    svg_transform(hole_doc, export_route)
    logging.info("将图形保存为SVG格式文件")
