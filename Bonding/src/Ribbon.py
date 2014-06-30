import Calculator

class Ribbon(object):
        
        def __init__(self, damageMod=1):
      
            self.damamod = damageMod
            self.Calculator = Calculator.Calculator()

        def doDamage(self, playOne, playTwo, enemy):
            distance = self.Calculator.distance(playOne, playTwo)
            distance = round(distance, 1)
            damage = self.damamod * 1000 / distance
            damage = round(damage, 0)
            enemy.health -= damage
            
            
