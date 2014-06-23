import Enemy
import Player
import Ribbon
import random
import Floor
import Room
import pygame as pyg
from pygame.locals import *
pyg.init()

screenWidth = 1280
screenHeight = 720
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
playerImage = pyg.image.load("Player.png")

screen = pyg.display.set_mode([screenWidth, screenHeight])
pyg.display.set_caption("Map Test")
floor = Floor.Floor(roomRows, roomCols, tileRows, tileCols)
playerPoint = (screenWidth//2 + 50, screenHeight//2 + 75/2)
screen.blit(playerImage, (playerPoint[0] - 50, playerPoint[1] - 72/2))
player = Player.Player(100, 1, screenWidth, screenHeight)

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
        screen.blit(playerImage, (player.playerPoint[0] - 50, player.playerPoint[1] - 72/2))
        pyg.display.update()
    
mainLoop()
