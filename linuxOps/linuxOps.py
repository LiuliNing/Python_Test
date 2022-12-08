# -*- coding: utf-8 -*-
"""
linux 自动化脚本
# @Time: 2022/11/4 10:20
# @Author: lln
# @File: linuxOps.py
"""
import os


def runCommand(command):
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


def getSystemStatus():
    # 系统
    OS = runCommand("uname -o")
    # 发行版本
    Release = runCommand("cat /etc/redhat-release 2>/dev/null")
    # 内核
    Kernel = runCommand("uname -r")
    # 主机名
    Hostname = runCommand("uname -n")
    # 当前时间
    LocalTime = runCommand("date +'%F %T'")
    # 最后启动
    LastReboot = runCommand("who -b | awk '{print $3,$4}'")
    # 运行时间
    Uptime = runCommand("date +'%F %T'")
    # 当前时区信息
    time_zone = runCommand("date -R")
    Res = {
        "系统": OS,
        "发行版本": Release,
        "内核": Kernel,
        "主机名": Hostname,
        "当前时间": LocalTime,
        "最后启动": LastReboot,
        "运行时间": Uptime,
        "时区信息": time_zone
    }
    return Res


def getCpuStatus():
    """
    获取CPU信息
    """
    # 物理CPU个数
    physical_cpus = runCommand("grep 'physical id' /proc/cpuinfo| sort | uniq | wc -l")
    # 逻辑CPU个数
    virt_cpus = runCommand("grep 'processor' /proc/cpuinfo | wc -l")
    # 每CPU核心数
    cpu_kernels = runCommand("grep 'cores' /proc/cpuinfo|uniq| awk -F ': ' '{print $2}'")
    # CPU型号
    cpu_type = runCommand("grep 'model name' /proc/cpuinfo | awk -F ': ' '{print $2}' | sort | uniq")
    # CPU架构
    cpu_arch = runCommand("uname -m")
    Res = {
        '物理CPU个数': physical_cpus,
        '逻辑CPU个数': virt_cpus,
        '每CPU核心数': cpu_kernels,
        'CPU型号': cpu_type,
        'CPU架构': cpu_arch
    }
    return Res


def getMemStatus():
    """
    内存信息
    """
    # 总内存
    MemTotal = runCommand("grep MemTotal /proc/meminfo| awk '{print $2}'")
    MemTotal_Num = map(float, MemTotal)[0]
    # 可用内存
    MemFree = runCommand("grep MemFree /proc/meminfo| awk '{print $2}'")
    MemFree_Num = map(float, MemFree)[0]
    # 比例
    Proportion = '{:.2%}'.format(MemFree_Num / MemTotal_Num)
    Res = {
        '总内存(MB)': int(MemTotal_Num / 1024),
        '可用内存(MB)': int(MemFree_Num / 1024),
        '已用比例(%)': Proportion
    }
    return Res


def getDiskStatus():
    """
    磁盘检查
    """
    # 生成临时数据记录文件
    # os.popen("df -TP | sed '1d' | awk '$2!='tmpfs'{print}'")
    # os.popen("df -hTP | sed 's/Mounted on/Mounted/'> /tmp/disk")
    # 硬盘总量
    DiskTotal = runCommand("df -TP | sed '1d' | awk '$2!='tmpfs'{print}'| awk '{total+=$3}END{print total}'")
    DiskTotalNum = map(float, DiskTotal)[0]
    # 硬盘使用量
    DiskUsed = runCommand("df -TP | sed '1d' | awk '$2!='tmpfs'{print}'| awk '{total+=$4}END{print total}'")
    DiskUsedNum = map(float, DiskUsed)[0]
    # 硬盘空余量
    DiskFree = DiskTotalNum - DiskUsedNum
    # 硬盘使用比例
    DiskUsedPercent = '{:.2%}'.format(DiskUsedNum / DiskTotalNum)
    # 索引总量
    InodeTotal = runCommand("df -iTP | sed '1d' | awk '$2!='tmpfs'{print}' | awk '{total+=$3}END{print total}' ")
    InodeTotal_Num = map(float, InodeTotal)[0]
    # 索引使用量
    InodeUsed = runCommand("df -iTP | sed '1d' | awk '$2!='tmpfs'{print}' | awk '{total+=$4}END{print total}' ")
    InodeUsed_Num = map(float, InodeUsed)[0]
    # 索引剩余量
    InodeFree = InodeTotal_Num - InodeUsed_Num
    # 索引使用比例
    InodePercent = '{:.2%}'.format(InodeUsed_Num / InodeTotal_Num)
    Res = {
        '硬盘总量(GB)': int(DiskTotalNum / 1024 / 1024),
        '硬盘使用量(GB)': int(DiskUsedNum / 1024 / 1024),
        '硬盘空余量(GB)': int(DiskFree / 1024 / 1024),
        '硬盘使用比例(%)': DiskUsedPercent,
        '索引总量(MB)': int(InodeTotal_Num / 1021),
        '索引使用量(MB)': int(InodeUsed_Num / 1021),
        '索引剩余量(MB)': int(InodeFree / 1021),
        '索引使用比例(%)': InodePercent,
    }
    return Res
