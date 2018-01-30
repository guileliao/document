

**本文仅使用于南京测评项目，描述内容仅包含测评项目中的linux服务器的部署过程；**  
**由于本文有可能会在linux终端上显示，所以采用utf-8字符集的md格式文本编写；**  
**时间仓促，和格式限制，本文中将不提供配图和格式高亮，如需要高亮语法，请使用vim或者gvim等文本编辑器查看;**  
**编者：guile.liao**  
**邮件地址：liaolei@geostar.com.cn**  
**注意：文中提到的软件包都会随同文档一起提交。**  



## 1. 操作系统定义

 - 操作系统类型：CentOS-7.3.1611以上，建议采用CentOS-7.4.1708

 - 磁盘分区：

   |类型|挂载点|文件系统|尺寸|  
   |-|-|-|-| 
   |基础分区|/boot|ext4|500MB|  
   |基础分区|/|ext4|200GB|  
   |基础分区|/home|ext4|剩余可用空间|  

 - 操作系统软件集：最小化安装CentOS

## 2. 部署oracle jdk8u162

 - 将程序包“jdk-8u162-linux-x64.tar.gz”上传到linux服务器（以下简称服务器）的“/opt”目录下；

 - 校验程序包的md5码；
```bash
	# md5sum /opt/jdk-8u162-linux-x64.tar.gz
```
 - 解压程序包；
```bash
	# cd /opt
	# tar xvf jdk-8u162-linux-x64.tar.gz && rm /opt/jdk-8u162-linux-x64.tar.gz -rf
```

## 3. 部署elasticsearch-2.4.6（随文档提交的软件包内已经预先做了配置处理，请检查配置文件。）

 - 将程序包“elasticsearch-2.4.6-with-plugin.tar.xz”上传到服务器的“/srv”目录下；

 - 校验程序包的md5码；
```bash
	# md5sum /srv/elasticsearch-2.4.6-with-plugin.tar.xz
```
 - 解压程序包；
```bash
	# cd /srv
	# tar xvf elasticsearch-2.4.6-with-plugin.tar.xz && rm /srv/elasticsearch-2.4.6-with-plugin.tar.xz -rf
```
 - 修改配置文件；
```bash
	# cd /srv/elasticsearch-2.4.6/conf
	# cp -a elasticsearch.yml elasticsearch.yml.$(date +%Y%m%d%H%M)
	# cat>elasticsearch.yml<<EOF
		cluster.name: elasticsearch-test
		node.name: node1
		node.rack: r1
		index.max_result_window: 100000
		network.host: $(hostname -I)
		EOF
```
 - 启动elasticsearch
```bash
	# sh /srv/elasticsearch-2.4.6/starup.sh
```

## 4. 部署apache-tomcat6.0.53

 - 将程序包“apache-tomcat-6.0.53-vm.tar.xz”上传到服务器的“/srv”目录下；

 - 校验程序包的md5码；
```bash
	# md5sum /srv/apache-tomcat-6.0.53-vm.tar.xz
```
 - 解压程序包；
```bash
	# cd /srv
	# tar xvf apache-tomcat-6.0.53-vm.tar.xz && rm /srv/apache-tomcat-6.0.53-vm.tar.xz -rf
```
 - 启动apache-tomcat6.0.53(注意在catalina.sh文件前段声明**JAVA_HOME**)
```bash
	# /srv/apache-tomcat-6.0.53/bin/catalina.sh start
```




## md5码对照表

   |md5码|文件名|
   |-|-|
   |776ff2fbc355dd2b297ef76a17c91592|apache-tomcat-6.0.53-vm.tar.xz|
   |2164a10d36a752cba67369a02ed9694c|elasticsearch-2.4.6-with-plugin.tar.xz|
   |781e3779f0c134fb548bde8b8e715e90|jdk-8u162-linux-x64.tar.gz|

