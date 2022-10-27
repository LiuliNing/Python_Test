# -*- coding: utf-8 -*-
""" 
@Time    : 2021/12/13 9:39
@Author  : 梅迁
@FileName: draw_zk.py
@SoftWare: PyCharm
"""
import ezdxf
import matplotlib.pyplot as plt
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

zk_doc = ezdxf.new()
zk_msp = zk_doc.modelspace()


# 多行文本框高度及宽度计算
def text_altitude(text_amount, width_mtext, size, hcoef1, vcoef1):
    """
    实现多行文本框宽度及高度计算
    :param text_amount:文本文字的总数目
    :param width_mtext:文本框设置宽度
    :param size:字体高度
    :param hcoef1:水平放大系数
    :param vcoef1:竖向放大系数
    :return:多行文本框的宽度与高度
    """
    font_size = size
    single_height = 1.05*vcoef1
    single_width = 0.7*hcoef1
    h_blank_space = 0.18*hcoef1
    v_blank_space = 0.75*vcoef1

    # 行数目
    line_num = (text_amount*single_width+(text_amount-1)*h_blank_space)*font_size/(width_mtext*hcoef1)
    total_height = (line_num*single_height + (line_num-1)*v_blank_space)*font_size
    total_width = width_mtext
    return total_width, total_height


"""
钻孔柱状图表格各角编号
①————②
|          |
④————③
"""


# 柱状图外框（高：1.03， 宽：0.6）
def graphic_zk_frame(gtmsp, pos1, pos2, pos3, pos4, hcoef, vcoef):
    """
    实现钻孔柱状图绘制功能
    :param gtmsp: modelspace
    :param pos1: 柱状图顶点①坐标
    :param pos2: 柱状图顶点②坐标
    :param pos3: 柱状图顶点③坐标
    :param pos4: 柱状图顶点④坐标
    :param hcoef: 横向放大比例
    :param vcoef: 纵向放大比例
    :return:
    """
    pos1 = (pos1[0] * hcoef, pos1[1] * vcoef)
    pos2 = (pos2[0] * hcoef, pos2[1] * vcoef)
    pos3 = (pos3[0] * hcoef, pos3[1] * vcoef)
    pos4 = (pos4[0] * hcoef, pos4[1] * vcoef)
    h_polyline0 = (pos1, pos2, pos3, pos4, pos1)
    h_polyline1 = ((pos1[0], pos1[1] - 2 * vcoef), ((pos2[0], pos2[1] - 2 * vcoef)))
    h_polyline2 = ((pos1[0], pos1[1] - 4 * vcoef), ((pos2[0], pos2[1] - 4 * vcoef)))
    h_polyline3_1 = ((pos1[0], pos1[1] - 6 * vcoef), (pos1[0] + 10 * hcoef, pos1[1] - 6 * vcoef))
    h_polyline3_2 = ((pos1[0] + 12 * hcoef, pos1[1] - 6 * vcoef), (pos2[0], pos1[1] - 6 * vcoef))
    h_polyline4 = ((pos1[0], pos1[1] - 8 * vcoef), ((pos2[0], pos2[1] - 8 * vcoef)))
    h_polyline5 = ((pos1[0], pos1[1] - 16 * vcoef), ((pos2[0], pos2[1] - 16 * vcoef)))

    uv_polyline1 = ((pos1[0] + 6 * hcoef, pos1[1]), (pos1[0] + 6 * hcoef, pos1[1] - 8 * vcoef))
    uv_polyline2 = ((pos1[0] + 10 * hcoef, pos1[1] - 4 * vcoef), (pos1[0] + 10 * hcoef, pos1[1] - 8 * vcoef))
    uv_polyline3 = ((pos1[0] + 12 * hcoef, pos1[1] - 4 * vcoef), (pos1[0] + 12 * hcoef, pos1[1] - 8 * vcoef))
    uv_polyline4 = ((pos1[0] + 19 * hcoef, pos1[1] - 2 * vcoef), (pos1[0] + 19 * hcoef, pos1[1] - 8 * vcoef))
    uv_polyline5 = ((pos1[0] + 23 * hcoef, pos1[1] - 2 * vcoef), (pos1[0] + 23 * hcoef, pos1[1] - 8 * vcoef))
    uv_polyline6 = ((pos1[0] + 28 * hcoef, pos1[1] - 4 * vcoef), (pos1[0] + 28 * hcoef, pos1[1] - 8 * vcoef))
    uv_polyline7 = ((pos1[0] + 34 * hcoef, pos1[1] - 4 * vcoef), (pos1[0] + 34 * hcoef, pos1[1] - 8 * vcoef))

    dv_polyline1 = ((pos1[0] + 2 * hcoef, pos1[1] - 8 * vcoef), (pos4[0] + 2 * hcoef, pos4[1]))
    dv_polyline2 = ((pos1[0] + 4 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 4 * hcoef, pos4[1]))
    dv_polyline3 = ((pos1[0] + 6 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 6 * hcoef, pos4[1]))
    dv_polyline4 = ((pos1[0] + 8 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 8 * hcoef, pos4[1]))
    dv_polyline5 = ((pos1[0] + 10 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 10 * hcoef, pos4[1]))
    dv_polyline6 = ((pos1[0] + 14 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 14 * hcoef, pos4[1]))
    dv_polyline7 = ((pos1[0] + 25 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 25 * hcoef, pos4[1]))
    dv_polyline8 = ((pos1[0] + 28 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 28 * hcoef, pos4[1]))
    dv_polyline9 = ((pos1[0] + 31 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 31 * hcoef, pos4[1]))
    dv_polyline10 = ((pos1[0] + 34 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 34 * hcoef, pos4[1]))
    dv_polyline11 = ((pos1[0] + 37 * hcoef, pos1[1] - 8 * vcoef), (pos1[0] + 37 * hcoef, pos4[1]))

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


# 外框
def graphic_outside(gtmsp, pos1, pos2, pos3, pos4, hcoef, vcoef):
    """
    绘制图件外框架
    :param gtmsp: modelspace
    :param pos1: 柱状图顶点①坐标
    :param pos2: 柱状图顶点②坐标
    :param pos3: 柱状图顶点③坐标
    :param pos4: 柱状图顶点④坐标
    :param hcoef: 水平放大系数
    :param vcoef: 垂直放大系数
    :return: 图件外框架
    """
    pos1 = (pos1[0] * hcoef, pos1[1] * vcoef)
    pos2 = (pos2[0] * hcoef, pos2[1] * vcoef)
    pos3 = (pos3[0] * hcoef, pos3[1] * vcoef)
    pos4 = (pos4[0] * hcoef, pos4[1] * vcoef)
    in_lwpolyline = ((pos1[0] - 16 * hcoef, pos1[1] + 5 * vcoef),
                     (pos2[0] + 16 * hcoef, pos2[1] + 5 * vcoef),
                     (pos3[0] + 16 * hcoef, pos3[1] - 2 * vcoef),
                     (pos4[0] - 16 * hcoef, pos4[1] - 2 * vcoef),
                     (pos1[0] - 16 * hcoef, pos1[1] + 5 * vcoef))
    out_lwpolyline = ((pos1[0] - 19 * hcoef, pos1[1] + 6 * vcoef),
                      (pos2[0] + 17 * hcoef, pos2[1] + 6 * vcoef),
                      (pos3[0] + 17 * hcoef, pos3[1] - 3 * vcoef),
                      (pos4[0] - 19 * hcoef, pos4[1] - 3 * vcoef),
                      (pos1[0] - 19 * hcoef, pos1[1] + 6 * vcoef))
    gtmsp.add_lwpolyline(points=in_lwpolyline, format='xyb')
    gtmsp.add_lwpolyline(points=out_lwpolyline, format='xyb')


# 添加文字
def text_write(gtmsp, zkrate, pos1, pos2, pos3, pos4, hcoef, vcoef):
    """
    添加钻孔柱状图文字
    :param gtmsp: modelspace
    :param pos1: 柱状图顶点①坐标
    :param pos2: 柱状图顶点②坐标
    :param pos3: 柱状图顶点③坐标
    :param pos4: 柱状图顶点④坐标
    :param hcoef: 水平放大系数
    :param vcoef: 垂直放大系数
    :return: 钻孔柱状图相关文字
    """
    pos1 = (pos1[0] * hcoef, pos1[1] * vcoef)
    pos2 = (pos2[0] * hcoef, pos2[1] * vcoef)
    pos3 = (pos3[0] * hcoef, pos3[1] * vcoef)
    pos4 = (pos4[0] * hcoef, pos4[1] * vcoef)
    # 钻孔柱状图
    gtmsp.add_text('钻 孔 柱 状 图', dxfattribs={'insert': ((pos1[0] + pos2[0]) / 2 - 3 * hcoef, pos1[1] + vcoef),
                                            'height': 1.03 * vcoef})
    gtmsp.add_text('工程名称',
                   dxfattribs={'insert': (pos1[0] + 0.2 * hcoef, pos1[1] - 1.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text('工程编号',
                   dxfattribs={'insert': (pos1[0] + 0.2 * hcoef, pos1[1] - 3.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text('孔口高程(m)',
                   dxfattribs={'insert': (pos1[0] + 0.2 * hcoef, pos1[1] - 5.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text('孔口直径(mm)',
                   dxfattribs={'insert': (pos1[0] + 0.2 * hcoef, pos1[1] - 7.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_mtext('坐标', dxfattribs={'width': 0.6 * hcoef, 'char_height': 1.03 * vcoef,
                                      'insert': (pos1[0] + 10.5 * hcoef, pos1[1] - 4.5 * vcoef)})
    gtmsp.add_text('钻孔编号',
                   dxfattribs={'insert': (pos1[0] + 19.5 * hcoef, pos1[1] - 3.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text('开工日期',
                   dxfattribs={'insert': (pos1[0] + 19.5 * hcoef, pos1[1] - 5.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text('竣工日期',
                   dxfattribs={'insert': (pos1[0] + 19.5 * hcoef, pos1[1] - 7.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text('稳定水位深度(m)',
                   dxfattribs={'insert': (pos1[0] + 28.2 * hcoef, pos1[1] - 5.5 * vcoef), 'height': 0.9 * vcoef})
    gtmsp.add_text('测量水位日期',
                   dxfattribs={'insert': (pos1[0] + 28.2 * hcoef, pos1[1] - 7.5 * vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_mtext('地层编号', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                        'insert': (pos1[0] + 0.6 * hcoef, pos1[1] - 9 * vcoef)})
    gtmsp.add_mtext('时代成因', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                        'insert': (pos1[0] + 2.6 * hcoef, pos1[1] - 9 * vcoef)})
    gtmsp.add_mtext('层底高程m', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                         'insert': (pos1[0] + 4.6 * hcoef, pos1[1] - 9 * vcoef)})
    gtmsp.add_mtext('分层厚度m', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                         'insert': (pos1[0] + 6.6 * hcoef, pos1[1] - 9 * vcoef)})
    gtmsp.add_mtext('层底深度m', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                         'insert': (pos1[0] + 8.6 * hcoef, pos1[1] - 9 * vcoef)})
    gtmsp.add_text('柱状图', dxfattribs={'insert': (pos1[0] + 11 * hcoef, pos1[1] - 12 * vcoef), 'height': 0.7 * vcoef})
    gtmsp.add_text(f'1：{round(zkrate)}',
                   dxfattribs={'insert': (pos1[0] + 11.5 * hcoef, pos1[1] - 15.5 * vcoef), 'height': 0.4 * vcoef})
    gtmsp.add_text('岩土名称及其特征',
                   dxfattribs={'insert': (pos1[0] + 17 * hcoef, pos1[1] - 12 * vcoef), 'height': 0.8 * vcoef})
    gtmsp.add_mtext('取' + '\n' + '\n' + '样',
                    dxfattribs={'char_height': 0.8 * vcoef, 'insert': (pos1[0] + 26 * hcoef, pos1[1] - 10.5 * vcoef)})
    gtmsp.add_mtext('岩芯采样率%', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.6 * vcoef,
                                          'insert': (pos1[0] + 29.2 * hcoef, pos1[1] - 8.2 * vcoef)})
    gtmsp.add_mtext('RQD', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                       'insert': (pos1[0] + 31.8 * hcoef, pos1[1] - 12 * vcoef)})
    gtmsp.add_mtext('%', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                     'insert': (pos1[0] + 32 * hcoef, pos1[1] - 13 * vcoef)})
    gtmsp.add_mtext('标贯击数', dxfattribs={'width': 0.4 * hcoef, 'char_height': 0.7 * vcoef,
                                        'insert': (pos1[0] + 35 * hcoef, pos1[1] - 9 * vcoef)})
    gtmsp.add_text('（击数）', dxfattribs={'insert': (pos1[0] + 35 * hcoef, pos1[1] - 15.8 * vcoef), 'height': 0.3 * vcoef})
    gtmsp.add_mtext('稳定水位和水位日期', dxfattribs={'width': 0.6 * hcoef, 'char_height': 0.6 * vcoef,
                                             'insert': (pos1[0] + 38 * hcoef, pos1[1] - 9 * vcoef)})


# 项目信息填写
def project_info_write(gtmsp, pos1, hcoef, vcoef, attr2):
    """
    实现项目基本信息填写功能
    :param gtmsp: modelspace
    :param pos1: 柱状图顶点①坐标
    :param hcoef: 水平缩放系数
    :param vcoef: 垂直缩放系数
    :param attr2: 项目基本信息字典
    :return: CAD钻孔柱状图项目基本信息
    """
    pos1 = (pos1[0] * hcoef, pos1[1] * vcoef)
    gtmsp.add_text(attr2['project_name'], dxfattribs={'insert': (pos1[0]+6.5*hcoef, pos1[1] - 1.5*vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text(attr2['project_num'], dxfattribs={'insert': (pos1[0]+6.5*hcoef, pos1[1] - 3.5*vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text(attr2['zk_zkbh'], dxfattribs={'insert': (pos1[0]+23.5*hcoef, pos1[1] - 3.5*vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text(attr2['zk_kkgc'], dxfattribs={'insert': (pos1[0]+6.5*hcoef, pos1[1] - 5.5*vcoef), 'height': 0.9 * vcoef})
    gtmsp.add_text(attr2['zk_kkzj'], dxfattribs={'insert': (pos1[0]+6.5*hcoef, pos1[1] - 7.5*vcoef), 'height': 0.9 * vcoef})
    gtmsp.add_text(attr2['zk_zbx'], dxfattribs={'insert': (pos1[0]+12.5*hcoef, pos1[1] - 5.5*vcoef), 'height': 0.9 * vcoef})
    gtmsp.add_text(attr2['zk_zby'], dxfattribs={'insert': (pos1[0]+12.5*hcoef, pos1[1] - 7.5*vcoef), 'height': 0.9 * vcoef})
    gtmsp.add_text(attr2['zk_kgrq'], dxfattribs={'insert': (pos1[0]+23.5*hcoef, pos1[1] - 5.5*vcoef), 'height': 0.8 * vcoef})
    gtmsp.add_text(attr2['zk_jgrq'], dxfattribs={'insert': (pos1[0]+23.5*hcoef, pos1[1] - 7.5*vcoef), 'height': 0.8 * vcoef})
    gtmsp.add_text(attr2['zk_wdswsd'], dxfattribs={'insert': (pos1[0]+34.5*hcoef, pos1[1] - 5.5*vcoef), 'height': 1.03 * vcoef})
    gtmsp.add_text(attr2['zk_clswrq'], dxfattribs={'insert': (pos1[0]+34.5*hcoef, pos1[1] - 7.5*vcoef), 'height': 0.9 * vcoef})


# 取样、岩芯取样率、RQD、标贯、稳定水位和水位日期
def rest_info_write(gtmsp, pos1, hcoef, vcoef, qyattr, bgattr, cylattr):
    """
    实现取样、岩芯取样率、RQD、标贯、稳定水位和水位日期样式设计功能
    :param gtmsp:modelspace
    :param pos1:柱状图顶点①坐标
    :param hcoef:水平缩放系数
    :param vcoef:垂直缩放系数
    :return:
    """
    pos1 = (pos1[0] * hcoef, pos1[1] * vcoef)
    # 添加岩性取样率
    gtmsp.add_line(start=(pos1[0]+28.6*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+28.6*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('20', dxfattribs={'insert': (pos1[0]+28.4*hcoef, pos1[1]-15.3*vcoef), 'height': 0.3 * vcoef})
    gtmsp.add_line(start=(pos1[0]+29.2*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+29.2*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('40', dxfattribs={'insert': (pos1[0] + 29 * hcoef, pos1[1] - 15.3 * vcoef), 'height': 0.3 * vcoef})
    gtmsp.add_line(start=(pos1[0]+29.8*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+29.8*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('60', dxfattribs={'insert': (pos1[0] + 29.6 * hcoef, pos1[1] - 15.3 * vcoef), 'height': 0.3 * vcoef})
    gtmsp.add_line(start=(pos1[0]+30.4*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+30.4*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('80', dxfattribs={'insert': (pos1[0] + 30.2 * hcoef, pos1[1] - 15.3 * vcoef), 'height': 0.3 * vcoef})
    # 添加RQD
    gtmsp.add_line(start=(pos1[0]+31.6*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+31.6*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('20', dxfattribs={'insert': (pos1[0]+31.4*hcoef, pos1[1]-15.3*vcoef), 'height': 0.3 * vcoef})
    gtmsp.add_line(start=(pos1[0]+32.2*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+32.2*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('40', dxfattribs={'insert': (pos1[0] + 32 * hcoef, pos1[1] - 15.3 * vcoef), 'height': 0.3 * vcoef})
    gtmsp.add_line(start=(pos1[0]+32.8*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+32.8*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('60', dxfattribs={'insert': (pos1[0] + 32.6 * hcoef, pos1[1] - 15.3 * vcoef), 'height': 0.3 * vcoef})
    gtmsp.add_line(start=(pos1[0]+33.4*hcoef, pos1[1]-16*vcoef), end=(pos1[0]+33.4*hcoef, pos1[1]-15.4*vcoef))
    gtmsp.add_text('80', dxfattribs={'insert': (pos1[0] + 33.2 * hcoef, pos1[1] - 15.3 * vcoef), 'height': 0.3 * vcoef})
    # 取样编号及深度
    # for qyi in range(len(qyattr)):
    #     gtmsp.add_text(qyattr[qyi]['qy_num'], dxfattribs={'insert': (pos1[0] + 26.3 * hcoef, pos1[1] - (16+qyattr[qyi]['qy_start']-0.2) * vcoef), 'height': 0.4 * vcoef})
    #     gtmsp.add_line(start=(pos1[0] + 25 * hcoef, pos1[1] - (16+qyattr[qyi]['qy_start']) * vcoef), end=(pos1[0] + 28 * hcoef, pos1[1] - (16+qyattr[qyi]['qy_start']) * vcoef))
    #     gtmsp.add_text(f"{'%.2f' % qyattr[qyi]['qy_start']}-{'%.2f' % qyattr[qyi]['qy_end']}", dxfattribs={'insert': (pos1[0] + 25.2 * hcoef, pos1[1] - (16 + qyattr[qyi]['qy_start'] + 0.4) * vcoef), 'height': 0.4 * vcoef})
    # 标贯击数
    # for bgi in range(len(bgattr)):
    #     gtmsp.add_text(f"={bgattr[bgi]['bg_js']}", dxfattribs={'insert': (pos1[0] + 34.3 * hcoef, pos1[1] - (16 + bgattr[bgi]['bg_jssd'] - 0.2) * vcoef), 'height': 0.4 * vcoef})
    #     gtmsp.add_line(start=(pos1[0] + 34 * hcoef, pos1[1] - (16 + bgattr[bgi]['bg_jssd']) * vcoef), end=(pos1[0] + 37 * hcoef, pos1[1] - (16 + bgattr[bgi]['bg_jssd']) * vcoef))
    #     gtmsp.add_text(f"{'%.2f' % bgattr[bgi]['bg_kssd']}-{'%.2f' % bgattr[bgi]['bg_jssd']}", dxfattribs={'insert': (pos1[0] + 34.2 * hcoef, pos1[1] - (16 + bgattr[bgi]['bg_jssd'] + 0.4) * vcoef), 'height': 0.4 * vcoef})
    # 岩芯采样率
    # cylattr.insert(0, {'sd': pos1[0] + 28 * hcoef, 'qyl': pos1[1] - 16 * vcoef})
    # cal_curv = [(pos1[0]+28*hcoef, pos1[1]-16*vcoef), (pos1[0]+(28+3*cylattr[0]['qyl']*0.01)*hcoef, pos1[1]-16*vcoef)]
    cal_curv = []
    sd_qy = 0
    for cyli in range(len(cylattr)):
        print(pos1[0])
        print(3*cylattr[cyli]['qyl'])
        print(pos1[1])
        print(cylattr[cyli]['sd'])
        cal_curv.append((pos1[0]+(28+3*cylattr[cyli]['qyl']*0.01)*hcoef, pos1[1]-(16+sd_qy)*vcoef))
        cal_curv.append((pos1[0]+(28+3*cylattr[cyli]['qyl']*0.01)*hcoef, pos1[1]-(16+cylattr[cyli]['sd'])*vcoef))
        sd_qy = cylattr[cyli]['sd']
    cal_curv.append((pos1[0]+28*hcoef, pos1[1]-(16+cylattr[-1]['sd'])*vcoef))
    gtmsp.add_lwpolyline(points=cal_curv, format='xyb', dxfattribs={'color': 1})


# 地层信息填写
def layers_info_write(gtmsp, pos1, hcoef, vcoef, attr1):
    """
    实现地层信息填写功能
    :param gtmsp:modelspace
    :param pos1:柱状图顶点①坐标
    :param hcoef:水平放大系数
    :param vcoef:垂直放大系数
    :param attr1:地层信息相关内容
    :return:钻孔柱状图地层信息
    """
    pos1 = (pos1[0] * hcoef, pos1[1] * vcoef)
    hd = 0
    hatch_hd = 0
    mtext_hd = 0
    new_mtext_hd = 0
    tuli = ['ANSI31', 'ANSI36', 'GRAVEL', 'TRIANG', 'ARHBONE', 'GOST_GROUND', 'ANSI31', 'TRIANG', 'ANSI36', 'GRAVEL']
    jishu = 0
    for attr1_i in attr1:
        gtmsp.add_text(attr1_i['order_number'], dxfattribs={
            'insert': (pos1[0] + 0.5 * hcoef, pos1[1] - (16 + attr1_i['fchd_text'] + hatch_hd-0.1) * vcoef),
            'height': 0.4 * vcoef})
        gtmsp.add_text(attr1_i['sdcy_text'], dxfattribs={
            'insert': (pos1[0] + 2.5 * hcoef, pos1[1] - (16 + attr1_i['fchd_text'] + hatch_hd-0.1) * vcoef),
            'height': 0.4 * vcoef})
        gtmsp.add_text(attr1_i['cdgc_text'], dxfattribs={
            'insert': (pos1[0] + 4.1 * hcoef, pos1[1] - (16 + attr1_i['fchd_text'] + hatch_hd-0.1) * vcoef),
            'height': 0.4 * vcoef})
        gtmsp.add_text(attr1_i['fchd_text'], dxfattribs={
            'insert': (pos1[0] + 6.5 * hcoef, pos1[1] - (16 + attr1_i['fchd_text'] + hatch_hd-0.1) * vcoef),
            'height': 0.4 * vcoef})
        gtmsp.add_text(attr1_i['cdsd_text'], dxfattribs={
            'insert': (pos1[0] + 8.5 * hcoef, pos1[1] - (16 + attr1_i['fchd_text'] + hatch_hd-0.1) * vcoef),
            'height': 0.4 * vcoef})
        gtmsp.add_line(start=(pos1[0], pos1[1] - (16 + hatch_hd + attr1_i['fchd_text']) * vcoef),
                       end=(pos1[0] + 14 * hcoef, pos1[1] - (16 + hatch_hd + attr1_i['fchd_text']) * vcoef))
        # 填充
        lwly = gtmsp.add_lwpolyline(points=((pos1[0]+10*hcoef,  pos1[1] - (16+hatch_hd) * vcoef),
                                             (pos1[0] + 14 * hcoef, pos1[1] - (16+hatch_hd) * vcoef),
                                             (pos1[0] + 14 * hcoef, pos1[1] - (16+attr1_i['fchd_text']+hatch_hd) * vcoef),
                                             (pos1[0]+10*hcoef, pos1[1] - (16+attr1_i['fchd_text']+hatch_hd) * vcoef)), format='xyb')
        zk_hatch = gtmsp.add_hatch(color=7)
        zk_hatch.set_pattern_fill(tuli[jishu+1], scale=0.05*vcoef)
        zk_path = zk_hatch.paths.add_polyline_path(lwly.get_points(format='xyb'))
        zk_hatch.associate(zk_path, [lwly])
        # 岩土名称及其特征
        tlen = len(attr1_i['describe_text'])
        wid1, heig1 = text_altitude(tlen, 9.5, 0.4, hcoef, vcoef)
        mtext_hd += heig1
        # 添加多行文本
        if jishu == 0:
            gtmsp.add_mtext(attr1_i['describe_text'], dxfattribs={'width': 8 * hcoef, 'char_height': 0.4*vcoef, 'insert': (pos1[0] + 14.8 * hcoef, pos1[1] - (16 + 0.2)*vcoef - new_mtext_hd*1.1)})
        else:
            gtmsp.add_mtext(attr1_i['describe_text'], dxfattribs={'width': 8 * hcoef, 'char_height': 0.4*vcoef, 'insert': (pos1[0] + 14.8 * hcoef, pos1[1] - (16 + 0.5)*vcoef - new_mtext_hd*1.1)})
        # 分割线
        hd += (attr1_i['fchd_text'])
        new_mtext_hd += heig1
        gtmsp.add_lwpolyline(points=((pos1[0] + 14 * hcoef, pos1[1] - (16+hd) * vcoef),
                                     (pos1[0] + 14.3 * hcoef, pos1[1] - (16 + 0.5)*vcoef - new_mtext_hd*1.1),
                                     (pos1[0] + 25 * hcoef, pos1[1] - (16 + 0.5)*vcoef - new_mtext_hd*1.1)))
        hatch_hd += attr1_i['fchd_text']
        jishu += 1


# 实现从获取数据到实现svg文件绘制功能
def data_svg_algorithm(scale, gc_datas, geo_cause, project_base_datas, layer_describs, sample_info, standard_penet_info, rock_core):
    # 图形初始定点
    pp1 = (100, 100)
    pp2 = (140, 100)
    pp3 = (140, 40)
    pp4 = (100, 40)
    # 图形比例尺设置
    zk_rate = 1000
    cf1 = scale / zk_rate
    cf2 = scale / zk_rate
    # 分层钻孔高程
    evalution = gc_datas
    # 地质年代和地质成因
    dznd = geo_cause
    # 地层序号
    lys = ('①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩')
    # 项目信息
    attrss1 = project_base_datas
    # 地层信息描述
    text_describe = layer_describs
    # 取样数据
    qy_attrss = sample_info
    # 标贯信息
    bg_attrss = standard_penet_info
    # 岩芯取样率信息
    yxqyl_attrss = rock_core
    # 地层信息
    attrss = []
    esn = 0
    for es in range(len(evalution) - 1):
        if evalution[es] - evalution[es + 1] == 0:
            esn += 0
        if evalution[es] - evalution[es + 1] != 0:
            if text_describe[es] == None:
                attrss.append({'order_number': lys[esn], 'sdcy_text': dznd[es], 'cdgc_text': round(evalution[es + 1], 2),
                               'fchd_text': round(evalution[es] - evalution[es + 1], 2),
                               'cdsd_text': round(evalution[0] - evalution[es + 1], 2),
                               'describe_text': '待描述'})
                esn += 1
            else:
                attrss.append(
                    {'order_number': lys[esn], 'sdcy_text': dznd[es], 'cdgc_text': round(evalution[es + 1], 2),
                     'fchd_text': round(evalution[es] - evalution[es + 1], 2),
                     'cdsd_text': round(evalution[0] - evalution[es + 1], 2),
                     'describe_text': text_describe[es]})
                esn += 1
    graphic_zk_frame(zk_msp, pp1, pp2, pp3, pp4, cf1, cf2)
    graphic_outside(zk_msp, pp1, pp2, pp3, pp4, cf1, cf2)
    rest_info_write(zk_msp, pp1, cf1, cf2, qy_attrss, bg_attrss, yxqyl_attrss)
    project_info_write(zk_msp, pp1, cf1, cf2, attrss1)
    text_write(zk_msp, zk_rate, pp1, pp2, pp3, pp4, cf1, cf2)
    layers_info_write(zk_msp, pp1, cf1, cf2, attrss)
    # zk_doc.saveas(r'C:\Users\andy\Desktop\zk12.dxf')
    svg_transform(zk_doc, f'E://cad2svg//1.svg')


def svg_transform(doc, export_file_path):
    """
    实现将.dxf文件保存为.svg文件功能
    :param export_file_path: .svg文件导出路径
    :return: 转换后的.svg格式文件
    """
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ctx = RenderContext(doc)
    out = MatplotlibBackend(ax)
    Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
    fig.savefig(export_file_path)