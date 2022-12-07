# -*- coding: utf-8 -*-
"""
linux 自动化脚本
# @Time: 2022/11/4 10:20
# @Author: lln
# @File: linuxOps.py.py
"""
import os


def getCommandLines(command):
    """
    执行命令，将所有读到的数据去除空行
    :param command: 命令
    :return: 去除空行后的命令
    """
    lines = os.popen(command).readlines()
    res = []
    for line in lines:
        res.append(line.replace('\n', ''))
    return res


def getTimeZone():
    """
    获取当前时区
    """
    timeZone = os.popen("date -R")
    return timeZone.readlines()


def getCpuStatus():
    """
    获取CPU信息
    """
    # 物理CPU个数
    Physical_CPUs = getCommandLines("grep 'physical id' /proc/cpuinfo| sort | uniq | wc -l")
    # 逻辑CPU个数
    Virt_CPUs = getCommandLines("grep 'processor' /proc/cpuinfo | wc -l")
    # 每CPU核心数
    CPU_Kernels = getCommandLines("grep 'cores' /proc/cpuinfo|uniq| awk -F ': ' '{print $2}'")
    # CPU型号
    CPU_Type = getCommandLines("grep 'model name' /proc/cpuinfo | awk -F ': ' '{print $2}' | sort | uniq")
    # CPU架构
    CPU_Arch = getCommandLines("uname -m")
    Res = {
        'Physical_CPUs': Physical_CPUs,
        'Virt_CPUs': Virt_CPUs,
        'CPU_Kernels': CPU_Kernels,
        'CPU_Type': CPU_Type,
        'CPU_Arch': CPU_Arch
    }
    return Res


def createReportFile(name, text):
    """
    创建report的txt文件,并写入数据
    """
    # os.getcwd() 获取当前的工作路径；
    folder = os.getcwd() + '\\report\\'
    # 判断当前路径是否存在，没有则创建new文件夹
    if not os.path.exists(folder):
        os.makedirs(folder)
    # 在当前py文件所在路径下的new文件中创建txt
    reportFile = folder + name + '.txt'
    # 打开文件，open()函数用于打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
    file = open(reportFile, 'w')
    # 写入内容信息
    file.write(text)
    file.close()
    print('文件创建成功', reportFile)


def createReportJson():
    """
    组合查询结果，构造结果JSON
    """
