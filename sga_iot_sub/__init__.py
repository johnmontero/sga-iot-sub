# -*- coding: utf-8 -*-
import time
from sga_iot_sub.application.base import BaseAppService
from sga_iot_sub.infraestructure.service.messaging_protocol import MessagingProtocol

class App(BaseAppService):

    def __init__(self, context, broker, port, topic, username, password):
        self.context = context
        self.broker = broker
        self.port = port
        self.topic = topic
        self.username = username
        self.password = password

    def run(self):
        protocol = MessagingProtocol(
            broker=self.broker,
            port=self.port,
            topic=self.topic
        )
        protocol.connect(self.username, self.password)
        protocol.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "exiting"
            protocol.disconnect()
