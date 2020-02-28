#!/usr/bin/env python3

import random
from GameBoard import *
from CalculatePosition import *

class HiddenTreasures:

    x = 0
    y = 0

    gb = GameBoard()

    def calculateXPosition(self):
        x = random.randint(0,self.gb.getRows())
        return x

    def calculateYPosition(self):
        y = random.randint(0,self.gb.getColumns())
        return y