## web服务端介绍

tornado+supervisor+nginx+mysql

## 部署步骤
Linux服务器我选择Centos7.1，选7的原因是系统自带的python环境为2.7.x，不用麻烦着去折腾升级python 2.6和其他一些依赖问题。

### tornado安装

1. 安装依赖

```
pip install tornado
pip install PyJWT
pip install python-jwt
pip install sqlalchemy
pip install pymysql
pip install configparser
```

2. 下载web源码

```
cd /usr/local/src/
git clone https://github.com/p1r06u3/opencanary_web.git
cd opencanary_web/
```

3. 安装mysql
自行Baidu or Google

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
这时数据库中User表内默认用户名和密码为：admin\admin
若要修改web后台登录密码请执行sql语句password的值换成自己的md5值：
```
UPDATE User SET password='900150983cd24fb0d6963f7d28e17f72' WHERE id=1;
```

5. 修改web数据库连接密码

vi /usr/local/src/opencanary_web/dbs/initdb.py
```
DB_PWD = 'huanchengzijidemima'
```
换成自己的mysql密码

5. 单tornado实例启动测试

```
python server.py --port=8081
```
若输出Development server is running at http://0.0.0.0:8081/，且访问主机的ip能够显示出登录后台地址，则web单实例后台启动成功。

### 安装supervisor

自行Baidu or Google

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

启动supervisor服务
```
service supervisord start
```
启动多tornado实例
```
supervisorctl start tornadoes:*
```
关于supervisor更多的使用方法，可以搜一下；如果你修改了supervisor配置，可能需要重启supervisor服务，然后再启动实例。

查看应用web是否启动成功：
ps aux|grep python
```
root     30403  2.1  0.3 256192 30596 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8000
root     30404  1.8  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8001
root     30406  2.0  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8002
root     30407  2.0  0.3 256192 30592 ?        S    16:08   0:00 python /usr/local/src/opencanary_web/server.py --port=8003
```

### 安装nginx反向代理tornado

自行Baidu or Google

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
nginx反向代理tornado配置：
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

启动nginx
```
systemctl start nginx.service
```
查看nginx是否启动成功：
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