## web后台和agent的一些使用方法

### 配置告警邮件

vi /usr/local/src/opencanary_web/application.py

smtp服务器默认配置中使用的是163，改成自己的

> 注意，163的smtp的密码不是你的邮箱登录密码，而是163邮箱的客户端授权密码，需单独开启。

```
# smtp邮件服务器配置
mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="qyfllyj"                           #用户名
mail_pass="opencanary123"                     #密码
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
insert into Whiteip values('172.18.88.76'),('172.168.1.1');
```

如果往后攻击请求来源ip是白名单表内的ip，攻击日志将会在后台的过滤列表中出现。

### 查看web日志进行排错

```
tailf /usr/local/src/opencanary_web/logs/app.log
```

### 新增管理员
将test换成自己想要设置的管理员账号

将1bc29b36f623ba82aaf6724fd3b16718换成自己的密码的32位md5值
```
insert into User values(username, password, create_time) values("test","1bc29b36f623ba82aaf6724fd3b16718",now());
```

### 清空数据库表内数据

进入数据库方法：
```
mysql -uroot -p
```

删除离线主机：
```
use honeypot;
delete from Host where status='offline';
```

删除过滤列表数据：
```
use honeypot;
delete from OpencanaryLog where white=1;
```

删除攻击列表数据：
```
use honeypot;
delete from OpencanaryLog where white=2;
```

### 后台更新方法

1. 停止tornado和下载最新源码
    ```
    supervisorctl stop tornadoes:
    cd /usr/local/src/
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

### 启动和停止opencanary方法


若第一次安装opencanary，需要先运行opencanaryd --copyconfig，会生成/root/.opencanary.conf配置文件。

生成配置：opencanaryd --copyconfig

启动命令: opencanaryd --start

停止命令: opencanaryd --stop

重启命令: opencanaryd --restart

开发模式运行: opencanaryd --dev

opencanary日志: /var/tmp/opencanary.log

配置文件位置: /root/.opencanary.conf

### 卸载和重新安装opencanary

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

使用过程当中出现任何问题，请点击[这里](https://github.com/p1r06u3/opencanary_web/issues/new)反馈