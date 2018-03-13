# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class BaseAppService():
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        raise NotImplementedError
