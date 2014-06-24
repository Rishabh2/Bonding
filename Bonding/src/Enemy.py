import Player
from math import *

class Enemy(object):
    def __init__(self, health, damageDealer, speed, point):
        '''
        Constructor
        '''
        self.health = health
        self.damage = damageDealer
        self.speed = speed
        self.enemyPoint = point
    def getDistance(p1, p2):
        return sqrt(((p2.getX() - p1.getX()) ** 2) + ((p2.getY() - p1.getY()) ** 2))
    
    def move(self, speed, player1, player2):
        distanceToP1 = getDistance(self, player1)
        distanceToP2 = getDistance(self, player2)
        if distanceToP1 < distanceToP2:
            pass
        else:
            pass    