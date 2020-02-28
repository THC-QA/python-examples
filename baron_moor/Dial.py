#!/usr/bin/env python3

from PlayerPosition import PlayerPosition
from Movement import *
from GameBoard import GameBoard

class Dial:

    def north(self,n):
        if n < PlayerPosition.getColumns(self):
            n+=1
        return n
              
    def east(self,e):
        if e < PlayerPosition.getRows(self):
            e+=1
        return e

    def south(self,s):
        if s > 0:
            s-=1
        return s
              
    def west(self,w):
        if w > 0:
            w-=1
        return w