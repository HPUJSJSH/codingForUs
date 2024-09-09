"""
log:
    2024/9/9    up  by cxs
"""

import json


class LoadConfig():
    def __init__(self):
        #定义初始化属性
        self.ConfigPath = './config/config.json'
        self.ConfigContent = None

        #加载
        self.__LoadConfigContent()


    def __LoadConfigContent(self):
        """

        :return: 无返回，对本身加载config content
        """
        with open(self.ConfigPath, 'r',encoding='utf-8') as fp:
            self.ConfigContent = dict(json.load(fp))

    def GetConfigNames(self):
        """

        :return:返回各个参数的名称
        """
        keys = {}
        for i in self.ConfigContent.keys():
            keys[i] = self.ConfigContent[i].keys()
        return keys

    def GetConfigValue(self,sql=False,camera=False,model=False):
        """
        bool 为ture则返回对应的值
        :param sql:
        :param camera:
        :param model:
        :return: dict
        """
        dic = {}
        if sql:
            dic['sql']=self.ConfigContent['sql']
        if camera:
            dic['camera'] = self.ConfigContent['camera']
        if model:
            dic['model'] = self.ConfigContent['model']

        return dic
if __name__ == '__main__':
    loadConfig = LoadConfig()

    print(loadConfig.GetConfigNames())
    print(loadConfig.GetConfigValue(sql=True))
    print(loadConfig.GetConfigValue(sql=True,camera=True))
