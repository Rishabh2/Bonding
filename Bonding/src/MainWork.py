from Enemy import *
from Player import *
from Ribbon import *
from random import *
import pygame as pyg
pyg.init()

screenWidth = 1280
screenHeight = 720
Player.health = 100
FPS = 60
Enemy.health = randrange(1, 10)
print(Enemy.health)


#event loop