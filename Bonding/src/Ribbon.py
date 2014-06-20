from Player import *
from math import *
from zellegraphics import *


def ribbonAttack(p1, p2):
    ribbon = Line(p1, p2)
    ribbon.setOutline("red")
    ribbon.setFill("red")


def getDistance(p1, p2):
    return sqrt(((p2.getX() - p1.getX()) ** 2) + ((p2.getY() - p1.getY()) ** 2))

def getDamage(p1, p2):
    distance = getDistance(p1, p2)
    distance = round(distance, 1)
    damage = 0
    enemy.health -= damage