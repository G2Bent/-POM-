import os
from BasePages.Config import LOG_PATH,Config
import logging
from logging.handlers import TimedRotatingFileHandler

class Logger(object):
    def __init__(self,logger_name=' framwork'):
        self.logger = logging.getLogger(logger_name) #创建一个logger对象
        self.logger.setLevel(logging.DEBUG)
        #self.log_path = LOG_PATH+r'\\'+self.file_name

        """
        获取ymal配置文件中的信息,ymal中的数据格式目前转化为json为dict类型
        """
        config = Config().get('log')
        print(config)
        self.file_name = config.get('file_name') if config and config.get('file_name') else 'test.log'
        self.backcup = config.get('backup') if config and config.get('backup') else 5
        self.console_level = config.get('console_level') if config and config.get('console_level') else 'DEBUG'
        self.file_level = config.get('file_level') if config and config.get('file_level') else 'DEBUG'
        self.parttern = config.get('parttern') if config and config.get('parttern') else '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
        self.log_path = os.path.join(LOG_PATH,self.file_name)
        print(self.log_path)
        print(self.file_level)
    def get_logger(self):
        streamhander = logging.StreamHandler()
        streamhander.setLevel(self.console_level)
        file_hander = TimedRotatingFileHandler(self.log_path,when='D',interval=1,backupCount=self.backcup,delay = False,encoding='utf-8')
        file_hander.setLevel(self.file_level)
        formatter = logging.Formatter(self.parttern)
        streamhander.setFormatter(formatter)
        file_hander.setFormatter(formatter)
        self.logger.addHandler(streamhander)
        self.logger.addHandler(file_hander)
        return self.logger

# logger = Logger().get_logger()
# logger.debug('123')
# logger.debug('12366')