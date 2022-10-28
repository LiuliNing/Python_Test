# -*- coding: utf-8 -*-
"""
服务器ntpDate离线安装及配置
@Time    : 2022/10/17 9:27
@Author  : superMap.lln
@FileName: dateSync_server.py
@SoftWare: PyCharm
"""
import os


def runningDateSync():
    print("INPUT: please input IP ...")
    ipPath = raw_input()
    checkIpPath(ipPath)
    os.system("ntpdate " + ipPath)
    print("INFO: sync " + ipPath + "date success...")


def checkIpPath(ipPath):
    ipList = ipPath.split(".")
    flag = False
    for num in ipList:
        if len(ipList) == 4 and num.isdigit() and 0 <= int(num) <= 255:
            continue
        else:
            flag = True
            break
    if flag:
        raise Exception("ERROR: ip input error, exit... ")


if __name__ == '__main__':
    try:
        # 执行同步命令
        runningDateSync()
    except Exception as err:
        print(err)
