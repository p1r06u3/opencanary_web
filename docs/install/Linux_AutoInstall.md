# Linux下蜜罐管理后台和蜜罐agent自动安装方法

## 适配 64 位操作系统列表：
* CentOS 7
> 由于 Linux 发行版较多，暂时无法一一适配，如果不在以上列表中，请自行手动安装。

## 安装蜜罐管理后台-Web

> 在安装之前，请自行更换`yum`源

打开终端，在 root 用户 Shell 下，输入以下命令：

```
curl -O https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_web.sh
```
或者输入输入以下命令：
```
wget --no-check-certificate https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_web.sh
```
下载后输入
```
bash install_opencanary_web.sh
```
### 安装完毕

本脚本安装完毕后会以系统服务形式启动Supervisord/Nginx/Mysql
### 启动服务

```
systemctl start supervisord.service
systemctl start nginx.service
systemctl start mariadb.service
```

### 停止服务

```
systemctl stop supervisord.service
systemctl stop nginx.service
systemctl stop mariadb.service
```

### 重启服务

```
systemctl restart supervisord.service
systemctl restart nginx.service
systemctl restart mariadb.service
```

### 查看服务运行状态

```
systemctl status supervisord.service
systemctl status nginx.service
systemctl status mariadb.service
```

### 安装Web后信息
访问URL:http://$ip<br />

|类型 | 用户名 | 密码 |
|----- |----- |-----| 
| Web账号 | admin | admin |
| mysql 数据库 | honeypot | Weiho@2019 |
| mysql 端口 | 3306| - |
| OpenCanary_Web物理路径 | /usr/src/local/opencanary_web | - |
| 发件人邮件配置 | /usr/local/src/opencanary_web/application.py | - |
| 收件人邮件配置(以及告警开关)| /usr/local/src/opencanary_web/util/conf/email.ini | - |

## 安装蜜罐客户端-Agent
另外开一台虚拟主机(VPS)安装蜜罐客户端.

```
curl -O https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_agent.sh
```
或者输入输入以下命令：
```
wget --no-check-certificate https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/install/install_opencanary_agent.sh
```
下载后输入
```
bash install_opencanary_agent.sh
```
输入上面Web服务端的IP.等待脚本执行完毕,即可.

到服务端的Web页面进行管理http://$ip.

## 报告问题

安装脚本在使用过程当中出现任何问题，请点击[这里](https://github.com/p1r06u3/opencanary_web/issues/new)反馈
