from Player import *
from math import *
import Enemy
import pygame as pyg

class Ribbon(object):
        def __init__(self, playerOne, playerTwo):
      
            self.playOne = playerOne
            self.playTwo = playerTwo
            

        def getDistance(self):
            return sqrt(((self.playTwo[0] - self.playOne[0]) ** 2) + ((self.playTwo[1] - self.playOne[1]) ** 2))

        def getDamage(self):
            distance = getDistance(self.playOne, self.playTwo)
            distance = round(distance, 1)
            damage = distance
            enemy.health -= damage
            