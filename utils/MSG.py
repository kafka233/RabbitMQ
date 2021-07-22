# -*- coding:utf-8 -*-
# __author__ = 'kafka'

import random
import string
import json
from utils.ReadData import ReadData
from utils.Logger import log
from conf import conf

class MSG_ENTER(object):
    def __init__(self,columnValues,employeeId):
        self.data = ReadData().get_one_range_column_list(columnValues)
        self.employee_id = str(employeeId)

        self.employee_relation = self.data[0]
        self.employee_type = self.data[1]
        # todo

    def msg(self):
        msg = {
            "column1" : self.employee_id,
            "column2" : self.employee_relation,
            "column3" : self.employee_type
            # todo
        }
        return msg

class MSG_LEAVE(object):
    def __init__(self):
        self.resignation_date = ReadData().random_date(conf.leave_start,conf.leave_end)
        self.approval_date = conf.approvel_date

    def msg_file(self):
        file = open(conf.MSG_FILE,'r',encoding='utf-8')
        file_content = file.readlines()
        file.close()
        newContent = []
        for line in file_content:
            #字符串转换成dic
            line = eval(line)
            updateI = {
                'datum' : self.resignation_date,
                'dat02' : self.approval_date
            }
            line.update(updateI)
            log('msg_leave').info(line)
            line = json.dumps(line)
            newContent.append(line)
        return newContent