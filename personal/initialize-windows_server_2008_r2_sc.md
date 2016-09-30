# 初始化Windows server 2008 R2 servercore
##系统初始化
### 1.配置系统
```powershell
c:\>sconfig
```
    a. 创建本地管理员用户(geostack:123@abc.com)
    b. 打开远程桌面
    c. 打开自动更新

### 2. 关闭防火墙
```powershell
c:\>Netsh Firewall Set Opmode disable
```
### 3.禁用页面文件
```powershell
c:\>wmic computersystem where name=“%computername%” set AutomaticManagedPagefile=False
```
### 4.删除页面文件(需要重启系统才能生效)
```powershell
c:\>wmic pagefileset delete
```
### 5.安装驱动（virtio-win-0.1.102.iso）
```powershell
c:\>pnputil -i -a 路径:\<驱动文件夹>\<驱动文件名>.inf
```
### 6.查询现有系统支持的角色列表
```powershell
c:\>dism /online /get-features /format:table
```
### 7.安装.NET Framework 2.0/3.0
```powershell
c:\>dism /online /enable-feature /featurename:NetFx2-ServerCore
	dism /online /enable-feature /featurename:NetFx3-ServerCore
```
### 8.安装IIS服务角色
```powershell
c:\>dism /online /enable-feature /featurename:IIS-WebServerRole
c:\>dism /online /enable-feature /featurename:IIS-ISAPIFilter
c:\>dism /online /enable-feature /featurename:IIS-ISAPIExtensions
c:\>dism /online /enable-feature /featurename:IIS-NetFxExtensibility
```
### 9.安装IIS-ASPNET
```powershell
c:\>dism /online /enable-feature /featurename:IIS-ASPNET
```
### 10.安装FTPSVC
```powershell
c:\>dism /online /enable-feature /featurename:IIS-FTPServer
c:\>dism /online /enable-feature /featurename:IIS-FTPSvc
c:\>dism /online /enable-feature /featurename:IIS-FTPExtensibility
```
## 11.选择远程管理控制台选项，并安装IIS管理服务：
>>>>>>> e7e6da26487c80b6d04ff32fc6fc718be616b93f
```powershell
c:\>dism /online /enable-feature /featurename:IIS-ManagementService
c:\>dism /online /enable-feature /featurename:WAS-WindowsActivationService
c:\>dism /online /enable-feature /featurename:WAS-ConfigurationAPI
```
### 12.安装成功后，还需要更改一些注册表键值来激活管理服务：
```powershell
c:\>Reg Add HKLM\Software\Microsoft\WebManagement\Server /V EnableRemoteManagement /T REG_DWORD /D 1
```
### 13.启动IIS服务
```powershell
c:\>net start w3svc
```
### 14.添加IIS服务自启动
```powershell
c:\>sc config w3svc start= auto
```
### 15.启动FTP服务
```powershell
c:\>net start FTPSVC
```
### 16.添加FTP服务自启动
```powershell
c:\>sc config FTPSVC start= auto
```
### 17.启动IIS服务管理器
```powershell
c:\>net start wmsvc
```
### 18.添加IIS服务管理器自启动
```powershell
c:\>sc config wmsvc start= auto
```
### 19.添加站点发布目录
```powershell
c:\>mkdir c:\webroot\localuser\public
```
### 20.添加本地管理员ftp私有目录
```powershell
c:\>mkdir c:\webroot\localuser\geostack
```
### 21.重启操作系统验证服务
```powershell
c:\>shutdown /r
```
### 22.关机导出模板待用
```powershell
c:\>shutdown /p
```
## 其他功能

### 下载文件
=======
## 22.关机导出模板待用
```powershell
c:\>shutdown /p
```
#####
下载文件
```powershell
>powershell
	PS>$client = new-object System.Net.WebClient
	PS>$client.DownloadFile("#1","#2")
		#1:下载文件的url；#2:下载文件的本地存放路径及用户名
		eg.("http://www.kernel.org/kernel-4.0.tar.gz","c:\software\kernel-4.0.tar.gz")
```
### 获取当前系统中已安装软件的列表
```powershell
c:\>wmic product get name,version
```
### 压缩与解压缩文件：
