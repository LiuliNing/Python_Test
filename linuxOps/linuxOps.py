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
    """
    系统信息
    """
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
    res = {
        "系统": OS,
        "发行版本": Release,
        "内核": Kernel,
        "主机名": Hostname,
        "当前时间": LocalTime,
        "最后启动": LastReboot,
        "运行时间": Uptime,
        "时区信息": time_zone
    }
    return res


def getCpuStatus():
    """
    CPU信息
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
    res = {
        '物理CPU个数': physical_cpus,
        '逻辑CPU个数': virt_cpus,
        '每CPU核心数': cpu_kernels,
        'CPU型号': cpu_type,
        'CPU架构': cpu_arch
    }
    return res


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
    Proportion = '{:.4%}'.format(MemFree_Num / MemTotal_Num)
    res = {
        '总内存(GB)': '{:.5}'.format(float(MemTotal_Num / 1024 / 1024)),
        '可用内存(GB)': '{:.5}'.format(float(MemFree_Num / 1024 / 1024)),
        '已用比例(%)': Proportion
    }
    return res


def getMemStatusSimple():
    MemTotal = runCommand("free -h")
    res = {
        '内存总览': MemTotal
    }
    return res


def getDiskStatus():
    """
    磁盘检查
    """
    # 生成临时数据记录文件
    # os.popen("df -TP | sed '1d' | awk '$2!='tmpfs'{print}'")
    # os.popen("df -hTP | sed 's/Mounted on/Mounted/'> /tmp/disk")
    # 硬盘总量
    DiskAllInfo = runCommand("df -h | grep -v docker")
    DiskTotal = runCommand("df -TP | sed '1d' | awk '$2!='tmpfs'{print}'| awk '{total+=$3}END{print total}'")
    DiskTotalNum = int(DiskTotal[0])
    # 硬盘使用量
    DiskUsed = runCommand("df -TP | sed '1d' | awk '$2!='tmpfs'{print}'| awk '{total+=$4}END{print total}'")
    DiskUsedNum = int(DiskUsed[0])
    # 硬盘空余量
    DiskFree = DiskTotalNum - DiskUsedNum
    # 硬盘使用比例
    DiskUsedPercent = '{:.2%}'.format(DiskUsedNum / DiskTotalNum)
    # 索引总量
    InodeTotal = runCommand("df -iTP | sed '1d' | awk '$2!='tmpfs'{print}' | awk '{total+=$3}END{print total}' ")
    InodeTotal_Num = int(InodeTotal[0])
    # 索引使用量
    InodeUsed = runCommand("df -iTP | sed '1d' | awk '$2!='tmpfs'{print}' | awk '{total+=$4}END{print total}' ")
    InodeUsed_Num = int(InodeUsed[0])
    # 索引剩余量
    InodeFree = InodeTotal_Num - InodeUsed_Num
    # 索引使用比例
    InodePercent = '{:.2%}'.format(InodeUsed_Num / InodeTotal_Num)
    res = {
        '磁盘总览': DiskAllInfo,
        '硬盘总量(GB)': int(DiskTotalNum / 1024 / 1024),
        '硬盘使用量(GB)': int(DiskUsedNum / 1024 / 1024),
        '硬盘空余量(GB)': int(DiskFree / 1024 / 1024),
        '硬盘使用比例(%)': DiskUsedPercent,
        '索引总量(MB)': int(InodeTotal_Num / 1021),
        '索引使用量(MB)': int(InodeUsed_Num / 1021),
        '索引剩余量(MB)': int(InodeFree / 1021),
        '索引使用比例(%)': InodePercent,
    }
    return res


def getNetworkStatus():
    """
    网络检查
    """
    GATEWAY = runCommand("ip route | grep default | awk '{print $3}'")
    DNS = runCommand("grep nameserver /etc/resolv.conf| grep -v '#' | awk '{print $2}' | tr '\n' ',' | sed 's/,$//'")
    IP = runCommand(
        "ip -f inet addr | grep -v 127.0.0.1 | grep inet | awk '{print $NF,$2}' | tr '\n' ',' | sed 's/,$//'")
    # TODO 语句有问题会报错，sed的错误，需要检查下执行情况
    # MAC = runCommand("ip link | grep -v 'LOOPBACK\|loopback' | awk '{print $2}' | sed 'N;s/\n//' | tr '\n' ',' | sed 's/,$//'")
    res = {
        'GATEWAY': GATEWAY,
        'DNS': DNS,
        'IP': IP
        # 'MAC': MAC
    }
    return res


def getUserStatus():
    """
    所有用户和空密码用户
    """
    all_user = runCommand("awk -F':' '{ print $1}' /etc/passwd")
    empty_passwd_user = runCommand("getent shadow | grep -Po '^[^:]*(?=::)'")
    res = {
        '所有用户名': all_user,
        '空密码用户': empty_passwd_user
    }
    return res


def getJdkStatus():
    """
    jdk信息
    """
    jdkInfo = runCommand("java -version 2>&1")
    res = {
        'jdk信息': jdkInfo
    }
    return res


def getFirewallStatus():
    """
    防火墙
    """
    firewall = runCommand("firewall-cmd --state 2>&1")
    res = {
        '防火墙状态': firewall
    }
    return res


def sshStatus():
    sshActive = runCommand("systemctl is-active sshd.service")
    sshNetstat = runCommand("sudo netstat -atlunp | grep sshd")
    res = {
        'ssh开启状态': sshActive,
        'ssh运行情况': sshNetstat
    }
    return res


def ntpStatus():
    ntpActive = runCommand("systemctl is-active ntpd")
    res = {
        'ntp运行情况': ntpActive
    }
    return res


def dockerStatus():
    dk_version = runCommand("docker -v")
    dk_stats = []
    for info in dk_version:
        if "version" not in info:
            dk_version = "未安装docker"
        else:
            lines = os.popen(
                "docker stats --all --no-stream").readlines()
            for line in lines:
                dk_stats.append(line.replace('\n', ''))
    dp_version = runCommand("docker-compose --version")
    for info in dp_version:
        if "version" not in info:
            dp_version = "未安装docker-compose"
    res = {
        'docker version': dk_version,
        'docker-compose version': dp_version,
        'docker stats': dk_stats
    }
    return res
