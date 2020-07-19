FROM centos:centos7.5.1804
MAINTAINER yerikyu "yerik_shu@139.com"
COPY /install/install_opencanary_agent.sh /usr/local/src
WORKDIR /usr/local/src
RUN yum install -y epel-release &&\
    yum -y update &&\
    yum install -y iptables-services &&\
    yum install -y libpcap-devel &&\
    yum install -y openssl-devel &&\
    yum install -y libffi-devel &&\
    yum install -y python-devel &&\
    yum install -y gcc &&\
    yum install -y gcc-c++ &&\
    yum install -y ntpdate &&\
    yum install -y python-pip &&\
    yum install -y rsyslog