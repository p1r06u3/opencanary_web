#!/bin/sh
#Author: Weiho@破晓团队
#Blog  : www.weiho.xyz 
#Email : H4x0er@SecBug.Org 
#Github: https://github.com/zhaoweiho
#Date  : 2018-09-10
#Environment: CentOS7.2
#Gratitude: k4n5ha0/Sven/Null/c00lman/kafka
#deploy single opencanary_web_server
#
# This script is meant for quick & easy install via:
#   'curl -sSL https://raw.githubusercontent.com/zhaoweiho/opencanary_web/master/install/install.sh | sh'
# or:
#   'wget -qO- https://raw.githubusercontent.com/zhaoweiho/opencanary_web/master/install/install.sh | sh'
#


echo "###########正在初始化环境#########"
yum -y -q install net-tools
#getip=192.168.1.100
getip=`ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"`

#开启alias功能
shopt -s expand_aliases

echo "服务端IP地址:$getip"
read -p "IP是否正确(y/n):" choice
if [ $choice = n ];then
	echo "######请手动配置IP######"
	exit 0
fi

echo "#########安装依赖包############"
a=`cat /etc/redhat-release |awk '{print $4}'`
if [ "$a" \< "7.0" ];then
	echo "系统版本太低，无法使用"
	exit 0
fi

yum install -y -q ntpdate epel-release python-devel git libtool

echo "#############正在关闭SELINUX#########"
setenforce 0
selinux_on=`sed -n '7p' /etc/selinux/config | awk -F '=' '{print $2}'`
if [ "$selinux_on" = "disabled" ]; then
  echo "SELINUX=disabled"
   else
    echo "已修改SELINUX=disabled"
    sed -i "s/$selinux_on/disabled/g" /etc/selinux/config
fi

echo "##################正在更新系统时间##################"
ntpdate cn.pool.ntp.org

host_name=`export |grep HOSTNAME|awk -F '"' '{print $2}'`
export |grep HOSTNAME|grep localhost
if [ $? -eq 0 ];then
	echo "###########hostname未改动，正常#############"
else
	echo "###########正在把hostname加入/etc/hosts###############"
	sed -i "/127.0.0.1/s/$/\ $host_name/" /etc/hosts
fi

pip_file="/usr/bin/pip"
if [ ! -f "$pip_file"]; then
    echo "################pip install error############"
    else
    curl https://bootstrap.pypa.io/get-pip.py | python
    python -m pip install --upgrade pip
    echo "################pip is installed############"
fi

opencanary_web_folder="/usr/local/src/opencanary_web"
if [ ! -d "$opencanary_web_folder"]; then
    echo "############正在同步最新版本opencary_web,并且安装第三方依赖包##########"
    git clone https://github.com/p1r06u3/opencanary_web.git /usr/local/src/opencanary_web
    cd /usr/local/src/opencanary_web/
    pip install -r requirements.txt
    else
    echo "############已下载opencanary_web,正在安装第三方依赖包#########"
    cd /usr/local/src/opencanary_web/
    pip install -r requirements.txt
fi

function MYSQL() {
rpm -qa|grep mariadb-server > /dev/null
if [ $? = '1' ]; then
	echo "######install mysql########"
    yum install -y -q mariadb-server
    systemctl enable mariadb
    systemctl daemon-reload
    else
	echo "######mysql is installed########"
fi
}
MYSQL

systemctl restart mariadb
if [ $? -eq 0 ];then
        echo "######mysqld start ok#########"
else
        echo "#######mysqld start fail#############"
        exit 0
fi
#Configure mysql PassWord:Weiho@2018,Import honeypot.sql
mysql -u root -e "
SET password for 'root'@'localhost'=password('Weiho@2018');  
create database honeypot;
use honeypot;
source /usr/local/src/opencanary_web/honeypot.sql"
sed -i "s/huanchengzijidemima/Weiho@2018/g" /usr/local/src/opencanary_web/dbs/initdb.py

function NGINX() {
#rpm -qa|grep nginx > /dev/null
netstat -anput | grep nginx > /dev/null
if [ $? = '1' ]; then
	echo "######install nginx########"
	rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
    yum install -y -q nginx
else
	echo "######nginx is installed########"
fi
}
NGINX

function SUPERVISOR() {
    rpm -qa|grep supervisor > /dev/null
if [ $? = '1' ]; then
	echo "######install supervisor########"
    yum install -y -q supervisor
else
	echo "######supervisor is installed########"
fi
}
SUPERVISOR

function SUPERVISOR_CONFIGURE() {
SUPERVISOR_CONFIGURE_DOTORNADO_FILE=/etc/supervisord.d/conf.dtornado.ini
if [ ! -s $SUPERVISOR_CONFIGURE_DOTORNADO_FILE ]; then
    echo "################正在写入supervisord配置.############"
    cat > /etc/supervisord.d/conf.dtornado.ini<<EOF
[group:tornadoes]
programs=tornado-8000,tornado-8001,tornado-8002,tornado-8003

[program:tornado-8000]
command=python /usr/local/src/opencanary_web/server.py --port=8000
directory=/usr/local/src/opencanary_web
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado.log
loglevel=debug          

[program:tornado-8001]
command=python /usr/local/src/opencanary_web/server.py --port=8001
directory=/usr/local/src/opencanary_web
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado.log
loglevel=debug          

[program:tornado-8002]
command=python /usr/local/src/opencanary_web/server.py --port=8002
directory=/usr/local/src/opencanary_web
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado.log
loglevel=debug          

[program:tornado-8003]
command=python /usr/local/src/opencanary_web/server.py --port=8003
directory=/usr/local/src/opencanary_web
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado.log
loglevel=debug
EOF
    else
    echo "################supervisord配置文件已存在.############"
fi
}
SUPERVISOR_CONFIGURE
echo "################正在启动supervisord##############"
systemctl enable supervisord.service
systemctl restart supervisord.service

echo "##############正在配置Nginx###############"
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
cat > /etc/nginx/nginx.conf<<EOF
user nginx;
worker_processes 5;
error_log /var/log/nginx/error.log warn;
pid    /var/run/nginx.pid;
events {
    worker_connections 1024;
}
http {
    include    /etc/nginx/mime.types;
    default_type application/octet-stream;
    log_format main '$remote_addr - $remote_user [$time_local] "$request"'
            '$status $body_bytes_sent "$http_referer" '
            '"$http_user_agent" "$http_x_forwarded_for"';
    access_log /var/log/nginx/access.log main;
    sendfile    on;
    #tcp_nopush   on;
    keepalive_timeout 65;
    #gzip on;
    fastcgi_connect_timeout 1800;
    fastcgi_send_timeout 1800;
    fastcgi_read_timeout 1800;
    fastcgi_buffer_size 1024k;
    fastcgi_buffers 32 1024k;
    fastcgi_busy_buffers_size 2048k;
    fastcgi_temp_file_write_size 2048k;
    map \$http_upgrade \$connection_upgrade {
    default upgrade;
    ''   close;
    }
    include /etc/nginx/conf.d/*.conf;
}
EOF
cat > /etc/nginx/conf.d/hp.conf<<EOF
upstream hp {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
    server 127.0.0.1:8003;
}
server {
    listen  80;
    server_name localhost;
    proxy_connect_timeout 10d;
    proxy_read_timeout 10d;
    proxy_send_timeout 10d;
    location /static/ {
        alias   /usr/local/src/opencanary_web/dist/static/;

    }
    location / {
        proxy_pass http://hp;
        proxy_pass_header Server;
        proxy_set_header Host \$http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Scheme \$scheme;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
EOF

sed -i "s/localhost/$getip/g" /etc/nginx/conf.d/hp.conf 
echo "##############NGINX配置已完成#############"
echo "##############正在启动NGINX###############"
systemctl enable nginx.service
systemctl restart nginx.service
echo "##############重新启动NGINX完成###############"
echo "##############正在关闭防火墙#############"
systemctl stop firewalld.service
systemctl disable firewalld

#配置蜜罐告警邮件收发
echo "############ 是否配置Opencanary_Web蜜罐邮件收发,输入yes/no?Enter.默认no. ############"
typeset -l select
read select
case $select in
y*)
get_mail_host=`sed -n '30p' /usr/local/src/opencanary_web/application.py |cut -d ' ' -f1`
get_mail_user=`sed -n '31p' /usr/local/src/opencanary_web/application.py |cut -d ' ' -f1`
get_mail_pass=`sed -n '32p' /usr/local/src/opencanary_web/application.py |cut -d ' ' -f1`
get_mail_postfix=`sed -n '33p' /usr/local/src/opencanary_web/application.py |cut -d ' ' -f1`
#get_mail_addressee=`sed -n '2p' /usr/local/src/opencanary_web/util/conf/email.ini`
echo "############正在配置opencanary蜜罐邮件收发###########"
read -p "smtp服务器地址:" mail_host
if [ "$mail_host" = "" ]; then
  echo "$get_mail_host"
   else
  sed -i "s/smtp.163.com/$mail_host/g" /usr/local/src/opencanary_web/application.py
fi
read -p "邮箱用户名:" mail_user
if [ "$mail_user" = "" ]; then
  echo "$get_mail_user"
   else
  sed -i "s/qyfllyj/$mail_user/g" /usr/local/src/opencanary_web/application.py
fi
read -p "输入邮箱密码:" mail_pass
if [ "$mail_pass" = "" ]; then
  echo "$get_mail_pass"
   else
  sed -i "s/opencanary123/$mail_pass/g" /usr/local/src/opencanary_web/application.py
fi
read -p "邮箱后缀名:" mail_postfix
if [ "$mail_postfix" = "" ]; then
  echo "$get_mail_postfix"
   else
  sed -i "s/163.com/$mail_postfix/g" /usr/local/src/opencanary_web/application.py
fi
echo "############配置已完成,下一步配置收件人邮箱###########"

get_mail_addressee=`sed -n '2p' /usr/local/src/opencanary_web/util/conf/email.ini | awk '{print $3}'`
read -p "收件人邮箱:" mail_addressee
if [ "$mail_addressee" = "" ]; then
  echo "########配置没有做任何更改,默认收件人邮箱:$get_mail_addressee#######"
   else
      sed -i "s/$get_mail_addressee/$mail_addressee/g" /usr/local/src/opencanary_web/util/conf/email.ini
get_new_mail_addressee=`sed -n '2p' /usr/local/src/opencanary_web/util/conf/email.ini | awk '{print $3}'`
      echo "##########已更新告警收件邮箱:$get_new_mail_addressee#########"
fi

mail_switch=`sed -n '3p' /usr/local/src/opencanary_web/util/conf/email.ini |awk '{print $3}'`
if [ "$mail_switch" = "on" ]; then
    echo "#######已开启告警邮件开关########"
    else
    echo "#######正在开启告警邮件开关##########"
    sed -i "s/switch = off/switch = on/g" /usr/local/src/opencanary_web/util/conf/email.ini
    echo "#######开启告警邮件成功##########"
fi


echo "############告警邮件配置已完成############"
echo "############正在重启服务############"
sleep 5
#重启服务配置生效
systemctl restart supervisord.service
systemctl restart nginx.service

#回显已完成
echo "已同步cn.pool.ntp.org时间"
echo "已关闭SELINUX"
echo "已安装pip"
echo "已安装mysql,并配置Root密码Weiho@2018,可以通过mysql -u root -pWeiho@2018 进行管理"
echo "已经安装并配置supervisor"
echo "已经安装并配置nginx并把原nginx配置文件备份到/etc/nginx/nginx.conf.bak"
echo "已经关闭防火墙"
echo "已成功安装opencanary_web,文件路径:/usr/local/src/opencanary_web"
echo "可以打开http://$getip,输入账号admin密码admin进行访问操作"
echo "如要修改opencanary_web管理密码,可以通过mysql进行更改,请执行sql语句password的值换成自己的32位md5."
echo "UPDATE User SET password='900150983cd24fb0d6963f7d28e17f72' WHERE id=1;"
echo "以及修改/usr/local/src/opencanary_web/dbs/initdb.py,DB_PWD字段"
echo "已经配置成功蜜罐告警邮件,具体配置浏览/usr/local/src/opencanary_web/application.py"
echo "收件人邮件配置(以及告警开关):/usr/local/src/opencanary_web/util/conf/email.ini"
echo "更多信息请参考https://github.com/p1r06u3/opencanary_web"
;;
n*)
echo "已同步cn.pool.ntp.org时间"
echo "已关闭SELINUX"
echo "已安装pip"
echo "已安装mysql,并配置Root密码Weiho@2018,可以通过mysql -u root -pWeiho@2018 进行管理"
echo "已经安装并配置supervisor"
echo "已经安装并配置nginx并把原nginx配置文件备份到/etc/nginx/nginx.conf.bak"
echo "已经关闭防火墙"
echo "已成功安装opencanary_web,文件路径:/usr/local/src/opencanary_web"
echo "可以打开http://$getip,输入账号admin密码admin进行访问操作"
echo "如要修改opencanary_web管理密码,可以通过mysql进行更改,请执行sql语句password的值换成自己的32位md5."
echo "UPDATE User SET password='900150983cd24fb0d6963f7d28e17f72' WHERE id=1;"
echo "以及修改/usr/local/src/opencanary_web/dbs/initdb.py,DB_PWD字段"
echo "蜜罐告警邮件没有配置成功,请自行决定是否需要配置."
echo "蜜罐告警具体配置(发件人)浏览/usr/local/src/opencanary_web/application.py"
echo "收件人邮件配置(以及告警开关):/usr/local/src/opencanary_web/util/conf/email.ini"
echo "更多信息请参考https://github.com/p1r06u3/opencanary_web"
;;
*)
echo "已同步cn.pool.ntp.org时间"
echo "已关闭SELINUX"
echo "已安装pip"
echo "已安装mysql,并配置Root密码Weiho@2018,可以通过mysql -u root -pWeiho@2018 进行管理"
echo "已经安装并配置supervisor"
echo "已经安装并配置nginx并把原nginx配置文件备份到/etc/nginx/nginx.conf.bak"
echo "已经关闭防火墙"
echo "已成功安装opencanary_web,文件路径:/usr/local/src/opencanary_web"
echo "可以打开http://$getip,输入账号admin密码admin进行访问操作"
echo "如要修改opencanary_web管理密码,可以通过mysql进行更改,请执行sql语句password的值换成自己的32位md5."
echo "UPDATE User SET password='900150983cd24fb0d6963f7d28e17f72' WHERE id=1;"
echo "以及修改/usr/local/src/opencanary_web/dbs/initdb.py,DB_PWD字段"
echo "蜜罐告警邮件没有配置成功,请自行决定是否需要配置."
echo "蜜罐告警具体配置(发件人)浏览/usr/local/src/opencanary_web/application.py"
echo "收件人邮件配置(以及告警开关):/usr/local/src/opencanary_web/util/conf/email.ini"
echo "更多信息请参考https://github.com/p1r06u3/opencanary_web"
esac

