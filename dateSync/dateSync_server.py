# -*- coding: utf-8 -*-
"""
服务器ntpDate离线安装及配置
@Time    : 2022/10/17 9:27
@Author  : superMap.lln
@FileName: dateSync_server.py
@SoftWare: PyCharm
"""
import os


def checkTimeZone():
    """
    校验时区
    """
    timeZone1 = os.popen("date -R")
    time1 = timeZone1.readline()
    timeZone2 = os.popen("timedatectl | grep 'Time zone'")
    time2 = timeZone2.readline()
    print("INFO: check current timeZone...")
    if "Oct" in time1 or "CST" in time1 or "Oct" in time2 or "CST" in time2:
        pass
    else:
        raise Exception("ERROR:The current timeZone not Oct or Cst , please modify...")
    print("INFO: OK..")

def checkPackage():
    """
    校验本地离线包完整性
    """
    localPath = os.getcwd()
    os.chdir(localPath)
    print("INFO: check offline package...")
    lines = getCommandLines("ls | grep rpm")
    if 3 != len(lines):
        raise Exception("ERROR: offline rpm package is broken,please check...")
    for name in lines:
        if "autogen-libopts-5.18-5.el7.x86_64.rpm" == name:
            pass
        elif "ntp-4.2.6p5-28.el7.centos.x86_64.rpm" == name:
            pass
        elif "ntpdate-4.2.6p5-28.el7.centos.x86_64.rpm" == name:
            pass
        else:
            raise Exception("ERROR: offline package is broken,please check...")
    print("INFO: OK..")


def checkConfig():
    """
    检验配置文件
    """
    print("INFO: check ntp.conf...")
    for name in getCommandLines("ls | grep ntp.conf"):
        if "ntp.conf" == name:
            pass
        else:
            raise Exception("ERROR: offline package is broken, 'ntp.conf' not find , please check...")
    print("INFO: OK..")


def checkPort():
    """
    检查ntp默认端口 123 是否被占用
    """
    print("INFO: check ntp port '123' is using...")
    # os.popen(" ps -ef | grep ntp | grep -v grep | cut -c 9-15 | xargs kill -9")
    if len(os.popen("netstat -anp | grep 123 | grep ntp").readlines()) > 0:
        print("ERROR: the 123 is ntp default port and is used...")
        print("INPUT: please input [yes] to kill port 123 or exit")
        yes = "yes"
        res = input()
        if res != yes:
            raise Exception("ERROR: input error, exit...")
        else:
            os.system("ps -ef | grep ntp | grep -v grep | cut -c 9-15 | xargs kill -9")
    print("INFO: OK..")


def check():
    """
    前置校验，判断本地时区、本地脚本文件是否到指定目录，本地配置文件，端口
    """
    checkPort()
    checkTimeZone()
    checkPackage()
    checkConfig()


def delNtpRpmPackage():
    """
    删除本地ntpDate包
    """
    # 读取本地ntp包
    print("INFO: remove old date rpm package...")
    ntpNames = os.popen("rpm -qa | grep ntp")
    # ntp包前缀名称
    ntpPrefix = "npt-"
    # ntpDate包前缀名称
    ntpDatePrefix = "nptdate-"
    for line in ntpNames:
        if ntpPrefix in line or ntpDatePrefix in line:
            os.system("rpm -e --nodeps " + line)
    print("INFO: OK..")


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


def addNtpRpmPackage():
    """
    安装离线ntpDate包
    """
    # 进入当前目录
    print("INFO: install ntpDate rpm package...")
    localPath = os.getcwd()
    os.chdir(localPath)
    ntpNames = os.popen("ls")
    for name in ntpNames.readlines():
        # 安装包
        if ".rpm" in name:
            os.system("rpm -ivh " + name)
    print("INFO: OK..")


def copyNtpConfig():
    """
    拷贝配置文件
    """
    print("INFO: copy ntp.conf to /etc/ntp.conf...")
    localPath = os.getcwd()
    os.chdir(localPath)
    os.system("cp ./ntp.conf /etc/")
    print("INFO: OK...")


def startNtpServer():
    """
    启动ntp服务
    """
    # 放行端口123
    print("INFO: permit ntpd tcpPort 123...")
    os.system("iptables -I INPUT -p tcp --dport 123 -j ACCEPT")
    print("INFO: OK...")
    print("INFO: start ntpd...")
    os.system("systemctl stop ntpd")
    os.system("systemctl start ntpd")
    # 设置开机启动
    os.system("chkconfig ntpd on")
    print("INFO: OK...")


def ntpTest():
    print("TEST: ntp server status...")
    os.system("systemctl status ntpd")


if __name__ == '__main__':
    try:
        # 离线包内容检查
        check()
        # 删除已存在的包
        delNtpRpmPackage()
        # 重新添加离线包
        addNtpRpmPackage()
        # 拷贝配置文件
        copyNtpConfig()
        # 启动服务端ntp服务
        startNtpServer()
        # 测试ntp状态
        ntpTest()
    except Exception as err:
        print(err)
