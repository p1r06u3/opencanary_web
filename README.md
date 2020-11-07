## 一、web服务端介绍
Tornado+Vue+Mysql+APScheduler+Nginx+Supervisor

### 1. 架构图
![架构图](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/honeypot.png)

### 2. 功能展示

#### 2.1 登录页面
![登录页面](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/login.png)

#### 2.2 仪表盘
![仪表盘](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/dashboard.png)

#### 2.3 主机状态
![主机状态](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/hoststatus.png)

#### 2.4 攻击列表
![攻击列表](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/attacklist.png)

#### 2.5 过滤列表
![过滤列表](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/filterlist.png)

#### 2.6 邮件配置
![邮件配置](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/mailconf.png)

#### 2.7 白名单ip
![白名单ip](https://raw.githubusercontent.com/p1r06u3/opencanary_web/master/docs/images/whiteiplist.png)

## 二、安装方式
可以选择通过脚本自动化安装，也可以选择手工安装。

### 1. 自动化安装

* [更省心省力的自动化安装方式](/docs/install/Linux_AutoInstall.md)

### 2. 手工安装

* [让你更了解蜜罐的手工安装方式](/docs/install/Manual_Installation.md)

### 3. 一些使用说明

* [后台和客户端的一些使用说明](/docs/install/Document.md)


## 三、后台可统计的信息

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
19. rdp协议windows远程登录；
20. snmp扫描；
21. sip请求；
22. mssql登录sql账户认证；
23. mssql登录win身份认证；
24. http代理登录尝试；

## 四、项目致谢

1. **Thinkst Applied Research**

2. **天使用户群和开源贡献者**：

    @Weiho @kafka @Pa5sw0rd @Cotton @Aa.Kay @冷白开 @YongShao @Lemon

## 五、报告问题

在使用过程当中出现任何问题，请点击[这里](https://github.com/p1r06u3/opencanary_web/issues/new)反馈