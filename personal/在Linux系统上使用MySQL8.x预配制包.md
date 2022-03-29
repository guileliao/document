# 在Linux系统上使用MySQL8.x预配制包

**最近公司要应对该死的牢厂什么狗屁框采的红线测试，搞得所有人都不安生，所有软件要升级。因为MySQL8.x是我们从来没用过的版本，以前一直都是MySQL5.7，现在这数据库也要升级了。记录一下过程算是备忘吧。既然是备忘，那就不是所谓给白痴也能看懂的文档，如果看不懂那就是本人才疏学浅，别BB。**

## 1.怎么选择MySQL的版本
首先解释一下什么吉奥预配制包。一般来说我们在dev.mysql.com网站上下载的tar包，并且在下载归类时属于“Linux-Generic”，版本分为“glibc2.12”和“glibc2.17”两种。其实到这个时候大多数人已经懵逼了，这鬼东西该怎么选择。作者给你个建议吧，就选“glibc2.17（x86_64）”，别问为什么，用就是了。知道原因的人自然知道，不知道这篇文章也不可能让你知道。因为要讲清楚这些东西基本上要把Linux系统的基础构成讲一遍，所以作者放弃。

## 2.去哪里下载
下载地址：https://dev.mysql.com/downloads/mysql/8.0.html

下载的包名“**mysql-8.0.XX-linux-glibc2.17-x86_64-minimal.tar.xz**”，看清楚别搞错了，其中XX代表版本号，不要认为就是XX。

如果你实在是懒可以用作者已经做好初始化的包直接用就好了。
下载地址：http://172.16.20.10/mysql-community/mysql-8.0.28-linux-glibc2.17-x86_64.tar.xz
下载地址：http://172.16.20.10/mysql-community/mysql-8.0.28-linux-glibc2.17-x86_64.tar.xz.sha256

## 3.如何选择安装环境
首先，作者所说的安装环境就是MySQL8即将运行的操作系统以及硬件环境。处理器最少1核心至于外频现在应该不会有太拉跨的处理器，内存最小也得2GB，磁盘不少于20GB。操作系统需要centos8.5以上，其实这是废话，这玩意已经终结生命周期了。建议用麒麟v10SP2或者openeuler系统的LTS版本。

最小安装环境  
处理器：1核心+  
内存：2GB+  
磁盘：20GB+  

## 4.怎么安装
### 4.1初始化
- step 1  
创建一个非特权用户，“mysql”。
```
# useradd mysql
```
- step 2  
使用mysql账户登录系统，此时所有的工作路径就都在“/home/mysql”下，注意这个路径以后多次出现。

- step 3  
下载好官方安装包后，在“/home/mysql”路径下解压此包，并创建一个名为mysql-server的软连接指向解压后的目录。

```
$ pwd
$ tar xvf mysql-8.0.XX-linux-glibc2.17-x86_64-minimal.tar.xz
$ ln -s mysql-8.0.XX-linux-glibc2.17-x86_64-minimal mysql-server
```
**为什么要创建这个软连接，麻烦自己脑补一下，如果你非要认为这是多此一举就请删掉，别BB。**

- step 4  
在“/home/mysql/mysql-server/”创建一个名为“my.cnf”的文件，并将如下内容写入。
```
$ cat>>/home/mysql/mysql-server/my.cnf<<EOF
[mysqld]
basedir=/home/mysql/mysql-server/
datadir=/home/mysql/mysql-server/data
socket=/tmp/mysql.sock
user=mysql
explicit_defaults_for_timestamp=1
max_connections=4096
lower_case_table_names=1
#lower_case_table_names=0
character-set-server=utf8
wait_timeout=1814400
skip-name-resolve
max_allowed_packet=20M
default_authentication_plugin=mysql_native_password

#--------
#sql_mode
#--------
#sql_mode='ONLY_FULL_GROUP_BY,NO_AUTO_VALUE_ON_ZERO,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION,PIPES_AS_CONCAT,ANSI_QUOTES'
sql_mode='NO_ZERO_IN_DATE,STRICT_TRANS_TABLES,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'

#------
#Innodb
#------
innodb_buffer_pool_size=512M
innodb_log_file_size=128M
innodb_log_buffer_size=8M
innodb_flush_log_at_trx_commit=0
innodb_lock_wait_timeout=50

#=============
[mysqld_safe]
#=============
log-error=/home/mysql/mysql-server/log/mysqld.err
pid-file=/home/mysql/mysql-server/run/mysqld.pid
default-character-set=utf8
EOF
$ cat /home/mysql/mysql-server/my.cnf
$ mkdir -p /home/mysql/mysql-server/{log,run}
```

- step 5  
初始化开始
```
/home/mysql/mysql-server/bin/mysqld \
--initialize \
--defaults-file=/home/mysql/mysql-server/my.cnf
```
**初始化完了你会得到一个随机的密码，这个密码是MySQL8的“root”账户的初始密码。注意，不是操作系统的“root”账户，是MySQL8的“root”账户。至于如何改MySQL的密码，这个请自己度娘，作者不想敲。**

### 4.2运行MySQL8.x
如果你使用的是4.1步骤中的成果，在一台新环境上部署MySQL8.x，那么一切就要从头开始。
- step 1  
创建一个非特权用户，“mysql”。
```
# useradd mysql
```
- step 2  
使用mysql账户登录系统，此时所有的工作路径就都在“/home/mysql”下，注意这个路径以后多次出现。

- step 3  
下载预配制包，解压，运行。
```
$ curl -O http://172.16.20.10/mysql-community/mysql-8.0.28-linux-glibc2.17-x86_64.tar.xz
$ tar xvf mysql-8.0.28-linux-glibc2.17-x86_64.tar.xz
$ /home/mysql/mysql-server/bin/mysqld_safe --defaults-file=/home/mysql/mysql-server &
```
**这个步骤中的启动命令是交互式启动，并把MySQL8的进程打到后台。如果需要随系统自启动，你可以使用rc.local或者systemd。但是作者就不在这里写这些，自己度娘。**
