import Enemy
import Player
import Ribbon
import random
import Floor
import Room
import Calculator
from math import *
import Bullet
import sys

# all pygame functions
import pygame as pyg
from pygame.locals import *
pyg.init()

healthFont = pyg.font.SysFont("Arial", 50)
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
backstabMod = .9  # must be <1, how much damage you keep per backstab
killBonus = 1.05
tileWidth = tileSize * tileCols
tileHeight = tileSize * tileRows
totalWidth = tileSize * totalCols
totalHeight = tileSize * totalRows
xoffset = (screenWidth - totalWidth) / 2
yoffset = (screenHeight - totalHeight) * 3 / 4
mapSize = 120
roomSize = mapSize / roomRows
mapBuffer = 10
enemyRadius = 15
bulletSize = 10
floorNum = 1
# image assigning
playerBuffer = 6
playerWidth = 27
playerHeight = 32
tileImage = pyg.image.load("Tile.png")
playerImage = pyg.image.load("Player1.png")
player2Image = pyg.image.load("Player2.png")
cornerImage = pyg.image.load("Corner.png")
cornerImage2 = pyg.image.load("Corner2.png")
cornerImage3 = pyg.image.load("Corner3.png")
cornerImage4 = pyg.image.load("Corner4.png")
CDoorImage = pyg.image.load("CDoor.png")
CDoorImage2 = pyg.image.load("CDoor2.png")
wallImage = pyg.image.load("Wall.png")
vwallImage = pyg.image.load("VWall.png")
bossImage = pyg.image.load("boss1.png")
redImage = pyg.image.load("red.png")
greenImage = pyg.image.load("green.png")
bulletImage = pyg.image.load("Bullet.png")
screen = pyg.display.set_mode([screenWidth, screenHeight])
calc = Calculator.Calculator()

floor = Floor.Floor(roomRows, roomCols, tileRows, tileCols)
player = Player.Player(100, 10, (screenWidth * 1 / 4, screenHeight), 100, True)
player2 = Player.Player(100, 10, (screenWidth * 3 / 4, screenHeight), 100, True)

ribbon = Ribbon.Ribbon()

def end():
    draw()
    red = 0
    while red <= 150:
        redImage.set_alpha(red)
        screen.blit(redImage, (0, 0))
        pyg.display.update()
        red += 1
    sys.exit()
    
def spawn():
    player.playerPoint = (screenWidth * 1 / 4 + xoffset, screenHeight / 2 + yoffset)
    player2.playerPoint = (screenWidth * 3 / 4 + xoffset, screenHeight / 2 + yoffset)
    floor.getCurrentRoom().beenVisited = True
    draw()
    pyg.time.delay(500)
    
def draw():
    pyg.display.set_caption("Bonding: Floor " + str(floorNum))
    screen.fill([0, 0, 0])
     
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
    
    screen.blit(healthFont.render(str(player.health), 1, [255 - 255 * player.health / player.limit, 255 * player.health / player.limit, 0]), (xoffset, yoffset / 3))
    screen.blit(healthFont.render(str(player2.health), 1, [255 - 255 * player2.health / player2.limit, 255 * player2.health / player2.limit, 0]), (xoffset + tileWidth + tileSize, yoffset / 3))
    
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
         
    pyg.draw.line(screen, Color('red'), player.playerPoint, player2.playerPoint, 3)
            
    screen.blit(playerImage, (player.playerPoint[0] - playerWidth / 2, player.playerPoint[1] - playerHeight / 2), (player.frame * (playerWidth + playerBuffer), player.dir * playerHeight, playerWidth, playerHeight))
    screen.blit(player2Image, (player2.playerPoint[0] - playerWidth / 2, player2.playerPoint[1] - playerHeight / 2), (player2.frame * (playerWidth + playerBuffer), player2.dir * playerHeight, playerWidth, playerHeight))
        
    for enemy in floor.getCurrentRoom().enemies:
        if not enemy.isBullet():
            screen.blit(bossImage, (enemy.point[0], enemy.point[1]))
        else:
            screen.blit(bulletImage, (enemy.point[0], enemy.point[1]))
    
    pyg.display.update()
    
def act():
    # player one handling
    if (pyg.key.get_pressed()[K_w]):
        player.move(0, -1 * player.speed, 0)
        if player.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 + xoffset and player.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 + xoffset and player.playerPoint[1] <= tileSize + playerHeight / 2 + yoffset and floor.getCurrentRoom().doors[0] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[0] -= 1
            spawn()
    if (pyg.key.get_pressed()[K_s]):
        player.move(0, 1 * player.speed, 2)
        if player.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 + xoffset and player.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 + xoffset and player.playerPoint[1] >= tileSize + tileHeight - playerHeight / 2 + yoffset and floor.getCurrentRoom().doors[2] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[0] += 1
            spawn()
    if (pyg.key.get_pressed()[K_a]):
        player.move(-1 * player.speed, 0, 3)
        if player.playerPoint[1] > totalHeight / 2 - 150 / 2 + playerHeight / 2 + yoffset and player.playerPoint[1] < totalHeight / 2 + 150 / 2 - playerHeight / 2 + yoffset and player.playerPoint[0] <= tileSize + playerWidth / 2 + xoffset and floor.getCurrentRoom().doors[3] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[1] -= 1
            spawn()
    if (pyg.key.get_pressed()[K_d]):
        player.move(1 * player.speed, 0, 1)
        if player.playerPoint[1] > totalHeight / 2 - 150 / 2 + playerHeight / 2 + yoffset and player.playerPoint[1] < totalHeight / 2 + 150 / 2 - playerHeight / 2 + yoffset and player.playerPoint[0] >= tileSize + tileWidth - playerWidth / 2 + xoffset and floor.getCurrentRoom().doors[1] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[1] += 1
            spawn()
    if not (pyg.key.get_pressed()[K_w] or pyg.key.get_pressed()[K_s] or pyg.key.get_pressed()[K_a] or pyg.key.get_pressed()[K_d]):
        player.frame = 1
    while player.playerPoint[0] - playerWidth / 2 < xoffset + tileSize:
        player.move(1, 0, 3)
    while player.playerPoint[0] + playerWidth / 2 > xoffset + tileSize + tileWidth:
        player.move(-1, 0, 1)
    while player.playerPoint[1] - playerHeight / 2 < yoffset + tileSize:
        player .move(0, 1, 0)
    while player.playerPoint[1] + playerHeight / 2 > yoffset + tileSize + tileHeight:
        player.move(0, -1, 2)
        
    # player two handling
    if (pyg.key.get_pressed()[K_UP]):
         player2.move(0, -1 * player2.speed, 0)
         if player2.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 + xoffset and player2.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 + xoffset and player2.playerPoint[1] <= tileSize + playerHeight / 2 + yoffset and floor.getCurrentRoom().doors[0] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[0] -= 1
            spawn()
    if (pyg.key.get_pressed()[K_DOWN]):
        player2.move(0, 1 * player2.speed, 2)
        if player2.playerPoint[0] > totalWidth / 2 - 75 / 2 + playerWidth / 2 + xoffset and player2.playerPoint[0] < totalWidth / 2 + 75 / 2 - playerWidth / 2 + xoffset and player2.playerPoint[1] >= tileSize + tileHeight - playerHeight / 2 + yoffset and floor.getCurrentRoom().doors[2] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[0] += 1
            spawn()
    if (pyg.key.get_pressed()[K_LEFT]):
        player2.move(-1 * player2.speed, 0, 3)
        if player2.playerPoint[1] > totalHeight / 2 - 150 / 2 + playerHeight / 2 + yoffset and player2.playerPoint[1] < totalHeight / 2 + 150 / 2 - playerHeight / 2 + yoffset and player2.playerPoint[0] <= tileSize + playerWidth / 2 + xoffset and floor.getCurrentRoom().doors[3] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[1] -= 1
            spawn()
    if (pyg.key.get_pressed()[K_RIGHT]):
        player2.move(1 * player2.speed, 0, 1)
        if player2.playerPoint[1] > totalHeight / 2 - 150 / 2 + playerHeight / 2 + yoffset and player2.playerPoint[1] < totalHeight / 2 + 150 / 2 - playerHeight / 2 + yoffset and player2.playerPoint[0] >= tileSize + tileWidth - playerWidth / 2 + xoffset and floor.getCurrentRoom().doors[1] and len(floor.getCurrentRoom().enemies) == 0:
            floor.currentRoom[1] += 1
            spawn()
    if not (pyg.key.get_pressed()[K_UP] or pyg.key.get_pressed()[K_DOWN] or pyg.key.get_pressed()[K_LEFT] or pyg.key.get_pressed()[K_RIGHT]):
        player2.frame = 1
    while player2.playerPoint[0] - playerWidth / 2 < xoffset + tileSize:
        player2.move(1, 0, 3)
    while player2.playerPoint[0] + playerWidth / 2 > xoffset + tileSize + tileWidth:
        player2.move(-1, 0, 1)
    while player2.playerPoint[1] - playerHeight / 2 < yoffset + tileSize:
        player2.move(0, 1, 0)
    while player2.playerPoint[1] + playerHeight / 2 > yoffset + tileSize + tileHeight:
        player2.move(0, -1, 2)
        
        
    # enemy handling
    for enemy in floor.getCurrentRoom().enemies:
        if enemy.move(player.playerPoint, player2.playerPoint):
            floor.getCurrentRoom().enemies.remove(enemy)
        else:
            if (not enemy.isBullet()) and calc.lineDistance(enemy.point, player.playerPoint, player2.playerPoint) < enemyRadius and calc.between(enemy.point, player.playerPoint, player2.playerPoint):
                ribbon.doDamage(player.playerPoint, player2.playerPoint, enemy)
                if enemy.health <= 0:
                    floor.getCurrentRoom().enemies.remove(enemy)
                    ribbon.damamod = ribbon.damamod * killBonus
                    if ribbon.damamod > 2:
                        ribbon.damamod = 1.5
                    if floor.currentRoom == floor.bossRoom:
                        floorNum += 1
                        # floor = Floor.Floor(roomRows, roomCols, tileRows, tileCols)
                        green = 0
                        while green <= 150:
                            greenImage.set_alpha(green)
                            screen.blit(greenImage, (0, 0))
                            pyg.display.update()
                            red += 1
                        draw()
            if calc.distance(player.playerPoint, enemy.point) < enemyRadius:
                player.addHealth(-enemy.damage)
                if enemy.isBullet():
                    floor.getCurrentRoom().enemies.remove(enemy)
            if calc.distance(player2.playerPoint, enemy.point) < enemyRadius:
                player2.addHealth(-enemy.damage)
                if enemy.isBullet():
                    floor.getCurrentRoom().enemies.remove(enemy)
            if not enemy.isBullet() and enemy.shoots and random.randrange(60) == 0:
                floor.getCurrentRoom().enemies.append(Bullet.Bullet(enemy.point, (player.playerPoint, player2.playerPoint)[random.randrange(1)], 10))
 
            
    if player.health <= 0:
        player.health = 0
  #      end()
    if player2.health <= 0:
        player2.health = 0
     #   end()
        
        
def mainLoop():
    while True:
        events = pyg.event.get()
        for e in events:
            if e.type == pyg.QUIT:
                return
            if e.type == pyg.KEYDOWN:
                if e.key == pyg.K_SPACE:
                    toDeal = (player.limit - player.health) / 2
                    if toDeal < player2.health:
                        player2.addHealth(-toDeal)
                        player.addHealth(toDeal)
                        ribbon.damamod = ribbon.damamod * backstabMod
                if e.key == pyg.K_KP0:
                    toDeal = (player2.limit - player2.health) / 2
                    if toDeal < player.health:
                        player.addHealth(-toDeal)
                        player2.addHealth(toDeal)
                        ribbon.damamod = ribbon.damamod * backstabMod
        act()
        draw()

spawn()
mainLoop()
