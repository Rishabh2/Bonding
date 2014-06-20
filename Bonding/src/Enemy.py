
class Enemy(object):
    '''
    Class for the player objects
    '''


    def __init__(self, health, damageDealer, speed):
        '''
        Constructor
        '''
        self.health = health
        self.damage = damageDealer
        self.speed = speed
    def _move(self, speed):
        pass