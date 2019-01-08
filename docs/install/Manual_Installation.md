## 手工安装

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

    ```
    mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak
    ```

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

这里优先推荐使用Centos7，其次Ubuntu16，因为系统比较新默认python环境为2.7.x，类库也比较新。

Centos7 最小化安装
```
yum -y install epel-release //安装epel扩展源
yum -y install libpcap-devel openssl-devel libffi-devel python-devel gcc python-pip gcc-c++
```

Ubuntu16
```
sudo apt-get install -y python-pip python-virtualenv libpcap-dev
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
```

#### 安装opencanary客户端

```
cd /usr/local/src/
git clone https://github.com/p1r06u3/opencanary.git
cd opencanary/
```

vi opencanary/data/settings.json

* 将第2行，device.node_id的值opencanary-1代表将来告警的节点，可以改为主机名等任意字符（不改也可以）。

    ```
    "device.node_id": "opencanary-1",
    ```

* 将第3行，server.ip改成自己web服务端的ip（重要）。

    注意: 如果你的web端，不是80端口，要在配置的ip后面跟上“:端口号”。

    ```
    "server.ip": "172.18.214.121",
    ```

* 将第4行，device.listen_addr改成自己本机ip(非127.0.0.1)。

    ```
    "device.listen_addr": "172.18.214.120",
    ```

安装opencanary
```
python setup.py sdist
cd dist
pip install opencanary-0.4.tar.gz
```

#### 配置端口扫描发现功能

>端口扫描发现模块是依赖于iptables；需要rsyslog配合产生kern.log日志。


##### 1 安装iptables

```
yum install iptables-services
```

##### 2 配置rsyslog

通过rsyslog 控制日志产生位置： vi /etc/rsyslog.conf

修改第50行
```
kern.*                                                 /var/log/kern.log
```
重启rsyslog

```
systemctl restart rsyslog.service
```

#### 启动和停止opencanary方法


若第一次安装opencanary，需要先运行opencanaryd --copyconfig，会生成/root/.opencanary.conf配置文件。

启动命令: opencanaryd --start

停止命令: opencanaryd --stop

重启命令: opencanaryd --restart

opencanary日志: /var/tmp/opencanary.log

#### 卸载opencanary方法

首先卸载旧客户端
```
opencanaryd --stop
rm -rf /root/.opencanary.conf
rm -rf  /usr/local/src/opencanary/
pip uninstall opencanary -y
iptables -t mangle -F
```

安装新客户端
```
curl -O https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_agent.sh
bash install_opencanary_agent.sh
```

## 报告问题

安装使用过程当中出现任何问题，请点击[这里](https://github.com/p1r06u3/opencanary_web/issues/new)反馈