<h1 align='center'>MySQL预配制版使用手册</h1>

## 1. 获取程序

- 下载地址  *仅限公司内部使用*

```
http://172.16.20.10/Oracle/MySQL-Community/mysql-5.6.38-presetup-el7-x64.tar.xz
```

## 2. 应用平台

```
CentOS 6.9
CentOS 7.4.1708
```

## 3. 资源配置

- 推荐配置

|CPU(core)|Memory(GB)|
|:-:|:-:|
|4|8|

- 最低配置

|CPU(core)|Memory(GB)|
|:-:|:-:|
|2|4|

## 4. 配置程序

- 创建mysql用户

```
[root@mysqlsrv ~]# useradd mysql
[root@mysqlsrv ~]# passwd mysql
```

- 使用mysql账户登录系统

- 下载软件包

```
[mysql@mysqlsrv ~]$ curl -O http://172.16.20.10/Oracle/MySQL-Community/mysql-5.6.38-presetup-el7-x64.tar.xz
```

- 解压软件包 *如果是centos6，则需要安装xz工具解压*

 ```
 [mysql@mysqlsrv ~]$ tar xvf mysql-5.6.38-presetup-el7-x64.tar.xz && rm mysql-5.6.38-presetup-el7-x64.tar.xz -rf 
 ```
 
 - 启动程序 **建议在启动前使用sh managerdb.sh -h查看程序帮助**
 
 ```
 [mysql@mysqlsrv ~]$ cd mysql-5.6.38-linux-glibc2.12-x86_64
 [mysql@mysqlsrv mysql-5.6.38-linux-glibc2.12-x86_64]$ sh managerdb.sh start
 ```
