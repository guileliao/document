# 初始化Windows server 2008 R2 servercore
1. 配置系统  
```powershell
sconfig
```
a. 创建本地管理员用户(geostack:123@abc.com)
b. 打开远程桌面
c. 打开自动更新

2.关闭防火墙
	Netsh Firewall Set Opmode disable
	
3.禁用页面文件
	wmic computersystem where name=“%computername%” set AutomaticManagedPagefile=False
	
4.删除页面文件(需要重启系统才能生效)
	wmic pagefileset delete
	
5.安装驱动（virtio-win-0.1.102.iso）
	pnputil -i -a 路径:\<驱动文件夹>\<驱动文件名>.inf

6.查询现有系统支持的角色列表
	dism /online /get-features /format:table

7.安装.NET Framework 2.0/3.0
	dism /online /enable-feature /featurename:NetFx2-ServerCore
	dism /online /enable-feature /featurename:NetFx3-ServerCore

10.安装IIS服务角色
	dism /online /enable-feature /featurename:IIS-WebServerRole
	dism /online /enable-feature /featurename:IIS-ISAPIFilter
	dism /online /enable-feature /featurename:IIS-ISAPIExtensions
	dism /online /enable-feature /featurename:IIS-NetFxExtensibility

11.安装IIS-ASPNET
	dism /online /enable-feature /featurename:IIS-ASPNET

12.安装FTPSVC
	dism /online /enable-feature /featurename:IIS-FTPServer
	dism /online /enable-feature /featurename:IIS-FTPSvc
	dism /online /enable-feature /featurename:IIS-FTPExtensibility

12.选择远程管理控制台选项，并安装IIS管理服务：

	dism /online /enable-feature /featurename:IIS-ManagementService
	dism /online /enable-feature /featurename:WAS-WindowsActivationService
	dism /online /enable-feature /featurename:WAS-ConfigurationAPI

13.安装成功后，还需要更改一些注册表键值来激活管理服务：
	Reg Add HKLM\Software\Microsoft\WebManagement\Server /V EnableRemoteManagement /T REG_DWORD /D 1

14.启动IIS服务
	net start w3svc

15.添加IIS服务自启动
	sc config w3svc start= auto

16.启动FTP服务
	net start FTPSVC

17.添加FTP服务自启动
	sc config FTPSVC start= auto

18.启动IIS服务管理器
	net start wmsvc

19.添加IIS服务管理器自启动
	sc config wmsvc start= auto

20.添加站点发布目录
	mkdir c:\webroot\localuser\public

21.添加本地管理员ftp私有目录
	mkdir c:\webroot\localuser\geostack

22.重启操作系统验证服务
	shutdown /r

23.关机导出模板待用
	shutdown /p


#####
下载文件
	  >powershell
	PS>$client = new-object System.Net.WebClient
	PS>$client.DownloadFile("#1","#2")
		#1:下载文件的url；#2:下载文件的本地存放路径及用户名
		eg.("http://www.kernel.org/kernel-4.0.tar.gz","c:\software\kernel-4.0.tar.gz")

获取当前系统中已安装软件的列表
	wmic product get name,version

压缩与解压缩文件：
