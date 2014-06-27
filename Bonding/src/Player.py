class Player(object):
    '''
    Class for the player objects
    '''
    import Ribbon
    import pygame
    
    def __init__(self, health, speed, point, healthLimit, isLiving):
        self.health = health
        self.speed = speed
        self.playerPoint = point
        self.limit = healthLimit
        self.living = isLiving
        self.dir = 2
        self.frame = 1
        self.dirs = [3, 2, 0, 1]
        
    def draw(self, surface):
        self.draw(screen)
    
    def move(self, dx, dy, dir):
        self.playerPoint = (self.playerPoint[0] + dx, self.playerPoint[1] + dy)
        self.dir = self.dirs[dir]
        if self.frame != 2:
            self.frame == 2
        else:
            self.frame == 0
        return self.playerPoint
    def addHealth(self, health):
        self.health += health
        if self.health > self.limit:
            self.health = self.limit
        self.health = round(self.health, 0)
            
