from Player import *
from math import *
import Enemy
import pygame as pyg

class Ribbon(object):
        def __init__(self, playerOne, playerTwo):
      
            self.playOne = playerOne
            self.playTwo = playerTwo
            


        def getDistance(self):
            return sqrt(((self.playTwo.getX() - self.playOne.getX()) ** 2) + ((self.playTwo.getY() - self.playOne.getY()) ** 2))

        def getDamage(self):
            distance = getDistance(self.playOne, self.playTwo)
            distance = round(distance, 1)
            damage = distance
            enemy.health -= damage
            