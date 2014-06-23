class Player(object):
    '''
    Class for the player objects
    '''

    
    def __init__(self, health, speed, screenWidth, screenHeight):
        self.health = health
        self.speed = speed
        self.playerPoint = (screenWidth//2 + 50, screenHeight//2 + 75/2)
        
    def draw(self, surface):
        self.draw(screen)
    
    def move(self, dx, dy):
        playerPoint = (MainWork.playerPoint[0]+dx, MainWork.point[1]+dy)
        return playerPoint