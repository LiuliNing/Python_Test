# 时间同步脚本使用命令整理

### 查看本地的时间包

~~~
rpm -qa | grep ntp
~~~

~~~
eg:
ntp-4.2.6p5-28.el7.centos.x86_64
fontpackages-filesystem-1.44-8.el7.noarch
python-ntplib-0.3.2-1.el7.noarch
ntpdate-4.2.6p5-28.el7.centos.x86_64
~~~

### 卸载指定名称的包

~~~
rpm -e --nodeps ntpdate-4.2.6p5-28.el7.centos.x86_64
~~~

### 安装本地离线包

~~~
rpm -ivh autogen-libopts-5.18-5.el7.x86_64.rpm
rpm -ivh ntpdate-4.2.6p5-28.el7.centos.x86_64.rpm
rpm -ivh ntp-4.2.6p5-28.el7.centos.x86_64.rpm
~~~

### 启动

~~~
启动：systemctl start ntpd
停止：systemctl stop ntpd
状态：systemctl status ntpd
~~~

### 端口使用情况

~~~
netstat -tlunp |grep ntp
~~~

### 拉取服务端时间

~~~
查看时区
date -R
cat /etc/timezone
~~~