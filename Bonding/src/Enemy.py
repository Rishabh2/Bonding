import player
class Enemy(object):
    def __init__(self, health, damageDealer, speed):
        '''
        Constructor
        '''
        self.health = health
        self.damage = damageDealer
        self.speed = speed
    def _move(self, speed):
        pass