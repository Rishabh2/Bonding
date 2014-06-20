'''
Shawn Leedy
'''

from Player import *
from math import *
from zellegraphics import *



ribbon = Line(pointOne, pointTwo)
ribbon.setOutline("red")
ribbon.setFill("red")
#TODO: find a way to set thickness

def getDistance(p1, p2):
    return sqrt(((p2.getX() - p1.getX()) ** 2) + ((p2.getY() - p1.getY()) ** 2))

def getDamage(p1, p2):
    distance = getDistance(p1, p2)
    damage = 0
    player.health -= damage