# Deepseek本地部署及连接知识库



## 准备工作

- 关闭防火墙

示例步骤：

Windows系统

1. Win+R打开控制面板并输入“control”

![](image/进入控制面板.png)

2.单击“系统和安全”

![](image/1.png)

3.单击“Windows Defender防火墙”

![](image/2.png)

4.单击 “启用或关闭Windows Defender防火墙”

![](image/3.png)

5.在 “专用网络设置和公用网络设置”里，都关闭 Windows Defender防火墙

![](image/4.png)

6.单击“确定”

![](image/5.png)



## 一、下载Ollama



进入https://ollama.com

![](image/6.png)

选择合适的系统版本下载

![](image/7.png)

点击“Download for XXX”进行下载并安装

下载安装完成后，Win+r 打开终端

![](image/8.png)

在终端输入ollama help 如果出现下面这些表明下载完成

![](image/9.png)



## 二、下载deepseek-R1模型



进入https://ollama.com

1.搜索deepseek-r1

![](image/10.png)

2.根据自己电脑配置选择不同模型

![](image/11.png)

如何查看自己电脑的配置？

2.1windows设置查看：

　　1、点击设置

　　从Windows电脑桌面左下角找到并点击“ 开始 ”，出现弹窗后点击“ 设置 ”。

　　2、点击系统

　　弹出windows设置窗口后，点击页面中的“系统”进入。

　　3、点击关于

　　从页面左侧的功能栏里找到并点击“关于”，右边页面将会出现设备规格即可查看电脑配置。

　　快捷键查看

　　1、按住win和R

　　[键盘](https://product.pconline.com.cn/keyboard/)上同时按住win和R键，页面将会出现一个小弹窗。

　　2、点击确定

　　从小弹窗里输入“dxdiag”,并点击确定选项，进入一个新的页面。

　　3、查看配置

　　待弹出页面后，系统信息下便是电脑配置，可自行查看。



　　2.2mac查看

　　1、点击关于本机

　　点击桌面左上角的苹果图标，再点击关于本机进入。

　　2、选择配置信息

　　出现弹窗后在上方功能栏，选择想查看的电脑配置信息。

　　3、查看配置

　　如果想查看更加详细的信息，点击“ 系统报告 ”，电脑配置详情便出现，即可自行查看。



选择显存满足魔性要求的版本下载

![](image/12.png)

选择好模型复制指令（以32b为例）

![](image/13.png)

3.在终端输入此指令进行下载deepseek模型

![](image/14.png)

自动安装模型

![](image/15.png)

安装成功(输入命令演示)

![](image/16.png)

4.如果下次再从终端打开运行模型输入以下命令：
==ollama run deepseek-r1:**b==，**为自己下载的模型名称

![](image/17.png)



## 三、下载Cherry Studio（用来美化界面以及连接知识库等作用）



进入https://cherry-ai.com下载客户端

![](image/18.png)

下载软件并安装



## 四．下载词嵌入模型



进入https://ollama.com还是ollama官网

搜索shaw/dmeta-embedding-zh

![](image/19.png)

复制指令

![](image/20.png)

在终端输入指令下载

![](image/21.png)



## 五．在Cherry Studio中选用本地模型进行对话



打开安装好的Cherry Studio按步骤操作

![](image/22.png)

点击添加

![](image/23.png)

选择本地部署的模型就可进行对话

![](image/24.png)



## 六．在Cherry Studio中连接知识库



进入知识库添加页面并点击添加

![](image/25.png)

知识库名称自己命名，嵌入模型选用刚才下载的词嵌入模型
可以添加文件到知识库

![](image/26.png)

添加知识库后，在对话时就可选择知识库，让大模型根据提供知识库回答

![](image/27.png)



## 视频教程



B站视频链接：https://b23.tv/OF0eUEp