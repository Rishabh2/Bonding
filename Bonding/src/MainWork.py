import Enemy
import Player
import Ribbon
import random
import Floor
import pygame as pyg
pyg.init()

screenWidth = 1280
screenHeight = 720
Player.health = 100
FPS = 60

floor = Floor.Floor()
floor.printgrid()

def mainLoop():
    pass