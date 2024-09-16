# 本项目基于树莓派与yolov8s



[TOC]

# 目录结构

![](.\image\目录结构.png)

# config

* 存放配置文件

* 目前支持设置sql配置信息
* 摄像头配置信息
* 以及模型的配置信息

# model

* model文件夹下面存放目前训练好的ncnn模型
* 具体训练过程与到处不再叙述，建议直接看yolov官网

.

# camera.py

* 可以直接运行查看目前目标检测情况

# detector.py

* 存放对于yolov的api封装

# LoadConfig.py

* 用来进行加载./config/config.json的配置信息，并提供api来进行访问