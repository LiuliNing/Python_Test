## 运维自动巡检脚本使用说明

```
createTime: 2022-12-21
createBy: lln
createInfo: 
检查服务器磁盘、内存、网络、docker容器等信息，以json格式输出至同目录下的report文件夹中，便于运维人员查看。
```

### 一、环境说明

```
Centos版本 >=7
Python2版本 >=2.6 (兼容python3)
```

### 二、使用说明

```
1、将脚本文件linuxOpsStartUp.py放入任意目录下
2、执行 python linuxOpsStartUp.py 命令，进行服务器信息检查，检查结果输出至同目录下report文件夹中。
```

### 三、检查结果示例

```
[
	{
		"最后启动": [
			"15:08 "
		],
		"发行版本": [
			"CentOS Linux release 7.9.2009 (Core)"
		],
		"当前时间": [
			"2022-12-20 17:50:13"
		],
		"系统": [
			"GNU/Linux"
		],
		"时区信息": [
			"Tue, 20 Dec 2022 17:50:13 +0800"
		],
		"运行时间": [
			"2022-12-20 17:50:13"
		],
		"内核": [
			"3.10.0-1160.6.1.el7.x86_64"
		],
		"主机名": [
			"localhost.localdomain"
		]
	},
	{
		"物理CPU个数": [
			"1"
		],
		"CPU架构": [
			"x86_64"
		],
		"每CPU核心数": [
			"4"
		],
		"CPU型号": [
			"Intel(R) Core(TM) i5-6400 CPU @ 2.70GHz"
		],
		"逻辑CPU个数": [
			"4"
		]
	},
	{
		"内存总览": [
			"              total        used        free      shared  buff/cache   available",
			"Mem:            15G        9.2G        307M        783M        5.9G        5.1G",
			"Swap:          7.8G        237M        7.6G"
		]
	},
	{
		"索引总量(MB)": 1125058,
		"硬盘使用量(GB)": 1060,
		"磁盘总览": [
			"文件系统                 容量  已用  可用 已用% 挂载点",
			"devtmpfs                 7.8G     0  7.8G    0% /dev",
			"tmpfs                    7.8G     0  7.8G    0% /dev/shm",
			"tmpfs                    7.8G  732M  7.1G   10% /run",
			"tmpfs                    7.8G     0  7.8G    0% /sys/fs/cgroup",
			"/dev/mapper/centos-root   50G   31G   20G   62% /",
			"/dev/sda2               1014M  188M  827M   19% /boot",
			"/dev/sda1                200M   12M  189M    6% /boot/efi",
			"/dev/mapper/centos-home  2.0T   38G  2.0T    2% /home",
			"tmpfs                    1.6G     0  1.6G    0% /run/user/0"
		],
		"硬盘总量(GB)": 3726,
		"硬盘使用比例(%)": "28.46%",
		"索引剩余量(MB)": 1095859,
		"索引使用量(MB)": 29198,
		"硬盘空余量(GB)": 2665,
		"索引使用比例(%)": "2.60%"
	},
	{
		"IP": [
			"enp3s0 192.168.11.127/24,br-1849b047c9dd 172.19.0.1/16,docker0 172.17.0.1/16,br-7e3fcfcbbbdf 172.18.0.1/16,br-e9753d63540c 172.20.0.1/16"
		],
		"GATEWAY": [
			"192.168.11.1"
		],
		"DNS": [
			"223.5.5.5"
		]
	},
	{
		"空密码用户": [
			"test"
		],
		"所有用户名": [
			"root",
			"bin",
			"daemon",
			"ntp"
		]
	},
	{
		"jdk信息": [
			"openjdk version \"1.8.0_275\"",
			"OpenJDK Runtime Environment (build 1.8.0_275-b01)",
			"OpenJDK 64-Bit Server VM (build 25.275-b01, mixed mode)"
		]
	},
	{
		"防火墙状态": [
			"not running"
		]
	},
	{
		"ssh开启状态": [
			"active"
		],
		"ssh运行情况": [
			"tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1062/sshd           ",
			"tcp        0      0 192.168.11.127:22       192.168.11.194:50779    ESTABLISHED 10513/sshd: root@pt ",
			"tcp        0      0 192.168.11.127:22       192.168.11.194:52458    ESTABLISHED 17626/sshd: root@no ",
			"tcp6       0      0 :::22                   :::*                    LISTEN      1062/sshd           "
		]
	},
	{
		"ntp运行情况": [
			"active"
		]
	},
	{
		"docker-compose version": [
			"docker-compose version 1.29.2, build unknown"
		],
		"docker version": [
			"Docker version 20.10.0, build 7287ab3"
		],
		"docket stats": [
			"CONTAINER ID   NAME                                       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS",
			"d36c48b5c621   sinfcloud-rabbitmq                         1.31%     122.7MiB / 15.47GiB   0.77%     3.78GB / 4.09GB   63.2MB / 2.58MB   29",
			"40db1a93ec2d   linux-command                              0.00%     144KiB / 15.47GiB     0.00%     62.1kB / 1.3MB    1.44MB / 0B       1"
		]
	}
]
```



