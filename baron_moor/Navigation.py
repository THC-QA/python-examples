#!/usr/bin/env python3

import math

class Navigation:

    def __init__(self, pX, pY, tX, tY):
        self.pX = pX
        self.pY = pY
        self.tX = tX
        self.tY = tY

    def getpX(self):
        return self.pX

    def getpY(self):
        return self.pY

    def gettX(self):
        return self.tX
    
    def gettY(self):
        return self.tY

    def setpX(self,x):
        self.pX = x

    def setpY(self,y):
        self.pY = y

    def settX(self,x):
        self.tX = x

    def settY(self,y):
        self.tY = y

    def getAllPosition(self):
        self.s = ("Navigation{" +
                "pX=" + self.pX +
                ", pY=" + self.pY +
                ", tX=" + self.tX +
                ", tY=" + self.tY +
                "}")
        return self.s

    def calculateResultant(self):
        self.xDiff = int(math.pow((self.pX - self.tX), 2))
        self.yDiff = int(math.pow((self.pY - self.tY), 2))
        self.summed = int(self.xDiff + self.yDiff)
        
        return round(math.sqrt(self.summed),2)