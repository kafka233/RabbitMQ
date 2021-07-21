# -*- coding:utf-8 -*-
# __author__ = 'kafka'

import os
import datetime

#rabbitMQ
server_ip = '10.0.12.85'
queues_name = 'ODS_ZHR2_001'
virtual_host = 'VHOST_SHR'
user = 'admin'
password = 'asdasd'

#插入MQ数量
insert_number = 1
#发送消息时间间隔
sleepTime = 0
#员工ID起始范围
employee_id_begin = 8400000
#随机生成出生年月起始范围
birthday_start = (1980,1,1,0,0,0,0,0,0)
birthday_end = (2000,12,31,23,59,59,0,0,0)
#随机生成入职日期起始范围
enter_start = (2000,1,1,0,0,0,0,0,0)
enter_end = (2020,6,31,23,59,59,0,0,0)
#随机生成离职日期时间
leave_start = (2021,1,1,0,0,0,0,0,0)
leave_end = (2021,6,31,23,59,59,0,0)
#领导审批离职日期
approvel_date = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')

#日志
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_LEVEL = 'info'
LOG_STREAM_LEVEL = 'error'
LOG_FILE_LEVEL = 'debug'
LOG_FILE_NAME = os.path.join(BASE_PATH,'log',datetime.datetime.now().strftime('%m%d%H') + '.txt')

#文件路径
FILE_PATH = os.path.join(BASE_PATH,'cong','data.xlsx')
MSG_FILE = os.path.join(BASE_PATH,'data','msg.txt')
MSG_BAK_FILE = os.path.join(BASE_PATH,'bak','msg-bak' + datetime.datetime.now().strftime('%m%d%H%M%S') + '.txt')