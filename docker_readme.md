# 使用之前
确认一下本机的防火墙是不是已经关了，如果关了需要打开防火墙，因为docker的网络管理是基于防火墙，关闭防火墙会导致打包失败、docker容器不能上网等问题

## 已经打包并发布在腾讯云的docker仓库
不想自己打包的可以通过以下命令来获取最新镜像
```
docker pull ccr.ccs.tencentyun.com/otherproject/honeypot-web
docker pull ccr.ccs.tencentyun.com/otherproject/honeypot-agent
```

# 使用说明
1. 使用agent的话，就用./buildDocker.sh进行打包
2. 使用master的话，就用./buildWebDocker.sh进行打包
3. 这些镜像打包之后需要在特权模式下运行docker container
由于蜜罐的部署需要使用iptable这个需要有root权限，因此需要使用以下命令使用特权模式访问。此外还需要注意的是在创建容器的时候要进行端口映射（由于是容器化进行操作，需要考虑在容器的端口映射）
`docker run -tdi -p {hostport:containerport} --privileged {image:version} bash`
如
```
docker run -tdi -p 12312:80 .... --privileged honeypot-master:1.0 bash 
docker run -tdi -p 12312:80 .... --privileged honeypot-agent:1.0 bash 
```
端口映射就根据实际需要来进行映射啦
注意：使用以上命令的时候命令行会返回一串`docker container id`如
$ docker run -tdi -p 12321:80 --privileged honeypot-master:1.0 bash
$ 0ce7e270fba362fc7ae7ef14dfb4dfd81bfeb49f1b623e6d966dee29cd461702

如果忘记id可以通过`docker ps`这个命令进行重新获取

```
$ docker ps | grep honeypot
0ce7e270fba3        honeypot-master:1.0                                 "bash"                   2 minutes ago       Up 2 minutes        0.0.0.0:12321->80/tcp                                                                                            amazing_heisenberg

```

## honeypot-web
使用命令`./buildWebDocker.sh`进行docker打包
使用命令`docker run -tdi -p 12321:80 --privileged honeypot-master:1.0 bash`
由于是通过特权模式创建的容器所以需要通过`docker exec`的方式进入容器
```
$ docker exec -ti 0ce7e270fba3  bash
[root@0ce7e270fba3 src]# 
```
进入容器之后，使用`ls`就可以发现相关的文件内容
```
[root@0ce7e270fba3 src]# ls
install_opencanary_web.sh  opencanary  start.sh
```
之后使用命令进行web安装，注意到由于docker的网络环境默认使用桥接模式，我们要使容器之间的网络互通服务器的ip必须是我们的网卡ip
```
$ ip add | grep 172.16
    inet 172.16.236.1/24 brd 172.16.236.255 scope global vmnet1
    inet 172.16.28.1/24 brd 172.16.28.255 scope global vmnet2
    inet 172.16.248.1/24 brd 172.16.248.255 scope global vmnet8
$ docker exec -ti 0ce7e270fba3  bash
[root@0ce7e270fba3 src]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
20240: eth0@if20241: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:06 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.6/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
[root@0ce7e270fba3 src]# ping 172.16.28.1
PING 172.16.28.1 (172.16.28.1) 56(84) bytes of data.
64 bytes from 172.16.28.1: icmp_seq=1 ttl=64 time=0.100 ms
^C
--- 172.16.28.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.100/0.100/0.100/0.000 ms
[root@0ce7e270fba3 src]# ping 172.16.248.1
PING 172.16.248.1 (172.16.248.1) 56(84) bytes of data.
64 bytes from 172.16.248.1: icmp_seq=1 ttl=64 time=0.068 ms
64 bytes from 172.16.248.1: icmp_seq=2 ttl=64 time=0.040 ms
^C
--- 172.16.248.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1020ms
rtt min/avg/max/mdev = 0.040/0.054/0.068/0.014 ms

```
通过以上测试可以发现我们的container可以和主机之间网络互通，这就意味着，我们接下来可以通过网络把数据库服务独立出来，首先安装服务
```
[root@0ce7e270fba3 src]# chmod +x install_opencannary_web.sh
[root@0ce7e270fba3 src]# ./install_opencanary_web.sh 
###########正在初始化环境#########
服务端IP地址:172.17.0.6
IP是否正确(y/n):n
######请手动配置IP######
请输入本机IP:172.16.248.1
#########安装依赖包############
Loaded plugins: fastestmirror, ovl

```
前面说了，我们为了可以让其他容器可以访问我们的服务器，所以要把web服务ip注册在宿主机上面

# 开发思路
1. 把安装脚本进行打包，之后再容器里面进行安装
2. 作者有进行测试过，原计划是要通个手动安装的方式对容器进行定制化开发，不过经过多次测试，不是由于网络的问题就是由于权限的问题，导致服务不能持续进行

# 建议
1. 作为web需要有数据库提供服务，这里强烈建议通过docker挂载数据库，而不是在容器中起数据库服务
    1. 启动数据库建议通过` docker-compose`启动已经准备好了启动脚本，进入docker目录通过指令
`docker-compose -f marridb.yml up -d`
    2. 使用前需要修改密码，请直接在` maridba.yml`中的` MARIADB_ROOT_PASSWORD`的进行修改

# 安装
1. 关于` docker`、` docker-compose`的安装，可以看[官网指引](https://docs.docker.com/get-docker/)

