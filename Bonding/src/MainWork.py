import Enemy
import Player
import Ribbon
import random
import Floor
import Room
from math import *

# all pygame functions
import pygame as pyg
from pygame.locals import *
pyg.init()

screenWidth = 1300
screenHeight = 800
FPS = 60
roomRows = 10
roomCols = 10
tileRows = 8
tileCols = 15
tileSize = 75
playerHeight = 75
playerWidth = 50
totalwidth = tileSize * tileCols
totalheight = tileSize * tileRows
xoffset = (screenWidth - totalwidth) / 2
yoffset = (screenHeight - totalheight) * 3 / 4
mapSize = 120
roomSize = mapSize / roomRows
mapBuffer = 10
tileImage = pyg.image.load("Tile.png")
playerImage = pyg.image.load("Player.png")
player2Image = pyg.image.load("Player.png")
screen = pyg.display.set_mode([screenWidth, screenHeight])
pyg.display.set_caption("Map Test")
floor = Floor.Floor(roomRows, roomCols, tileRows, tileCols)
playerPoint = (screenWidth // 2 + 100 // 2, screenHeight // 2 + 75)
screen.blit(playerImage, (playerPoint[0] - playerWidth / 2, playerPoint[1] - playerHeight / 2))
screen.blit(player2Image, (playerPoint[0] - playerWidth / 2, playerPoint[1] - playerHeight / 2))
player = Player.Player(100, 10, (screenWidth * 1 / 4, screenHeight), 100, True)
player2 = Player.Player(100, 10, (screenWidth * 3 / 4, screenHeight), 100, True)
ribbon = Ribbon.Ribbon(player, player2, 1)
def drawBorder():
    pyg.draw.rect(screen, pyg.Color("white"), pyg.Rect(xoffset, yoffset, totalwidth, totalheight))
    
def mainLoop():
    while True:
        events = pyg.event.get()
        for e in events:
            if e.type == pyg.QUIT:
                return
            if e.type == pyg.KEYDOWN:
                if e.key == pyg.K_SPACE:
                    toDeal = (player.limit - player.health) / 2
                    if toDeal > player2.health:
                        player2.damageTake(toDeal)
                        player.addHealth(toDeal)
                if e.key == pyg.K_KP0:
                    toDeal = (player2.limit - player2.health) / 2
                    if toDeal > player.health:
                        player.damageTake(toDeal)
                        player2.addHealth(toDeal)
        screen.fill([0, 0, 0])
        drawBorder()
        for row in range(tileRows):
            for col in range(tileCols):
                screen.blit(tileImage, [xoffset + col * tileSize, yoffset + row * tileSize])
        screen.blit(playerImage, (player.playerPoint[0] - playerWidth / 2, player.playerPoint[1] - playerHeight / 2))
        screen.blit(player2Image, (player2.playerPoint[0] - playerWidth / 2, player2.playerPoint[1] - playerHeight / 2))
        if player.living == True:
            if player2.living == True:
                # deals with damage and all
                ribbon = pyg.draw.line(screen, Color('red'), player.playerPoint, player2.playerPoint, 3)
        
        
            # player one handling
        if player.living == True:
            if (pyg.key.get_pressed()[K_w]):
                player.move(0, -1 * player.speed)
            if (pyg.key.get_pressed()[K_s]):
                player.move(0, 1 * player.speed)
            if (pyg.key.get_pressed()[K_a]):
                player.move(-1 * player.speed, 0)
            if (pyg.key.get_pressed()[K_d]):
                player.move(1 * player.speed, 0)
            while player.playerPoint[0] - playerWidth / 2 < xoffset:
                player.move(1, 0)
            while player.playerPoint[0] + playerWidth / 2 > totalwidth + xoffset:
                player.move(-1, 0)
            while player.playerPoint[1] - playerHeight / 2 < yoffset:
                player .move(0, 1)
            while player.playerPoint[1] + playerHeight / 2 > totalheight + yoffset:
                player.move(0, -1)
        else:
            player.playerPoint(screenWidth * 1 / 4, screenHeight)
        
            
            # player two handling
        if player2.living == True:
            if (pyg.key.get_pressed()[K_UP]):
                 player2.move(0, -1 * player2.speed)
            if (pyg.key.get_pressed()[K_DOWN]):
                player2.move(0, 1 * player2.speed)
            if (pyg.key.get_pressed()[K_LEFT]):
                player2.move(-1 * player2.speed, 0)
            if (pyg.key.get_pressed()[K_RIGHT]):
                player2.move(1 * player2.speed, 0)
            while player2.playerPoint[0] - playerWidth / 2 < xoffset:
                player2.move(1, 0)
            while player2.playerPoint[0] + playerWidth / 2 > totalwidth + xoffset:
                player2.move(-1, 0)
            while player2.playerPoint[1] - playerHeight / 2 < yoffset:
                player2.move(0, 1)
            while player2.playerPoint[1] + playerHeight / 2 > totalheight + yoffset:
                player2.move(0, -1)
        else:
            player2.playerPoint(screenWidth * 3 / 4, screenHeight)

        for y in range(roomRows):
            for x in range(roomCols):
                if floor.rooms[y][x].beenVisited:
                    if not floor.rooms[y][x].doors[0]:
                        pyg.draw.line(screen, [255, 255, 255], (x * roomSize + (screenWidth - mapSize) / 2, y * roomSize + mapBuffer), ((x + 1) * roomSize + (screenWidth - mapSize) / 2, y * roomSize + mapBuffer))
                    if not floor.rooms[y][x].doors[1]:
                        pyg.draw.line(screen, [255, 255, 255], ((x + 1) * roomSize + (screenWidth - mapSize) / 2, y * roomSize + mapBuffer), ((x + 1) * roomSize + (screenWidth - mapSize) / 2, (y + 1) * roomSize + mapBuffer))
                    if not floor.rooms[y][x].doors[2]:
                        pyg.draw.line(screen, [255, 255, 255], ((x + 1) * roomSize + (screenWidth - mapSize) / 2, (y + 1) * roomSize + mapBuffer), ((x) * roomSize + (screenWidth - mapSize) / 2, (y + 1) * roomSize + mapBuffer))
                    if not floor.rooms[y][x].doors[3]:
                        pyg.draw.line(screen, [255, 255, 255], (x * roomSize + (screenWidth - mapSize) / 2, (y + 1) * roomSize + mapBuffer), (x * roomSize + (screenWidth - mapSize) / 2, y * roomSize + mapBuffer))

        pyg.display.update()

mainLoop()
