# -*- coding: utf-8 -*-
"""
linux 自动化脚本
# @Time: 2022/11/4 10:20
# @Author: lln
# @File: linuxOps.py.py
"""
import json
import os
import time

import linuxOps

def getSystemStatus():
    """
    系统检查
    """

def getCpuStatus():
    """
    获取CPU信息
    """
    # 物理CPU个数
    Physical_CPUs = os.popen("grep 'physical id' /proc/cpuinfo| sort | uniq | wc -l")
    # 逻辑CPU个数
    Virt_CPUs = os.popen("grep 'processor /proc/cpuinfo | wc -l")
    # 每CPU核心数
    CPU_Kernels = os.popen("grep 'cores' /proc/cpuinfo|uniq| awk -F ': ' '{print $2}'")
    # CPU型号
    CPU_Type = os.popen("grep 'model name' /proc/cpuinfo | awk -F ': ' '{print $2}' | sort | uniq")
    # CPU架构
    CPU_Arch = os.popen("uname -m")


def getTimeZone():
    """
    获取当前时区
    """
    timeZone = os.popen("date -R")
    return timeZone.readlines()


def createReportFile(name, text):
    """
    创建report的txt文件,并写入数据
    """
    # os.getcwd() 获取当前的工作路径；
    report_dir = os.getcwd() + os.sep + "report" + os.sep
    # 判断当前路径是否存在，没有则创建new文件夹
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    # 在当前py文件所在路径下的new文件中创建txt
    report_file = report_dir + name + '.txt'
    # 打开文件，open()函数用于打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
    file = open(report_file, 'w')
    # 写入内容信息
    file.write(text)
    file.close()
    print('report_file create success', report_file)


if __name__ == '__main__':
    outputFileName = time.strftime('%Y-%m-%d', time.localtime(time.time())) + "_report"
    report = list()
    report.append(linuxOps.getCpuStatus())
    report.append(linuxOps.getTimeZone())
    createReportFile(outputFileName, json.dumps(report))
