# -*- coding: utf-8 -*-
""" 
@Time    : 2021/10/12 19:47
@Author  : 梅迁
@FileName: coor_zhuanhuan.py
@SoftWare: PyCharm
"""
import pandas as pd
import math
import json


# json数据转python
def json_t_py(data2):
    """
     将接收到的json数据转换为python数据
    :param data2: 传入的json数据
    :return: 转换后可以使用的python数据
    """
    df1 = pd.DataFrame(columns=['pointId', 'lat', 'lon', 'pointX', 'pointY'])
    df2 = pd.DataFrame(columns=['pointId', 'lat', 'lon', 'pointX', 'pointY'])
    js_py_list = data2
    try:
        dmks = js_py_list[0]['dmarks']
        pits = js_py_list[0]['points']
    except TypeError:
        print('Wrong data type')
    else:
        try:
            for j in range(len(dmks)):
                df1.loc[j, 'pointId'] = dmks[j]['pointId']
                df1.loc[j, 'lat'] = float(dmks[j]['lat'])
                df1.loc[j, 'lon'] = float(dmks[j]['lon'])
                df1.loc[j, 'pointX'] = float(dmks[j]['pointX'])
                df1.loc[j, 'pointY'] = float(dmks[j]['pointY'])
            for k in range(len(pits)):
                df2.loc[k, 'pointId'] = pits[k]['pointId']
                df2.loc[k, 'lat'] = pits[k]['lat']
                df2.loc[k, 'lon'] = pits[k]['lon']
                df2.loc[k, 'pointX'] = float(pits[k]['pointX'])
                df2.loc[k, 'pointY'] = float(pits[k]['pointY'])
        except KeyError:
            print('Key error')
        else:
            return df1, df2


# python转json
def py_to_js(df1, df2):
    """
    将python格式数据转换为json数据
    :param df1: 需要进行坐标转换计算的python数据
    :param df2: 基准点数据
    :return: 转换后的json格式数据
    """
    try:
        list1, list2 = [], []
        for i in range(len(df1)):
            dict1 = {'pointId': str(df1.loc[i, 'pointId']),
                     'lat': str(df1.loc[i, 'lat']),
                     'lon': str(df1.loc[i, 'lon']),
                     'pointX': str(df1.loc[i, 'pointX']),
                     'pointY': str(df1.loc[i, 'pointY'])}
            dict11 = json.dumps(dict1)
            list1.append(eval(dict11))
        for j in range(len(df2)):
            dict2 = {'pointId': str(df2.loc[j, 'pointId']),
                     'lat': str(df2.loc[j, 'lat']),
                     'lon': str(df2.loc[j, 'lon']),
                     'pointX': str(df2.loc[j, 'pointX']),
                     'pointY': str(df2.loc[j, 'pointY'])}
            dict22 = json.dumps(dict2)
            list2.append(eval(dict22))
    except KeyError:
        print('Key error')
    else:
        dicts = {"dmarks": list2, "points": list1}
        new_dicts = eval(json.dumps(dicts))
        return new_dicts


# 图像基准点移动到原点
def coordinate_move(datadf1, h_move_value, v_move_value, flag, num):
    """
    坐标移动
    :param datadf1: 需要移动的坐标数据
    :param X_move_value: 水平向移动距离
    :param Y_move_value: 垂直向移动距离
    :param flag: 区分数据来源，1：需要计算的坐标数据集， 2：基准点数据集
    :param num: 基准点个数
    :return: 移动后的坐标结果
    """
    try:
        if flag == 1:
            for i in range(len(datadf1)):
                datadf1.loc[i, 'pointX_move'] = float(datadf1.loc[i, 'pointX']) - float(h_move_value)
                datadf1.loc[i, 'pointY_move'] = float(datadf1.loc[i, 'pointY']) - float(v_move_value)
        if flag == 2:
            for i in range(len(datadf1) - num, len(datadf1)):
                datadf1.loc[i, 'lon_move'] = float(datadf1.loc[i, 'lon']) - float(h_move_value)
                datadf1.loc[i, 'lat_move'] = float(datadf1.loc[i, 'lat']) - float(v_move_value)
    except AttributeError:
        print('Attribute error')
    return datadf1


# 数据缩放
def coordinate_scale(datadf2, scale_value):
    """
    对数据进行缩放
    :param datadf2: 需要进行缩放的数据
    :param scale_value: 缩放的比例
    :return: 缩放后的数据
    """
    try:
        for i in range(len(datadf2)):
            datadf2.loc[i, 'pointX_scale'] = datadf2.loc[i, 'pointX_move'] * scale_value
            datadf2.loc[i, 'pointY_scale'] = datadf2.loc[i, 'pointY_move'] * scale_value
    except TypeError:
        print('Type error')
    else:
        return datadf2


# 旋转角度计算
def cal_included(Xbpoint, Ybpoint):
    """
    计算第一二个基准点旋转到水平轴上的旋转角度
    :param Xbpoint: 第二个基准点的横坐标
    :param Ybpoint: 第二个基准点的纵坐标
    :return: 旋转过的度数（弧度数）
    """
    try:
        k_value = abs(Ybpoint / Xbpoint)
        if Xbpoint >= 0 and Ybpoint >= 0:
            thetas = 2 * math.pi - math.atan(k_value)
        elif Xbpoint < 0 and Ybpoint >= 0:
            thetas = math.pi + math.atan(k_value)
        elif Xbpoint < 0 and Ybpoint < 0:
            thetas = math.pi - math.atan(k_value)
        else:
            thetas = math.atan(k_value)
    except TypeError:
        print('Type error')
    else:
        return thetas


# 坐标旋转
def coordinate_rotate(datadf3, rotate_angle, flag):
    """
    坐标旋转计算
    :param datadf3: 需要进行旋转计算的坐标数据
    :param rotate_angle: 坐标旋转转角度(弧度数)
    :param flag: 区分数据来源，1：需要计算的坐标数据集， 2：基准点数据集
    :return: 经过旋转后的坐标数据
    """
    try:
        if flag == 1:
            for i in range(len(datadf3)):
                datadf3.loc[i, 'pointX_rotate'] = datadf3.loc[i, 'pointX_scale'] * math.cos(rotate_angle) - datadf3.loc[
                    i, 'pointY_scale'] * math.sin(rotate_angle)
                datadf3.loc[i, 'pointY_rotate'] = datadf3.loc[i, 'pointX_scale'] * math.sin(rotate_angle) + datadf3.loc[
                    i, 'pointY_scale'] * math.cos(rotate_angle)
        if flag == 2:
            for i in range(len(datadf3)):
                datadf3.loc[i, 'lon_rotate'] = datadf3.loc[i, 'lon_move'] * math.cos(rotate_angle) - datadf3.loc[
                    i, 'lat_move'] * math.sin(rotate_angle)
                datadf3.loc[i, 'lat_rotate'] = datadf3.loc[i, 'lon_move'] * math.sin(rotate_angle) + datadf3.loc[
                    i, 'lat_move'] * math.cos(rotate_angle)
        if flag == 3:
            for i in range(len(datadf3)):
                datadf3.loc[i, 'pointX_jz3'] = datadf3.loc[i, 'pointX_correcte_three'] * math.cos(rotate_angle) + \
                                               datadf3.loc[i, 'pointY_correcte_three'] * math.sin(rotate_angle)
                datadf3.loc[i, 'pointY_jz3'] = datadf3.loc[i, 'pointY_correcte_three'] * math.cos(rotate_angle) - \
                                               datadf3.loc[i, 'pointX_correcte_three'] * math.sin(rotate_angle)
    except AttributeError:
        print('Attribute error')
    else:
        return datadf3


# 坐标绕横轴翻转
def coordinate_turn(datadf4):
    """
    进行坐标数据翻转
    :param datadf4: 需要进行翻转的坐标数据
    :return: 翻转后的坐标数据
    """
    try:
        for i in range(len(datadf4)):
            datadf4.loc[i, 'pointX_turn'] = datadf4.loc[i, 'pointX_rotate']
            datadf4.loc[i, 'pointY_turn'] = -datadf4.loc[i, 'pointY_rotate']
    except KeyError:
        print('Key value error')
    else:
        return datadf4


# 第二个基准点校正
def two_coordinate_correcte(datadf5, two_correcte_value):
    """
    进行图像基准点校正
    :param datadf5: 需要进行基准点校正的数据
    :param two_correcte_value: 坐标数据缩放比例
    :return: 基准点校正后的坐标数据
    """
    try:
        for i in range(len(datadf5)):
            datadf5.loc[i, 'pointX_correcte_two'] = datadf5.loc[i, 'pointX_turn'] * two_correcte_value
            datadf5.loc[i, 'pointY_correcte_two'] = datadf5.loc[i, 'pointY_turn'] * two_correcte_value
    except KeyError:
        print('Key value error')
    else:
        return datadf5


# 第三个基准点校正
def three_coordinate_correcte(datadf6, three_correcte_value):
    """
    第三个基准点校正
    :param datadf6: 需要进行校正的坐标数据
    :param three_correcte_value: 校正缩放比例
    :return: 校正后的坐标数据
    """
    try:
        for i in range(len(datadf6)):
            datadf6.loc[i, 'pointX_correcte_three'] = datadf6.loc[i, 'pointX_correcte_two']
            datadf6.loc[i, 'pointY_correcte_three'] = datadf6.loc[i, 'pointY_correcte_two'] * three_correcte_value
    except KeyError:
        print('Key value error')
    else:
        return datadf6


# 计算两点之间的距离
def cal_distance(point1, point2):
    """
    计算两点之间的距离
    :param point1: 第一个点的坐标值（列表形式）
    :param point2: 第二个点的坐标值（列表形式）
    :return: 两点之间的距离值
    """
    try:
        distance_value = math.sqrt((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2)
    except ValueError:
        print('Value error')
    else:
        return distance_value


# 计算出坐标变化后的结果，并输出为json格式数据
def transform_algorithm(js_datas):
    """
    进行坐标转换计算，并将计算结果转换为json格式数据
    :param js_datas: json格式数据，包括基准点与需要进行坐标转换的坐标值
    :return:
    """
    # 得到两组数据
    dmarks_df, points_df = json_t_py([js_datas])
    jz_point_num = len(dmarks_df)
    points_df = pd.concat([points_df, dmarks_df], axis=0)
    points_df.reset_index(drop=True, inplace=True)
    # 平移
    lenth1 = len(points_df) - jz_point_num
    xmove = float(points_df.loc[lenth1, 'pointX'])
    ymove = float(points_df.loc[lenth1, 'pointY'])
    jmove = float(dmarks_df.loc[0, 'lon'])
    wmove = float(dmarks_df.loc[0, 'lat'])
    # 平移后坐标
    df1 = coordinate_move(points_df, xmove, ymove, 1, jz_point_num)
    df2 = coordinate_move(dmarks_df, jmove, wmove, 2, jz_point_num)
    # 整体缩放
    pointA = [df1.loc[len(df1) - jz_point_num, 'pointX_move'], df1.loc[len(df1) - jz_point_num, 'pointY_move']]
    pointB = [df1.loc[len(df1) - jz_point_num + 1, 'pointX_move'], df1.loc[len(df1) - jz_point_num + 1, 'pointY_move']]
    pointC = [df2.loc[0, 'lon_move'], df2.loc[0, 'lat_move']]
    pointD = [df2.loc[1, 'lon_move'], df2.loc[1, 'lat_move']]
    xydistance = cal_distance(pointA, pointB)
    jwdistance = cal_distance(pointC, pointD)
    rate1 = jwdistance / xydistance
    sf_df = coordinate_scale(df1, rate1)
    Xb = sf_df.loc[len(sf_df) - jz_point_num + 1, 'pointX_scale']
    Yb = sf_df.loc[len(sf_df) - jz_point_num + 1, 'pointY_scale']
    theta1 = cal_included(Xb, Yb)
    Jb = df2.loc[1, 'lon_move']
    Wb = df2.loc[1, 'lat_move']
    theta2 = cal_included(Jb, Wb)
    xz_df_xy = coordinate_rotate(sf_df, theta1, 1)
    xz_df_jw = coordinate_rotate(df2, theta2, 2)
    # 翻转操作
    result1 = xz_df_xy.loc[len(xz_df_xy) - jz_point_num + 2, 'pointY_rotate']
    result2 = xz_df_jw.loc[2, 'lat_rotate']
    result3 = result1 * result2
    if result3 < 0:
        fz_df = coordinate_turn(xz_df_xy)
    else:
        xz_df_xy.loc[:, 'pointX_turn'] = xz_df_xy.loc[:, 'pointX_rotate']
        xz_df_xy.loc[:, 'pointY_turn'] = xz_df_xy.loc[:, 'pointY_rotate']
        fz_df = xz_df_xy
    # 第二个基准点校正
    turnx = fz_df.loc[len(fz_df) - jz_point_num + 1, 'pointX_turn']
    rate2 = xz_df_jw.loc[1, 'lon_rotate'] / turnx
    jz2_df = two_coordinate_correcte(fz_df, rate2)
    # 第三点校正
    turny = jz2_df.loc[len(jz2_df) - jz_point_num + 2, 'pointY_correcte_two']
    rate3 = xz_df_jw.loc[2, 'lat_rotate'] / turny
    jz3_df = three_coordinate_correcte(jz2_df, rate3)
    theta3 = cal_included(df2.loc[1, 'lon_move'], df2.loc[1, 'lat_move'])
    hy_df = coordinate_rotate(jz3_df, theta3, 3)
    for i in range(len(hy_df) - jz_point_num):
        hy_df.loc[i, 'pointX_jz3'] = hy_df.loc[i, 'pointX_jz3'] + hy_df.loc[len(hy_df) - jz_point_num, 'lon']
        hy_df.loc[i, 'pointY_jz3'] = hy_df.loc[i, 'pointY_jz3'] + hy_df.loc[len(hy_df) - jz_point_num, 'lat']
    new_hy_df = hy_df[['pointId', 'pointX_jz3', 'pointY_jz3', 'pointX', 'pointY']]
    new_hy_df1 = pd.DataFrame(columns=['pointId', 'lat', 'lon', 'pointX', 'pointY'])
    new_hy_df1['pointId'] = new_hy_df['pointId']
    new_hy_df1['lon'] = new_hy_df['pointX_jz3']
    new_hy_df1['lat'] = new_hy_df['pointY_jz3']
    new_hy_df1['pointX'] = new_hy_df['pointX']
    new_hy_df1['pointY'] = new_hy_df['pointY']
    L = len(new_hy_df1)
    new_hy_df2 = new_hy_df1[0:L - jz_point_num]
    list_new = []
    for m in range(len(new_hy_df2)):
        list_new.append(new_hy_df2.iloc[m, :].tolist())
    s1 = []
    for i in range(len(list_new)):
        r1 = dict([['pointId', list_new[i][0]], ['lat', list_new[i][1]], ['lon', list_new[i][2]], ['pointX', list_new[i][3]],['pointY', list_new[i][4]]])
        s1.append(r1)
    result1 = json.dumps(s1)
    return result1


