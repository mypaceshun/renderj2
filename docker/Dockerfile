FROM centos:latest
MAINTAINER KAWAI Shun

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install rpm-build rpmdevtools gcc make tar openssl-devel openldap-devel tree
RUN yum -y install python-devel python34-devel python36-devel
RUN yum -y groupinstall "Development Tools"
ADD rpm.tar.gz /
RUN chown -R root:root /rpm

CMD ["/rpm/CMD.sh"]
