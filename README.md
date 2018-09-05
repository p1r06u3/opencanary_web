## web服务端介绍
tornado+supervisor+nginx+mysql

## 部署步骤

Linux服务器我选择Centos7.1，选7的原因是系统自带的python环境为2.7.x，不用麻烦着去折腾python 2.6和其他一些依赖问题。

### tornado安装

1. 安装依赖

    ```
    pip install -r requirements.txt
    ```

2. 下载web源码

    ```
    cd /usr/local/src/
    git clone https://github.com/p1r06u3/opencanary_web.git
    cd opencanary_web/
    ```

3. 安装mysql

    自行Baidu OR Google

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
    python server.py --port=8081
    ```
    若输出"Development server is running at http://0.0.0.0:8081/ "，且访问主机的ip能够显示出登录后台地址，则web单实例后台启动成功。

### 安装supervisor

1. 自行Baidu or Google，安装好后请使用我的配置。

    这里给出我的supervisor配置：

    vi /etc/supervisor/conf.d/tornado.conf

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
    service supervisord start
    ```

3. 启动多tornado实例

    ```
    supervisorctl start tornadoes:*
    ```
    关于supervisor更多的使用方法，可以搜一下；如果你修改了supervisor配置，可能需要重启supervisor服务，然后再启动实例。

4. 查看应用web是否启动成功

    ps aux|grep python

    ```
    root     30403  2.1  0.3 256192 30596 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8000
    root     30404  1.8  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8001
    root     30406  2.0  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8002
    root     30407  2.0  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8003
    ```

### 安装nginx反向代理tornado

1. 安装nginx请自行Baidu or Google.

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

## 客户端部署方法
详情见：https://github.com/p1r06u3/opencanary

## web后台的一些使用方法

### 配置告警邮件

vi /usr/local/src/opencanary_web/application.py

smtp服务器默认配置中使用的是163，改成自己的

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

### 后台可统计的攻击信息

1. ftp登录尝试；
2. http访问请求；
3. http登录请求；
4. ssh建立连接；
5. ssh远程版本发送；
6. ssh登录尝试；
7. telnet登录尝试；
8. mysql登录尝试；
9. 全端口扫描