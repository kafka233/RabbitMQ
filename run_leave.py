# -*- coding:utf-8 -*-
# __author__ = 'kafka'

from utils.RabbitMQ import RabbitMQ
from utils.LogDir import LogDir
from utils.MSG import MSG_LEAVE
from utils.common import *
from utils.Logger import log
from tqdm import tqdm

""" 发送离职消息 """


@timefn
def insert_mq_leave():
    print('***Start!***')
    LogDir().log_path()
    # 连接MQ
    log('start').info('*' * 20 + 'Start insert_mq_leave!' + '*' * 20)
    connection = RabbitMQ().connection()
    msg = MSG_LEAVE().msg_file()
    try:
        for m in tqdm(msg, desc='Processing'):
            RabbitMQ().producer(m, connection)
    finally:
        connection.close()
        log('end').info('*' * 20 + 'End insert_mq_leave!' + '*' * 20)
        print('***End!***')


if __name__ == '__main__':
    insert_mq_leave()
