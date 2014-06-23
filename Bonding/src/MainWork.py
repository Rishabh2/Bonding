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
roomRows = 10
roomCols = 10
tileRows = 7
tileCols = 12
tileSize = 100
totalwidth = tileSize * tileCols
totalheight = tileSize * tileRows
xoffset = (screenWidth - totalwidth) / 2
yoffset = (screenHeight - totalheight) / 2
tileImage = pyg.image.load("Tile.png")

screen = pyg.display.set_mode([screenWidth, screenHeight])
pyg.display.set_caption("Map Test")
floor = Floor.Floor(roomRows, roomCols, tileRows, tileCols)

def drawBorder():
    pyg.draw.rect(screen, pyg.Color("white"), pyg.Rect(xoffset, yoffset, totalwidth, totalheight))
    
def mainLoop():
    while True:
        events = pyg.event.get()
        for e in events:
            if e.type == pyg.QUIT:
                return
        screen.fill([0, 0, 0])
        drawBorder()
        for row in range(tileRows):
            for col in range(tileCols):
                screen.blit(tileImage, [xoffset + col * tileSize, yoffset + row * tileSize])
        pyg.display.update()
    
mainLoop()
