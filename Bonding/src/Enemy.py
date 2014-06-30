import Player
import Calculator

class Enemy(object):
    def __init__(self, health, damageDealer, speed, point, shoots):
        '''
        Constructor
        '''
        self.health = health
        self.damage = damageDealer
        self.speed = speed
        self.point = point
        self.shoots = shoots
        self.calc = Calculator.Calculator()
    
    def move(self, player1, player2):
        distanceToP1 = self.calc.distance(self.point, player1)
        distanceToP2 = self.calc.distance(self.point, player2)
        if distanceToP1 < distanceToP2:
            self.point = self.calc.moveTo(self.point, player1, self.speed)
        else:
            self.point = self.calc.moveTo(self.point, player2, self.speed)