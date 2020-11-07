#!/bin/sh
#Author: Weiho@破晓团队
#Blog  : www.weiho.xyz 
#Email : H4x0er@SecBug.Org 
#Github: https://github.com/zhaoweiho
#Date  : 2018-12-25
#Environment: CentOS7.2
#Gratitude: k4n5ha0/p1r06u3/Sven/Null/c00lman/kafka/JK
#deploy single opencanary_web_server
#
# This script is meant for quick & easy install via:
#   'curl -O https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_agent.sh'
#    or
#   'wget --no-check-certificate https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_agent.sh'
#
#    chmod o+x install_opcanary_agent.sh
#    bash install_opcanary_agent.sh
#
#
#ip=192.168.1.100
#ip=`ip add | grep -w inet | grep -v "127.0.0.1"| awk -F '[ /]+' '{print $3}'`
netcard_num=`ls /sys/class/net/ | grep -v lo | wc -l`


echo "###############请确认已经安装Web服务端##############"
read -p "请确认是否已经安装OpenCanary_Web服务端(y/n)" choice
if [ $choice = n ];then
	echo "######请安装完服务端后再配置agent######"
	exit 0
fi
if [ $netcard_num -lt 2 ];then
    ip=`ip add | grep -w inet | grep -v "127.0.0.1"| awk -F '[ /]+' '{print $3}'`
    else
    #ls /sys/class/net/ | grep -v lo | awk '{print $1}' > /tmp/netcard_ip.txt
    ip add | grep -w inet | grep -v "127.0.0.1"| awk -F '[ /]+' '{print $3}' > /tmp/netcard_ip.txt
    ip1=`sed -n '1p' /tmp/netcard_ip.txt`
    ip2=`sed -n '2p' /tmp/netcard_ip.txt`
    echo "
    请选择本机IP?(1-3) 
    1.$ip1  
    2.$ip2 
    3.其他
    "
    read -p "请输入指令(1-3):" ip
    n2=`echo $ip | sed 's/[0-9]//g'`
        if [ -n "$n2" ];then
         echo "The input content is not a number."
         exit
        fi
        case $ip in
        1)
         echo "本机IP地址:$ip1"
         ip=$ip1
        ;;
        2)
        echo "本机IP地址:$ip2"
        ip=$ip2
        ;;
        3)
    	echo "######请手工设置本机IP地址######"
        read -p "请输入本机IP:" ip
        ;;
        *)
        echo "请输入数字:1-3"  
        ;;
        esac
fi

read -p "请确认本机IP:$ip是否正确?(y/n)" ipd
if [ $ipd = n ];then
	echo "######请手工设置本机IP地址######"
    read -p "请输入本机IP:" ip
fi


read -p "请输入Web服务端IP:" opencanary_web_server_ip
read -p "请输入本机节点名称:" opencanary_agent_name
echo "###################################"
echo Web服务端IP:$opencanary_web_server_ip
echo 本机IP地址:$ip
echo 本机节点名称:$opencanary_agent_name

echo "###########正在安装系统依赖#########"
a=`cat /etc/redhat-release | grep -oP '[[:digit:]]\S*'`
if [ "$a" \< "7.0" ];then
    wget -O /etc/yum.repos.d/CentOS-6.repo http://mirrors.aliyun.com/repo/Centos-6.repo &> /dev/null
    yum clean all
    yum makecache
else
    wget -O /etc/yum.repos.d/CentOS-7.repo http://mirrors.aliyun.com/repo/Centos-7.repo &> /dev/null
    yum clean all
    yum makecache
fi
yum -y -q install epel-release
yum -y -q install libpcap-devel openssl-devel libffi-devel python-devel gcc python-pip gcc-c++ ntpdate git iptables-services

echo "##################正在更新系统时间##################"
ntpdate cn.pool.ntp.org

echo "###########正在下载opencanary_agent#########"
opencanary_folder="/usr/local/src/opencanary"
if [ ! -d $opencanary_folder ]; then
    git clone https://github.com/p1r06u3/opencanary.git /usr/local/src/opencanary
	configure_agent_name=`sed -n "2p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
    configure_server_ip=`sed -n "3p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
	configure_ip=`sed -n "4p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
	sed -i "s/$configure_agent_name/$opencanary_agent_name/g" /usr/local/src/opencanary/opencanary/data/settings.json
    sed -i "s/$configure_server_ip/$opencanary_web_server_ip/g" /usr/local/src/opencanary/opencanary/data/settings.json
	sed -i "s/$configure_ip/$ip/g" /usr/local/src/opencanary/opencanary/data/settings.json
    else
	configure_agent_name=`sed -n "2p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
    configure_server_ip=`sed -n "3p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
	configure_ip=`sed -n "4p"  /usr/local/src/opencanary/opencanary/data/settings.json | awk -F '["]+' '{print $4}'`
	sed -i "s/$configure_agent_name/$opencanary_agent_name/g" /usr/local/src/opencanary/opencanary/data/settings.json
    sed -i "s/$configure_server_ip/$opencanary_web_server_ip/g" /usr/local/src/opencanary/opencanary/data/settings.json
	sed -i "s/$configure_ip/$ip/g" /usr/local/src/opencanary/opencanary/data/settings.json
fi

echo "###########正在安装opencanary_agent#########"
    cd /usr/local/src/opencanary/
    python setup.py sdist
    cd /usr/local/src/opencanary/dist
    pip install opencanary-0.4.tar.gz


a=`cat /etc/redhat-release |awk '{print $4}'`
if [ "$a" \< "7.0" ];then
    echo "#############配置并启动rsyslog#############"
    sed -i '50i kern.*                                              /var/log/kern.log' /etc/rsyslog.conf
    /etc/init.d/rsyslog restart
    chkconfig --level 2345 rsyslog on
    else
    echo "#############配置并启动rsyslog#############"
    sed -i '50i kern.*                                              /var/log/kern.log' /etc/rsyslog.conf
    systemctl restart rsyslog.service
    systemctl enable rsyslog.service
fi

if [ "$a" \< "7.0" ];then
    echo "##############正在关闭iptables防火墙#############"
    /etc/init.d/iptables stop
    chkconfig iptables off
    else 
    echo "##############正在关闭firewalld防火墙#############"
    systemctl stop firewalld.service
    systemctl disable firewalld.service
fi


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
