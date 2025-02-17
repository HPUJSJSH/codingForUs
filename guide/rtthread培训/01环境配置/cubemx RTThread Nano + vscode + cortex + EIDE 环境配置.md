# cubemx RTThread Nano + vscode + cortex + EIDE 环境配置



[TOC]



# 前置安装



## 需要软件

* vscode
* cubemx
* keil

## 需要插件

### C/C++

![c++.png](https://oss-club.rt-thread.org/uploads/20240923/562faa12c8847e30200daeae48771cdd.png.webp)

### cortex

* 作为一个debug的插件

![cortex.png](https://oss-club.rt-thread.org/uploads/20240923/98b4634b873c0b68e90261f08c3f5f65.png)

### EIDE

* 作为一个vscode上支持mdk5 等项目的编译与下载

![EDLE.png](https://oss-club.rt-thread.org/uploads/20240923/0b96460b16a9f73dd8ac04107fea90f1.png.webp)

### chinese

* 中文简体插件

![chinese.png](https://oss-club.rt-thread.org/uploads/20240923/038571124732cbe0c2775c9624d3c32c.png)

* OpenOCD
  * 通过百度网盘分享的文件：OpenOCD-20231002.7z
    链接：https://pan.baidu.com/s/1gGonwqx1oDEEayyoX6wiMw?pwd=1234 
    提取码：1234 
    --来自百度网盘超级会员V2的分享
* armToolchain
* gdbPath
  * 对于这一套工具，我使用的为env里面的tools
  * 通过百度网盘分享的文件：env-windows-v2.0.0.7z
    链接：https://pan.baidu.com/s/1Vjc7ih11acRWv4NICZ_egw?pwd=1234 
    提取码：1234 
    --来自百度网盘超级会员V2的分享

# 关于keil下载安装

* 建议观看b站视频并采用其安装下载方式

【STM32入门教程-2023版 细致讲解 中文字幕】https://www.bilibili.com/video/BV1th411z7sn?p=13&vd_source=d5ee3e266fe4d6633f3a89949e9f48bf

# 关于cubemx生成nano项目

* 建议观看b站视频

	【STM32CubeMX使用RT-Thread nano v4.1.1资源包教学】https://www.bilibili.com/video/BV1AUtWeiEDC?vd_source=d5ee3e266fe4d6633f3a89949e9f48bf
	
*  社区文章

  * [RT-Thread-RT-Thread Nano 上线ST CubeMXRT-Thread问答社区 - RT-Thread](https://club.rt-thread.org/ask/article/09235f1f8fe6c19e.html)




# 关于vscode配置

## cortex配置

配置调试文件

![配置调试文件.png](https://oss-club.rt-thread.org/uploads/20240923/383e5cb8d745e255b55774739de2eb5d.png.webp)

![调试文件.png](https://oss-club.rt-thread.org/uploads/20240923/76671a3e7bc8dbed471dbca656528f1d.png.webp)

### 下面附录openocd使用stlink的配置参数

```c
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "openocd",							//调试器名称
            "executable": "C:/Users/Desktop/my_work/project/stm32f103/stm32project/nano/example_stm32f103c8t6/eide/build/example_stm32f103c8t6/example_stm32f103c8t6.elf",					//要执行的烧录文件，建议通过EIDE编译时候生成elf文件
            "request": "launch",
            "type": "cortex-debug",
            "runToEntryPoint": "main",
            "targetId": "STM32F103C8T6",
            "servertype": "openocd",
            "configFiles": [
                "interface/stlink-v2.cfg",			//选择合适的烧录方式
                "target/stm32f1x.cfg"				//配置合适的文件
            ],
            "armToolchainPath": "C:/Users/Desktop/my_work/rtt/env-windows-v2.0.0/env-windows/tools/gnu_gcc/arm_gcc/mingw/bin", // ！！！需要修改为自己的GCC 工具链路径 ！！！
            "gdbPath": "C:/Users/Desktop/my_work/rtt/env-windows-v2.0.0/env-windows/tools/gnu_gcc/arm_gcc/mingw/bin/arm-none-eabi-gdb.exe" // ！！！需要修改为自己的GDB 路径 ！！！
        }
    ]
}

```

### *** 注意还需要配置openocd的路径***

vscode 中 点击扩展，找到cortex的设置，及其扩展设置：

![cortex配置0.png](https://oss-club.rt-thread.org/uploads/20240923/a1c467ca129df0e3fdca5df3255cf929.png.webp)

![cortex在setting.png](https://oss-club.rt-thread.org/uploads/20240923/f972b4b0658b02bbd1b9ce49f8bc6bb5.png.webp)

```c
{
    "cortex-debug.openocdPath": "C:/Users/Desktop/my_work/rtt/OpenOCD-20231002/bin/openocd.exe" //这里填入你的openocd的路径
}
```

## EIED配置

* 建议观看csdn文档

[vscode平台上通过Embedded IDE搭建单片机开发环境-CSDN博客](https://blog.csdn.net/weixin_41080308/article/details/128053268?sharetype=blog&shareId=128053268&sharerefer=APP&sharesource=m0_73016766&sharefrom=link)



# 总结

* 本质配置还是依靠EIDE来做编译，cortex来做debug ，vscode来做优化编写代码体验
* 本文章将优质内容链接进行粘贴，以提供给大家方便观看。

