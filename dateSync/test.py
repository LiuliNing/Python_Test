# coding=utf-8
# @Time: 2022/10/27 13:50
# @Author: lln
# @File: test.py
import os


def addNtpRpmPackage():
    # 进入当前目录
    localPath = os.getcwd()
    os.chdir(localPath)
    ntpNames = os.popen("ls")
    for name in ntpNames.readlines():
        # 安装包
        if ".rpm" in name:
            os.system("rpm -ivh " + name)


def copyNtpConfig():
    """
    拷贝配置文件
    """
    localPath = os.getcwd()
    os.chdir(localPath)
    os.system("cp ./ntp.conf /etc/")


def checkPort():
    """
    检查ntp默认端口 123 是否被占用
    """
    print("INFO: check ntp port '123' ...")
    if len(os.popen("netstat -anp | grep 123").readlines()) > 0:
        raise Exception("ERROR: the 123 is ntp default port and is used,please close...")
    print("INFO: OK..")


def inputTest():
    yes = "yes"
    print("INPUT: please input [yes] to kill port 123 or exit")
    res = input()
    if res != yes:
        raise Exception("ERROR: input error, exit...")
    else:
        os.system("ps -ef | grep ntp | grep -v grep | cut -c 9-15 | xargs kill -9")


def portTest():
    if len(os.popen("netstat -anp | grep 123 | grep ntp").readlines()) > 0:
        raise Exception("ERROR: the 123 is ntp default port and is used...")
    print("INFO: OK..")


def runningDateSync():
    # 获取输入的ip
    ipPath = input()
    checkIpPath(ipPath)
    print(1)


def checkIpPath(ipPath):
    ip_list = ipPath.split(".")  # 将字符串按点分割成列表
    flag = False
    for num in ip_list:
        if len(ip_list) == 4 and num.isdigit() and 0 <= int(num) <= 255:
            continue
        else:
            flag = True
            break
    if flag:
        raise Exception("ERROR: ip input error, exit... ")


if __name__ == '__main__':
    try:
        runningDateSync()
    except Exception as err:
        print(err)
