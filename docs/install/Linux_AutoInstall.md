# Linux 自动安装

## 适配 64 位操作系统列表：
* CentOS 7
> 由于 Linux 发行版较多，无法一一适配，如果不在以上列表中，请自行手动安装

## 安装

> 在安装之前，请自行更换`yum`源
打开终端，在 root 用户 Shell 下，输入以下命令：

```
   $ curl -O https://raw.githubusercontent.com/zhaoweiho/opencanary_web/master/install/install.sh
```
或者输入输入以下命令：
```
   $ wget --no-check-certificate https://raw.githubusercontent.com/zhaoweiho/opencanary_web/master/install/install.sh
```
下载后输入
```
    chmod o+x install.sh
    ./install.sh
```
## 安装完毕

本脚本安装完毕后会以系统服务形式启动supervisord/Nginx
### 启动服务

```
$ systemctl start supervisord.service
```

### 停止服务

```
systemctl stop supervisord.service
```

### 重启服务

```
systemctl restart supervisord.service
```
### 查看服务运行状态

```
systemctl status supervisord.service
```
### 安装后信息
访问URL:http://ip<br />

|类型 | 用户名 | 密码 |
|----- |----- |-----| 
| Web账号 | admin | admin |
| mysql 数据库 | root | Weiho@2018 |
| mysql 端口 | 3306| - |
| OpenCanary_Web物理路径 | /usr/src/local/opencanary_web | - |

## 报告问题

安装脚本在使用过程当中出现任何问题，请点击[这里](https://github.com/p1r06u3/opencanary_web/issues/new)反馈
