"""
log:
    2024/9/9    up  by cxs
"""


from LoadConfig import LoadConfig
import cv2
import time
import threading
from detector import detector
class camera(LoadConfig):

    def __init__(self):
        super(camera,self).__init__()
        #定义初始化变量
        self.CameraId = None
        self.height = None
        self.width = None
        self.dpi = None
        self.capture = None
        self.FrameAndTime = {}

        #加载摄像头参数
        self.__LoadCameraConfig()
        self.__DetectCameras()
        self.__OpenCamera()


    def __LoadCameraConfig(self):
        CameraConfig = self.GetConfigValue(camera=True)['camera']

        self.CameraId = CameraConfig['ID']
        self.height = CameraConfig['height']
        self.width = CameraConfig['width']


    def __DetectCameras(self):

        try:
            capture = cv2.VideoCapture(self.CameraId)

            if capture.isOpened():
                ret, frame = capture.read()

                if ret == True:
                    capture.release()
                    pass
                else:
                    capture.release()
                    raise f'摄像头{self.CameraId}打开出现问题'

        except:
            raise f'摄像头{self.CameraId}打开出现问题'

    def __OpenCamera(self):
        """
        打开摄像头
        :return:
        """
        self.capture = cv2.VideoCapture(self.CameraId)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def GetCurentFrame(self):
        """

        :return:获得当前照片
        """
        ret, frame = self.capture.read()
        if ret == True:
            return frame
        else:
            raise f'摄像头{self.CameraId}的视频流出现问题'


    def GenerateFrameAndTime(self):
        """
        dict：
        key 时间戳
        value 三维数组帧
        存储到
        :return:
        """
        self.FrameAndTime[time.time()] = self.GetCurentFrame()


    def LoadVideo(self):
        self.video = threading.Thread(target=camera.__StartVideoCapture,daemon=True)
        self.video.start()




    def __StartVideoCapture(self):
        while 1:
            ret,frame = self.capture.read()
            cv2.imshow(f"Camera", frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyWindow('Camera')



    @staticmethod
    def GrayFrame(frame):
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        return img_gray
    @staticmethod
    def ThresholdFrame(frame):
        if frame.shape[-1]==3:
            frame = camera.GrayFrame(frame)
        else:
            pass
        ret, img = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY);
        return img



    def DrawImage(self,frame,name):

        # plt.figure(num=name,clear=True) # 图像窗口名称
        # if frame.shape[-1]==3:
        #
        #     plt.imshow(frame)
        # else:
        #     plt.imshow(frame,cmap='gray')
        # plt.axis('off')
        #
        # plt.show(block=True)

        cv2.imshow(name,frame)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            cv2.destroyWindow(name)


    def CloseCamera(self):
        """
        关闭摄像头资源
        :return:
        """
        self.capture.release()


    def __del__(self):
        self.CloseCamera()

if __name__ == '__main__':
    num = 0
    camera = camera()
    predictor = detector()
    # camera.LoadVideo()
    time = time.time()

    while True:

        frame = camera.GetCurentFrame()
        print(frame.shape)
        if num<=100:


            num +=1
        else:
            predictor.predict(frame)
            frame =predictor.GetPlotPicture()
            record = predictor.GetStrRecord()
            print(record)

            num=0

        camera.DrawImage(frame, "Frame")
        print('-'*50)




