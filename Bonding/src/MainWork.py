import Enemy
import Player
import Ribbon
import random
import Floor
import Room

#all pygame functions
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
playerHeight = 100
playerWidth = 75
totalwidth = tileSize * tileCols
totalheight = tileSize * tileRows
xoffset = (screenWidth - totalwidth) / 2
yoffset = (screenHeight - totalheight) / 2
tileImage = pyg.image.load("Tile.png")
playerImage = pyg.image.load("Player.png")
player2Image = pyg.image.load("Player.png")
screen = pyg.display.set_mode([screenWidth, screenHeight])
pyg.display.set_caption("Map Test")
floor = Floor.Floor(roomRows, roomCols, tileRows, tileCols)
playerPoint = (screenWidth//2 + 100 // 2, screenHeight//2 + 75)
screen.blit(playerImage, (playerPoint[0] - 50, playerPoint[1] - 75/2))
screen.blit(player2Image, (playerPoint[0] - 50, playerPoint[1] - 75/2))
player = Player.Player(0, 0, 100, 10, screenWidth * 1 / 4, screenHeight, 100, True)
player2 = Player.Player(0, 0, 100, 10, screenWidth * 3 / 4, screenHeight, 100, True)
ribbon = Ribbon.Ribbon(player, player2)
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
        screen.blit(player2Image, (player2.playerPoint[0] - 50, player2.playerPoint[1] - 72/2))
        if player.living == True:
            if player2.living == True:
                #deals with damage and all
                ribbon = pyg.draw.line(screen, Color('red'), player.playerPoint, player2.playerPoint, 3)
        
        for e in events:
            #player one handling
            if player.living == True:
                if (pyg.key.get_pressed()[K_w]):
                    player.move(0, -1 * player.speed)
                if (pyg.key.get_pressed()[K_s]):
                    player.move(0, 1 * player.speed)
                if (pyg.key.get_pressed()[K_a]):
                    player.move(-1 * player.speed, 0)
                if (pyg.key.get_pressed()[K_d]):
                    player.move(1 * player.speed, 0)
                while player.playerPoint[0]  - playerWidth/2 - 12< xoffset:
                    player.move(1, 0)
                while player.playerPoint[0]  + playerWidth/2 - 13> totalwidth +  xoffset:
                    player.move(-1, 0)
                while player.playerPoint[1] - playerHeight/2 + 14 < yoffset:
                    player .move(0, 1)
                while player.playerPoint[1] + playerHeight/2 + 13 > totalheight + yoffset:
                    player.move(0, -1)
            else:
                player.playerPoint(screenWidth * 1 / 4, screenHeight)
            
            #player two handling
            if player2.living == True:
                if (pyg.key.get_pressed()[K_UP]):
                    player2.move(0, -1 * player2.speed)
                if (pyg.key.get_pressed()[K_DOWN]):
                    player2.move(0, 1 * player2.speed)
                if (pyg.key.get_pressed()[K_LEFT]):
                    player2.move(-1 * player2.speed, 0)
                if (pyg.key.get_pressed()[K_RIGHT]):
                    player2.move(1 * player2.speed, 0)
                while player2.playerPoint[0]  - playerWidth/2 - 12< xoffset:
                    player2.move(1, 0)
                while player2.playerPoint[0]  + playerWidth/2 - 13> totalwidth +  xoffset:
                    player2.move(-1, 0)
                while player2.playerPoint[1] - playerHeight/2 + 14 < yoffset:
                    player2.move(0, 1)
                while player2.playerPoint[1] + playerHeight/2 + 13 > totalheight + yoffset:
                    player2.move(0, -1)
            else:
                player2.playerPoint(screenWidth * 3 / 4, screenHeight)
        pyg.display.update()

mainLoop()