# -*- coding:utf-8 -*-
# __author__ = 'kafka'

from utils.RabbitMQ import RabbitMQ
from utils.LogDir import LogDir
from conf import conf
from utils.MSG import MSG_ENTER
from utils.common import *
from utils.LogDir import log
from utils.ReadData import ReadData
from tqdm import tqdm
import time

""" 发送入职消息 """


@timefn
def insert_mq_enter():
    print('***运行开始！***')
    LogDir().log_path()
    # 备份文件
    ReadData().bak_msg_file()
    # 连接MQ
    log('start').info('*' * 20 + 'Start insert_mq_enter!' + '*' * 20)
    columnValues = ReadData().read_column_value()
    connection = RabbitMQ().connection()
    # 发送消息
    try:
        if conf.sleepTime == 0:
            for i in tqdm(range(conf.employee_id_begin, conf.employee_id_begin + conf.insert_number, 1),
                          desc='Processing'):
                msg = MSG_ENTER(columnValues, i).msg()
                RabbitMQ().producer(msg, connection)
                time.sleep(0.01)
        else:
            for i in tqdm(range(conf.employee_id_begin, conf.employee_id_begin + conf.insert_number, 1),
                          desc='Processing'):
                msg = MSG_ENTER(columnValues, i).msg()
                RabbitMQ().producer(msg, connection)
    finally:
        connection.close()
        log('end').info('*' * 20 + 'End insert_mq_enter!' + '*' * 20)
        print('***运行结束***')


if __name__ == '__main__':
    insert_mq_enter()
