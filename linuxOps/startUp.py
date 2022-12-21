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


def createReportFile(name, text):
    """
    创建report的txt文件,并写入数据
    """
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


def appendFile(name, text):
    report_dir = os.getcwd() + os.sep + "report" + os.sep
    report_file = report_dir + name + '.txt'
    file = open(report_file, 'a')
    file.write("\n")
    file.write(text)
    file.close()


if __name__ == '__main__':
    outputFileName = time.strftime('%Y-%m-%d', time.localtime(time.time())) + "_report"
    report = list()
    report.append(linuxOps.getSystemStatus())
    report.append(linuxOps.getCpuStatus())
    report.append(linuxOps.getMemStatusSimple())
    report.append(linuxOps.getDiskStatus())
    report.append(linuxOps.getNetworkStatus())
    report.append(linuxOps.getUserStatus())
    report.append(linuxOps.getJdkStatus())
    report.append(linuxOps.getFirewallStatus())
    report.append(linuxOps.sshStatus())
    report.append(linuxOps.ntpStatus())
    report.append(linuxOps.dockerStatus())
    createReportFile(outputFileName,
                     json.dumps(report, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False))
