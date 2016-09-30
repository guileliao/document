请注意如果在CentOS6中安装MySQL5.6，则一下包会被替换：
mysql-community-libs.x86_64.5.6.26-2.el6会替换系统中的mysql-libs.x86_64 5.1.73-5.el6_6
mysql-community-libs-compat.x86_64.5.6.26-2.el6会替换系统中的mysql-libs.x86_64 5.1.73-5.el6_6




yum install nfs-utils ntpdate vsftpd wget ntp tomcat6-admin-webapps tomcat6-webapps mysql-server mysql cloudstack-management cloudstack-agent system-config-network-tui bridge-utils createrepo ftp httpd


mysql-server-community-5.6.x

yum install perl perl-DBI perl-Module-Pluggable perl-Pod-Escapes perl-Pod-Simple perl-libs perl-version




#cloudstack全局配置
secstorage.allowed.internal.sites（192.168.230.40） #模板上传地址，可用ip和网段
expunge.delay（120） #虚拟机实际销毁时间
expunge.interval（60） #虚拟机销毁间隔时间
endpointe.url（http://192.168.2390.10:8080/client） #管理节点访问地址
max.account.user.vms（253） #每用户最大创建虚拟机数量

#服务方案
在计算方案名称后加“-preset”