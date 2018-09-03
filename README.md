sudo apt-get install -y python-dev python-pip python-virtualenv libpcap-dev
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev

pip install --upgrade virtualenv
pip install --upgrade setuptools
virtualenv env/
. env/bin/activate

pip install opencanary
pip install pyasn1-modules
pip install service_identity
pip install scapy pcapy
pip install rdpy
pip install pyinotify
pip install apscheduler

mkdir /etc/opencanaryd


```
pcap.h: No such file or directory
sudo apt-get install libpcap-dev
```

page 1 1-10 0 
page 2 11-20 10
page 3 21-30 20
10*page-10



pip install tornado
pip install PyJWT
pip install python-jwt
pip install sqlalchemy
pip install pymysql
pip install configparser

## 安装配置sendmail
alternatives --config mta
yum -y install m4
yum -y install sendmail-cf
vi /etc/mail/sendmail.mc
m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf

hostnamectl set-hostname honeypot.com



