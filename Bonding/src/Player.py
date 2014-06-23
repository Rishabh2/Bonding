class Player(object):
    '''
    Class for the player objects
    '''
    import Ribbon
    
    def __init__(self, dx, dy, health, speed, screenWidth, screenHeight, healthLimit, isLiving):
        self.health = health
        self.speed = speed
        self.playerPoint = (screenWidth//2 + 50, screenHeight//2 + 75/2)
        self.dx = dx
        self.dy = dy
        self.limit = healthLimit
        self.living = isLiving
        
    def draw(self, surface):
        self.draw(screen)
    
    def move(self, dx, dy):
        self.playerPoint = (self.playerPoint[0] + dx, self.playerPoint[1] + dy)
        return self.playerPoint
    def addHealth(self, health):
        self.health += health
        if self.health > self.limit:
            self.health = self.limit
    def kill(self):
        self.health = 0
        self.living = False
    def damageTake(self, damage):
        self.health -= damage
        if self.health <= 0:
            kill()
            