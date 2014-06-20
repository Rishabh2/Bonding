from Enemy import *
from Player import *
from Ribbon import *
from zellegraphics import *
from random import *

screenWidth = 1280
screenHeight = 720
Player.health = 100
Enemy.health = randrange(1, 10)
print(Enemy.health)
win = GraphWin("RibBonding", screenWidth, screenHeight)