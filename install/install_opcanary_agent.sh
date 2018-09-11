#!/bin/sh
#Author: Weiho@破晓团队
#Blog  : www.weiho.xyz 
#Email : H4x0er@SecBug.Org 
#Github: https://github.com/zhaoweiho
#Date  : 2018-09-11
#Environment: CentOS7.2
#Gratitude: k4n5ha0/p1r06u3/Sven/Null/c00lman/kafka/JK
#deploy single opencanary_web_server
#
# This script is meant for quick & easy install via:
#   'curl -O https://raw.githubusercontent.com/zhaoweiho/opencanary_web/master/install/install_opcanary_agent.sh'
#    or
#   'wget --no-check-certificate https://raw.githubusercontent.com/zhaoweiho/opencanary_web/master/install/install_opcanary_agent.sh'
#
#    chmod o+x install_opcanary_agent.sh
#    ./install_opcanary_agent.sh
#

echo "###############请确认已经安装Web服务端##############"
read -p "请确认是否已经安装OpenCanary_Web服务端(y/n)" choice
if [ $choice = n ];then
	echo "######请安装完服务端后再配置agent######"
	exit 0
fi
read -p "请输入Web服务端IP:" opencanary_web_server_ip
echo $opencanary_web_server_ip

echo "###########正在安装系统依赖#########"
yum -y -q install epel-release
yum -y -q install libpcap-devel openssl-devel libffi-devel python-devel gcc python-pip gcc-c++ ntpdate git iptables-services

PIP_FILE=/usr/bin/pip
if [ ! -s $PIP_FILE ]; then
    curl https://bootstrap.pypa.io/get-pip.py | python
    python -m pip install --upgrade pip
    echo "################pip is installed############"
    else
    echo "################pip install error############"
fi

echo "##################正在更新系统时间##################"
ntpdate cn.pool.ntp.org

echo "###########正在下载opencanary_agent#########"
opencanary_folder="/usr/local/src/opencanary"
if [ ! -d $opencanary_folder ]; then
    git clone https://github.com/p1r06u3/opencanary.git /usr/local/src/opencanary
    configure_server_ip=`sed -n "69p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
    sed -i "s/$configure_server_ip/$opencanary_web_server_ip/g" /usr/local/src/opencanary/opencanary/data/settings.json
    else
    configure_server_ip=`sed -n "69p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
    sed -i "s/$configure_server_ip/$opencanary_web_server_ip/g" /usr/local/src/opencanary/opencanary/data/settings.json
fi

echo "###########正在安装opencanary_agent#########"
opencanary_sdist_folder="/usr/local/src/opencanary/sdist"
if [ ! -d $opencanary_folder ]; then
    cd /usr/local/src/opencanary/
    python setup.py sdist
    cd /usr/local/src/opencanary/dist
    pip install opencanary-0.3.2.tar.gz
    else
    cd /usr/local/src/opencanary/dist
    pip install opencanary-0.3.2.tar.gz
fi

echo "#############配置并启动rsyslog#############"
sed -i '50i kern.*                                              /var/log/kern.log' /etc/rsyslog.conf
systemctl restart rsyslog.service

echo "##############正在关闭firewalld防火墙#############"
systemctl stop firewalld.service
systemctl disable firewalld.service

OPENCANARY_CONF_FILE=/root/.opencanary.conf
if [ ! -s $OPENCANARY_CONF_FILE ]; then
    opencanaryd --copyconfig
    opencanaryd --start
    echo "################第一次运行,初始化opencanaryd############"
    echo "################已安装完成opencanaryd_agent############"
    else
    echo "################已运行过opencanaryd############"
    echo "################正在重启opencanaryd############"
    opencanaryd --stop
    opencanaryd --start
fi
echo "安装opencanary_agent成功.opencanary支持以下协议"
echo "ftp登录尝试/http访问请求/http登录请求/ssh建立连接"
echo "ssh远程版本发送/ssh登录尝试/telnet登录尝试/mysql登录尝试"
echo "建议使用iptables对相关端口进行管理,详细请参考https://github.com/p1r06u3/opencanary_web"
echo "请登陆至http://$opencanary_web_server_ip 进行管理."
