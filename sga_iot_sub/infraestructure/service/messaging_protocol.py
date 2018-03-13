# -*- coding: utf-8 -*-
import time
import dependency_injector.containers as containers
import dependency_injector.providers as providers

import paho.mqtt.client as mqtt

CLIENT_NAME = "sga-iot-sub"

class Protocol(object):
    """
    Protocol is a heart of every MessagingProtocol. Protocol is a very common term and could be
    implemented in very different ways.
    """

class MQTTProtocol(Protocol):
    """MQTTProtocol protocol."""

    def __init__(self, broker, port, topic):
        self._broker = broker
        self._port = port
        self._topic = topic
        self._client = mqtt.Client(CLIENT_NAME)
        self._connected = False

    def _on_connect(self, client, userdata, flags, rc):
        if rc != 0:
            print("Connection failed")
            return

        print("Connected to broker: {}:{}".format(self._broker, self._port))
        self._connected = True

    def _on_message(self, client, userdata, message):
        self.on_message(self, userdata, message)

    def connect(self, username, password):
        self._client.username_pw_set(username, password=password)
        self._client.on_connect= self._on_connect
        self._client.on_message = self._on_message
        self._client.subscribe(self._topic)

    def start(self):
        self._client.loop_start()    #start the loop

        while self._connected != True:    #Wait for connection
            time.sleep(0.1)

    def on_message(self, userdata, message):
        print "Message received: "  + message.payload

    def disconnect(self):
        self._client.disconnect()
        self._client.loop_stop()
        self._connected = False


class AMQPProtocol(Protocol):
    """AMQ protocol."""


class RabbitMQProtocol(Protocol):
    """RabbitMQ protocol."""


class Protocols(containers.DeclarativeContainer):
    """IoC container of protocol providers."""

    mqtt = providers.Factory(MQTTProtocol)

    amq = providers.Factory(MQTTProtocol)

    rabbitmq = providers.Factory(RabbitMQProtocol)


class MessagingProtocol(object):
    """ Messaging Protocol for comunication with sensor IOT. """

    def __init__(self, broker, port, topic):
        # Protocol is injected
        self._protocol = Protocols.mqtt(broker, port, topic)

    def connect(self, username, password):
        if not self._protocol._connected:
            self._protocol.connect(username, password)

    def disconnect(self):
        if self._protocol._connected:
            self._protocol.disconnect()

    def start(self):
        if not self._protocol._connected:
            self._protocol.start()
