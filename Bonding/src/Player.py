class Player(object):
    '''
    Class for the player objects
    '''
    import Ribbon
    
    def __init__(self, dx, dy, health, speed, screenWidth, screenHeight):
        self.health = health
        self.speed = speed
        self.playerPoint = (screenWidth//2 + 50, screenHeight//2 + 75/2)
        self.dx = dx
        self.dy = dy
        
    def draw(self, surface):
        self.draw(screen)
    
    def move(self, dx, dy):
        self.playerPoint = (self.playerPoint[0] + dx, self.playerPoint[1] + dy)
        return self.playerPoint
