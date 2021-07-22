# -*- coding:utf-8 -*-
# __author__ = 'kafka'

import pandas
import random
import shutil
import time
import os
from conf import conf
from utils.Logger import log


class ReadData(object):
    def __init__(self):
        self.file_path = conf.FILE_PATH
        self.dtype = {
            'column1': str,
            'column2': str,
            'column3': str,
            'column4': str
            # todo
        }

    def read_column_value(self):
        df = pandas.read_excel(self.file_path, engine='openpyxl', dtype=self.dtype)
        columnValue = []
        for column in df:
            values = []
            for value in df[column]:
                if pandas.isnull(value):
                    pass
                else:
                    values.append(value)
            columnValue.append(values)
        return columnValue

    def get_one_range_column_list(self, columnValues):
        datas = []
        for value in columnValues:
            data = random.choice(value)
            datas.append(data)
        return datas

    def random_date(self, dateStart, dateEnd):
        startTime = time.mktime(dateStart)
        endTime = time.mktime(dateEnd)
        t = random.randint(startTime, endTime)
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
        return date

    def write_msg_to_file(self, data):
        with open(conf.MSG_FILE, 'a+', encoding='utf-8') as file:
            log('write').debug('write data to file---->{}'.format(conf.MSG_FILE))
            file.write(data)
            file.write('\n')
        file.close()

    def read_msg_file_data(self):
        file = open(conf.MSG_FILE, 'r', encoding='utf-8')
        file_content = file.readlines()
        file.close()
        return file_content

    def bak_msg_file(self):
        if os.path.exists(conf.MSG_FILE):
            # 备份
            shutil.copy(conf.MSG_FILE, conf.MSG_BAK_FILE)
            os.remove(conf.MSG_FILE)
            log('os').debug('***bak file path:[{}]***'.format(conf.MSG_BAK_FILE))
        else:
            log('os').debug('***No need bak msg file***')
