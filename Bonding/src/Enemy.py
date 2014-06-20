
class Enemy(object, health, damageDealer, speed):
    '''
    Class for the player objects
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.health = health
        self.damage = damageDealer
        self.speed = speed
    def _move(self, speed):
        pass