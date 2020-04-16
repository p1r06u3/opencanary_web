# 使用说明
1. 使用agent的话，就用./buildDocker.sh进行打包
2. 使用master的话，就用./buildMasterDocker.sh进行打包
3. 这些镜像打包之后需要在特权模式下运行docker container
由于蜜罐的部署需要使用iptable这个需要有root权限，因此需要使用以下命令使用特权模式访问。此外还需要注意的是在创建容器的时候要进行端口映射（由于是容器化进行操作，需要考虑在容器的端口映射）
`docker run -tdi -p {hostport:containerport} --privileged {image:version} /usr/sbin/init`
如
```
docker run -tdi -p 12312:80 .... --privileged honeypot-master:1.0 /usr/sbin/init 
docker run -tdi -p 12312:80 .... --privileged honeypot-agent:1.0 /usr/sbin/init 
```
端口映射就根据实际需要来进行映射啦

# 开发思路
1. 把安装脚本进行打包，之后再容器里面进行安装
2. 作者有进行测试过，原计划是要通个手动安装的方式对容器进行定制化开发，不过经过多次测试，不是由于网络的问题就是由于权限的问题，导致服务不能持续进行

# 建议
1. 作为web需要有数据库提供服务，这里强烈建议通过docker挂载数据库，而不是在容器中起数据库服务
