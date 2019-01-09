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
#   'curl -O https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_web.sh'
#    or
#   'wget --no-check-certificate https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_web.sh'
#
#    chmod o+x install_opencanary_web.sh
#    bash install_opencanary_web.sh
#


echo "###########正在初始化环境#########"
#getip=192.168.1.100
getip=`ip add | grep -w inet | grep -v "127.0.0.1"| awk -F '[ /]+' '{print $3}'`

#开启alias功能
shopt -s expand_aliases

echo "服务端IP地址:$getip"
read -p "IP是否正确(y/n):" choice
if [ $choice = n ];then
	echo "######请手动配置IP######"
	read -p "请输入本机IP:" getip
fi

echo "#########安装依赖包############"
a=`cat /etc/redhat-release |awk '{print $4}'`
if [ "$a" \< "7.0" ];then
	echo "系统版本太低，无法使用"
	exit 0
fi
wget -O /etc/yum.repos.d/CentOS-7.repo http://mirrors.aliyun.com/repo/Centos-7.repo &> /dev/null
yum clean all
yum makecache
yum install -y -q ntpdate epel-release python-devel git 

echo "#############正在关闭SELINUX#########"
setenforce 0
selinux_on=`sed -n '7p' /etc/selinux/config | awk -F '=' '{print $2}'`
if [ "$selinux_on" = "disabled
