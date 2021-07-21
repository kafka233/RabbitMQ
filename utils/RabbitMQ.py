# -*- coding:utf-8 -*-
# __author__ = 'kafka'

from utils.Logger import log
from conf import conf
import pika


class RabbitMQ(object):
    def __init__(self):
        self.ip = conf.server_ip
        self.queuesName = conf.queues_name
        self.credentials = pika.PlainCredentials(conf.user, conf.password)
        self.virtualHost = conf.virtual_host

    def msg_on_recv(self, ch, method, properties, msg):
        log('MQ').debug('[consumer] receive %s' % msg)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def connection(self):
        connectParams = pika.ConnectionParameters(host=self.ip, credentials=self.credentials,
                                                  virtual_host=self.virtualHost)
        try:
            connection = pika.BaseConnection(connectParams)
            return connection
        except pika.exception.AMQPError as e:
            log('MQ').error('AMQPError {0} , {1}'.format(self.ip, e))

    def declare_chanel(self, connection):
        channel = connection.channel()
        channel.queue_declare(queue=self.queuesName, durable=True)
        return channel

    def consumer(self, connection):
        channel = self.declare_chanel(connection)
        channel.basic_consume(queue=self.queuesName, on_message_callback=self.msg_on_recv, auto_ack=False)
        channel.start_consuming()
        log('MQ').debug('[consumer] waiting for msg')

    def producer(self, msg, connection):
        channel = self.declare_chanel(connection)
        channel.exchange_declare(exchange=self.queuesName)
        channel.basic_publish(exchange='', routing_key=self.queuesName, body=msg,
                              properties=pika.BasicProperties(delivery_mode=2))
        log('MQ').debug('[Producer] send %s' % msg)

    def close_connection(self, connection):
        connection.close()
