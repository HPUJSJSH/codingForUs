"""
log:
    2024/9/9    up  by cxs
"""

# import os
from ultralytics import YOLO
from LoadConfig import LoadConfig
import cv2

class detector(LoadConfig):
    def __init__(self):
        super(detector,self).__init__()

        #初始化参数
        self.ModelPath = None
        self.thord = None
        self.model = None
        self.half =None
        self.imgsz = None

        self.results = None

        #初始化方法
        self.__SetConfig__()
        self._SetModel()



    def __SetConfig__(self):
        self.config = self.GetConfigValue(model=True)['model']

        self.ModelPath = self.config['path']
        self.thord = self.config['thord']
        self.half = bool(self.config['half'])
        self.imgsz = self.config['imgsz']
    def _SetModel(self):
        self.model = YOLO(self.ModelPath)

    def predict(self,img):
        self.results = self.model.predict(img,conf=self.thord,imgsz=self.imgsz,half=self.half)


    def GetPlotPicture(self):
        return self.results[0].plot()

    def GetStrRecord(self):
        return self.results[0].verbose()






