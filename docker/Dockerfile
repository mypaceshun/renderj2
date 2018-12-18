FROM centos:latest
MAINTAINER KAWAI Shun
ARG rootdir="/home/rpmbuilder"

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install rpm-build rpmdevtools gcc make tar openssl-devel openldap-devel tree
RUN yum -y install python-devel python34-devel python36-devel
RUN yum -y groupinstall "Development Tools"
RUN mkdir -p ${rootdir}
ADD rpm.tar.gz ${rootdir}
RUN chown -R root:root ${rootdir}/rpm
RUN ln -s ${rootdir}/rpm/CMD.sh /CMD

CMD ["/CMD"]
