# -*- coding:utf-8 -*-
# __author__ = 'kafka'

import os
from utils.Logger import log


class LogDir(object):
    def __init__(self):
        self.initDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def log_dir(self):
        return os.path.join(self.initDir, 'log')

    def log_path(self):
        logDir = self.log_dir()
        if os.path.exists(logDir):
            log('log_path').info('log path is exists,no need create!')
        else:
            os.mkdir(logDir)
            log('create log path').debug('log path create success!')
            log('log path').debug('log path:' + logDir)
