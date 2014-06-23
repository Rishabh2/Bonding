import Enemy
import Player
import Ribbon
import random
import Floor
import Room
import pygame as pyg
pyg.init()

screenWidth = 1280
screenHeight = 720
Player.health = 100
FPS = 60

screen = pyg.display.set_mode([screenWidth, screenHeight])
pyg.display.set_caption("Map Test")
floor = Floor.Floor(10,10)
for row in range(len(floor.rooms)):
    for col in range(len(floor.rooms[row])):
        floor.rooms[row][col].mapdraw(row, col, 65, 10, screen)
        
pyg.display.update()
pyg.time.delay(3000)
def mainLoop():
    pass