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
tileRows = 6
tileCols = 13
tileSize = 75
totalRows = 8
totalCols = 15
playerHeight = 75
playerWidth = 50
tileWidth = tileSize * tileCols
tileHeight = tileSize * tileRows
totalWidth = tileSize * totalCols
totalHeight = tileSize * totalRows
xoffset = (screenWidth - totalWidth) / 2
yoffset = (screenHeight - totalHeight) * 3 / 4
mapSize = 120
roomSize = mapSize / roomRows
mapBuffer = 10
tileImage = pyg.image.load("Tile.png")
playerImage = pyg.image.load("Player.png")
player2Image = pyg.image.load("Player.png")
cornerImage = pyg.image.load("Corner.png")
cornerImage2 = pyg.image.load("Corner2.png")
cornerImage3 = pyg.image.load("Corner3.png")
cornerImage4 = pyg.image.load("Corner4.png")
CDoorImage = pyg.image.load("CDoor.png")
CDoorImage2 = pyg.image.load("CDoor2.png")
wallImage = pyg.image.load("Wall.png")
vwallImage = pyg.image.load("VWall.png")
screen = pyg.display.set_mode([screenWidth, screenHeight])
pyg.display.set_caption("Map Test")
floor = Floor.Floor(roomRows, roomCols, tileRows, tileCols)
playerPoint = (screenWidth // 2 + 100 // 2, screenHeight // 2 + 75)
screen.blit(playerImage, (playerPoint[0] - playerWidth / 2, playerPoint[1] - playerHeight / 2))
screen.blit(player2Image, (playerPoint[0] - playerWidth / 2, playerPoint[1] - playerHeight / 2))
player = Player.Player(100, 10, (screenWidth * 1 / 4, screenHeight), 100, True)
player2 = Player.Player(100, 10, (screenWidth * 3 / 4, screenHeight), 100, True)
ribbon = Ribbon.Ribbon(player, player2, 1)
def spawn():
    player.playerPoint = (screenWidth * 1 / 4, screenHeight)
    player2.playerPoint = (screenWidth * 3 / 4, screenHeight)
    
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
        for row in range(tileRows):
            for col in range(tileCols):
                screen.blit(tileImage, (xoffset + (col + 1) * tileSize, yoffset + (row + 1) * tileSize))
        screen.blit(cornerImage, (xoffset, yoffset))
        screen.blit(cornerImage2, (xoffset + tileSize + tileWidth, yoffset))
        screen.blit(cornerImage3, (xoffset + tileSize + tileWidth, yoffset + tileSize + tileHeight))
        screen.blit(cornerImage4, (xoffset, yoffset + tileSize + tileHeight))
        for i in range(tileCols):
            screen.blit(wallImage, (xoffset + tileSize * (i + 1), yoffset))
            screen.blit(wallImage, (xoffset + tileSize * (i + 1), yoffset + tileSize + tileHeight))
        for i in range(tileRows):
            screen.blit(vwallImage, (xoffset, yoffset + tileSize * (i + 1)))
            screen.blit(vwallImage, (xoffset + tileSize + tileWidth, yoffset + tileSize * (i + 1)))
        if floor.getCurrentRoom().doors[0]:
            screen.blit(CDoorImage, (xoffset + tileSize + tileSize * (tileCols // 2), yoffset))
        if floor.getCurrentRoom().doors[1]:
            screen.blit(CDoorImage2, (xoffset + tileSize + tileWidth, yoffset + tileSize * (tileRows // 2)))
        if floor.getCurrentRoom().doors[2]:
            screen.blit(CDoorImage, (xoffset + tileSize + tileSize * (tileCols // 2), yoffset + tileSize + tileHeight))
        if floor.getCurrentRoom().doors[3]:
            screen.blit(CDoorImage2, (xoffset, yoffset + tileSize * (tileRows // 2)))
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
                if player.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 and player.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 and player.playerPoint[1] <= tileSize + playerHeight / 2 and floor.getCurrentRoom().doors[0]:
                    floor.currentRoom[0] -= 1
                    spawn()
            if (pyg.key.get_pressed()[K_s]):
                player.move(0, 1 * player.speed)
                if player.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 and player.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 and player.playerPoint[1] >= tileSize + tileHeight - playerHeight / 2 and floor.getCurrentRoom().doors[2]:
                    floor.currentRoom[0] += 1
                    spawn()
            if (pyg.key.get_pressed()[K_a]):
                player.move(-1 * player.speed, 0)
                if player.playerPoint[1] > totalHeight / 2 - 100 / 2 + playerHeight / 2 and player.playerPoint[1] < totalHeight / 2 + 100 / 2 - playerHeight / 2 and player.playerPoint[0] <= tileSize + playerWidth / 2 and floor.getCurrentRoom().doors[3]:
                    floor.currentRoom[1] -= 1
                    spawn()
            if (pyg.key.get_pressed()[K_d]):
                player.move(1 * player.speed, 0)
                if player.playerPoint[1] > totalHeight / 2 - 100 / 2 + playerHeight / 2 and player.playerPoint[1] < totalHeight / 2 + 100 / 2 - playerHeight / 2 and player.playerPoint[0] >= tileSize + tileWidth - playerWidth / 2 and floor.getCurrentRoom().doors[1]:
                    floor.currentRoom[1] += 1
                    spawn()
            while player.playerPoint[0] - playerWidth / 2 < xoffset + tileSize:
                player.move(1, 0)
            while player.playerPoint[0] + playerWidth / 2 > xoffset + tileSize + tileWidth:
                player.move(-1, 0)
            while player.playerPoint[1] - playerHeight / 2 < yoffset + tileSize:
                player .move(0, 1)
            while player.playerPoint[1] + playerHeight / 2 > yoffset + tileSize + tileHeight:
                player.move(0, -1)
        
            
            # player two handling
        if player2.living == True:
            if (pyg.key.get_pressed()[K_UP]):
                 player2.move(0, -1 * player2.speed)
                 if player2.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 and player2.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 and player2.playerPoint[1] <= tileSize + playerHeight / 2 and floor.getCurrentRoom().doors[0]:
                    floor.currentRoom[0] -= 1
                    spawn()
            if (pyg.key.get_pressed()[K_DOWN]):
                player2.move(0, 1 * player2.speed)
                if player2.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 and player2.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 and player2.playerPoint[1] >= tileSize + tileHeight - playerHeight / 2 and floor.getCurrentRoom().doors[2]:
                    floor.currentRoom[0] += 1
                    spawn()
            if (pyg.key.get_pressed()[K_LEFT]):
                player2.move(-1 * player2.speed, 0)
                if player2.playerPoint[1] > totalHeight / 2 - 100 / 2 + playerHeight / 2 and player2.playerPoint[1] < totalHeight / 2 + 100 / 2 - playerHeight / 2 and player2.playerPoint[0] <= tileSize + playerWidth / 2 and floor.getCurrentRoom().doors[3]:
                    floor.currentRoom[1] -= 1
                    spawn()
            if (pyg.key.get_pressed()[K_RIGHT]):
                player2.move(1 * player2.speed, 0)
                if player2.playerPoint[1] > totalHeight / 2 - 100 / 2 + playerHeight / 2 and player2.playerPoint[1] < totalHeight / 2 + 100 / 2 - playerHeight / 2 and player2.playerPoint[0] >= tileSize + tileWidth - playerWidth / 2 and floor.getCurrentRoom().doors[1]:
                    floor.currentRoom[1] += 1
                    spawn()
            while player2.playerPoint[0] - playerWidth / 2 < xoffset + tileSize:
                player2.move(1, 0)
            while player2.playerPoint[0] + playerWidth / 2 > xoffset + tileSize + tileWidth:
                player2.move(-1, 0)
            while player2.playerPoint[1] - playerHeight / 2 < yoffset + tileSize:
                player2.move(0, 1)
            while player2.playerPoint[1] + playerHeight / 2 > yoffset + tileSize + tileHeight:
                player2.move(0, -1)

        for y in range(roomRows):
            for x in range(roomCols):
                if floor.rooms[y][x].beenVisited:
                    if (x == floor.currentRoom[1] and y == floor.currentRoom[0]):
                        pyg.draw.rect(screen, pyg.Color("yellow"), Rect((x * roomSize + (screenWidth - mapSize) / 2, y * roomSize + mapBuffer), (roomSize, roomSize)))
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
