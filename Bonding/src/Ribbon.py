import Calculator

class Ribbon(object):
        
        def __init__(self, playerOne, playerTwo, damageMod):
      
            self.playOne = playerOne
            self.playTwo = playerTwo
            self.damamod = damageMod
            self.Calculator = Calculator.Calculator()

        def doDamage(self, playOne, playTwo, enemy):
            distance = self.Calculator.distance(playOne, playTwo)
            distance = round(distance, 1)
            damage = distance * damamod
            damage = round(damage, 0)
            enemy.health -= damage
            
            