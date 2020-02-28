#!/usr/bin/env python3

import abc

class Movement(abc.ABC):

    @abc.abstractmethod
    def nort(self,n):
        pass

    @abc.abstractmethod
    def south(self,s):
        pass

    @abc.abstractmethod
    def west(self,w):
        pass

    @abc.abstractmethod
    def east(self,e):
        pass