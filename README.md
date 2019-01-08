## 一、web服务端介绍
tornado+supervisor+nginx+mysql

## 二、自动化安装
* [Linux 一条命令安装](./docs/install/Linux_AutoInstall.md)

## 三、手工安装

Linux服务器我选择Centos7.1，选7的原因是系统自带的python环境为2.7.x，不用麻烦着去折腾python 2.6和其他一些依赖问题。

首先应该关闭SELINUX:

vi /etc/selinux/config
```
SELINUX=disabled
```
然后重启服务器，使关闭SELINUX永久生效。

### tornado安装

1. 下载web源码和安装依赖

    ```
    cd /usr/local/src/
    git clone https://github.com/p1r06u3/opencanary_web.git
    cd opencanary_web/
    pip install -r requirements.txt
    ```

3. 安装mysql

    在MySQL官网中下载YUM源rpm安装包：http://dev.mysql.com/downloads/repo/yum/
    
    **下载mysql5.7源安装包**
    ```
    wget http://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm
    ```

    **安装mysql源**

    ```
    yum localinstall mysql57-community-release-el7-8.noarch.rpm
    或者
    rpm -ivh mysql57-community-release-el7-8.noarch.rpm
    ```
    **检查mysql源是否安装成功**
    ```
    yum repolist enabled|grep "mysql.*-community.*"
    ```
    **安装mysql**
    ```
    yum install mysql-server
    ```
    **启动mysql并设置开机启动**
    ```
    systemctl start mysqld
    systemctl enable mysqld
    systemctl daemon-reload
    ```
    **修改root本地登录密码**

    mysql安装完成之后，在/var/log/mysqld.log文件中给root生成了一个默认密码。

    通过下面的方式找到root默认密码，然后登录mysql进行修改：
    ```
    grep 'temporary password' /var/log/mysqld.log
    root@localhost: 后面就是默认初始密码
    M%+#bC>1l%EX
    登录mysql：mysql -u root -p
    执行修改密码语句：alter user root@localhost identified by 'Nidemima';
    identified by 后面单引号内的是你的新密码
    ```

4. 创建mysql数据库和表结构

    切换到opencanary_web目录
    ```
    cd /usr/local/src/opencanary_web
    ```

    创建数据库并还原表结构
    ```
    create database honeypot;
    use honeypot;
    source honeypot.sql;
    ```

    这时数据库中User表内默认用户名和密码为：admin\admin

    若要修改web后台登录密码请执行sql语句password的值换成自己的32位md5：
    ```
    UPDATE User SET password='900150983cd24fb0d6963f7d28e17f72' WHERE id=1;
    ```
5. 修改web数据库连接密码

    vi /usr/local/src/opencanary_web/dbs/initdb.py
    ```
    DB_PWD = 'huanchengzijidemima'
    ```
    换成自己的mysql密码

6. 单tornado实例启动测试

    ```
    python server.py --port=80
    ```
    若输出"Development server is running at http://0.0.0.0:80/ "，且访问主机的ip能够显示出登录后台地址，则web单实例后台启动成功。

### 安装配置 supervisor

>  Supervisor（ http://supervisord.org/ ）是用Python开发的一个client/server服务，是Linux/Unix系统下的一个进程管理工具，不支持Windows系统。它可以很方便的监听、启动、停止、重启一个或多个进程。用Supervisor管理的进程，当一个进程意外被杀死，supervisort监听到进程死后，会自动将它重新拉起，很方便的做到进程自动恢复的功能，不再需要自己写shell脚本来控制。

1. 安装supervisor
    ```
    yum install supervisor
    ```
2. 设置开机启动
    ```
    systemctl enable supervisord.service
    ```

3. 配置文件

    supervisord 的配置 文件是 /etc/supervisord.conf 

    自定义配置文件目录是/etc/supervisord.d/,该目录下文件以.ini为后缀

    这里给出我的supervisor子配置：

    vi /etc/supervisord.d/tornado.ini

    ```
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
    ```

2. 启动supervisor服务

    ```
    systemctl start supervisord.service
    ```
    其他常用命令
    ```
    systemctl stop supervisord.service      # 停止supervisord
    systemctl restart supervisord.service   # 重启supervisord
    ```

3. 启动多tornado实例

    ```
    supervisorctl start tornadoes:*
    ```
    
    其他更多supervisord 客户端管理命令
    ```
    supervisorctl status                    # 状态
    supervisorctl stop nginx                #关闭 nginx
    supervisorctl start nginx               #启动 nginx
    supervisorctl restart nginx             #重启 nginx
    supervisorctl reread
    supervisorctl update                    #更新新的配置
    ```

4. 查看应用web是否启动成功

    ps aux|grep python

    ```
    root     30403  2.1  0.3 256192 30596 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8000
    root     30404  1.8  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8001
    root     30406  2.0  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8002
    root     30407  2.0  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8003
    ```

### 安装nginx反向代理tornado

1. 安装nginx
    ```
    yum install nginx
    ```

2. nginx反向代理tornado配置

    nginx主配置文件：
    vi /etc/nginx/nginx.conf

    ```
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
        map $http_upgrade $connection_upgrade {
        default upgrade;
        ''   close;
        }
        include /etc/nginx/conf.d/*.conf;
    }
    ```

    nginx反向代理tornado配置:

    vi /etc/nginx/conf.d/hp.conf

    ```
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
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
    }
    ```

3. 启动或重启nginx

    已经启动了，就重启nginx；

    若没有启动，就启动nginx;

    为了使配置生效。

    ```
    systemctl start nginx.service
    systemctl restart nginx.service
    ```

4. 查看nginx是否启动成功

    ps aux|grep nginx
    ```
    root      1144  0.0  0.0  56704  1192 ?        Ss   16:45   0:00 nginx: master process /usr/sbin/nginx
    nginx     1145  0.0  0.0  61356  2176 ?        S    16:45   0:00 nginx: worker process
    nginx     1146  0.0  0.0  61356  2176 ?        S    16:45   0:00 nginx: worker process
    nginx     1147  0.0  0.0  61356  2176 ?        S    16:45   0:00 nginx: worker process
    nginx     1148  0.0  0.0  61356  2176 ?        S    16:45   0:00 nginx: worker process
    nginx     1149  0.0  0.0  61356  2176 ?        S    16:45   0:00 nginx: worker process
    root      1151  0.0  0.0 112700   968 pts/1    S+   16:45   0:00 grep --color=auto nginx
    ```

    访问主机ip的80端口，查看是否可以正常访问、正常登陆。

### 客户端部署方法
当蜜罐管理后台部署完成之后，可以重新启用一台虚拟主机部署客户端。
详情见：https://github.com/p1r06u3/opencanary

## 四、web后台的一些使用方法

### 配置告警邮件

vi /usr/local/src/opencanary_web/application.py

smtp服务器默认配置中使用的是163，改成自己的

> 注意，163的smtp的密码不是你的邮箱登录密码，而是163邮箱的客户端授权密码，需单独开启。

```
# smtp邮件服务器配置
mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="qyfllyj"                           #用户名
mail_pass="opencanary123"                             #密码
mail_postfix="163.com"                  #邮箱的后缀，网易就是163.com
```

告警邮箱写在/usr/local/src/opencanary_web/util/conf/email.ini，可通过后台进行修改告警邮箱。

但是邮箱默认开关关闭；需要开启告警邮件的，需要修改源码email.ini中的off为on。

```
[email]
user = p1r06u3@gmail.com;980555216@qq.com
switch = off
```

### 后台暂时无法删除攻击日志和添加白名单列表

如需要删除日志请登录服务器mysql，手工删除和添加。

举例:
增加白名单sql
```
use honeypot;
insert into Whiteip values('172.18.88.76');
```

如果往后攻击请求来源ip是白名单表内的ip，攻击日志将会在后台的过滤列表中出现。

### 查看web日志进行排错

```
tailf /usr/local/src/opencanary_web/logs/app.log
```

### 清空数据库表内数据

你需要先停止所有的tornado进程，然后进入数据库删数据。

### 后台可统计的攻击信息

1. ftp登录尝试；
2. http访问请求；
3. http登录请求；
4. ssh建立连接；
5. ssh远程版本发送；
6. ssh登录尝试；
7. telnet登录尝试；
8. 全端口(SYN)扫描识别;
9. NMAP OS扫描识别；
10. NMAP NULL扫描识别；
11. NMAP XMAS扫描识别；
12. NMAP FIN扫描识别；
13. mysql登录尝试；
14. git clone请求；
15. ntp monlist请求（默认关闭）；
16. redis命令请求；
17. TCP连接请求；
18. vnc连接请求；
19. windows远程登录；
20. snmp扫描；
21. sip请求；
22. mssql登录sql账户认证；
23. mssql登录win身份认证；
24. http代理登录尝试；

### 更新方法

1. 停止tornado和下载最新源码
    ```
    supervisorctl stop tornadoes:
    rm -rf opencanary_web/
    git clone https://github.com/p1r06u3/opencanary_web.git
    cd opencanary_web/
    ```
2. 修改配置文件
    
    重要的是修改数据库连接密码，修改正确：

    vi dbs/initdb.py

3. 安装依赖
    ```
    pip install -r requirements.txt
    ```
    
4. 删除旧数据库
    ```
    drop database honeypot;
    ```

5. 创建还原新数据库
    ```
    create database honeypot;
    use honeypot;
    source honeypot.sql;
    ```

6. 更改管理后台管理员密码
    ```
    UPDATE User SET password='900150983cd24fb0d6963f7d28e17f72' WHERE id=1;
    ```

7. 如需配置白名单ip
    ```
    insert into Whiteip values('192.168.1.3'),('192.168.1.8'),('192.168.1.9');
    ```
    
8. 启动实例
    ```
    supervisorctl start tornadoes:
    ```


## 致谢
@Pa5sw0rd @Weiho @冷白开 @kafka @Cotton
