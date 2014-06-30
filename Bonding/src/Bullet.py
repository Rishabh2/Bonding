import Calculator
class Bullet(object):
    
    def __init__(self, point, target, damage):
        self.calc = Calculator.Calculator()
        self.point = point
        t = self.calc.moveTo(self.point, target, 10)
        self.damage = damage
        self.dx = t[0] - point[0]
        self.dy = t[1] - point[1]
        
        
    def move(self, p1, p2):
        self.point = (self.point[0] + self.dx, self.point[1] + self.dy)
        if self.point[0] < 88 or self.point[0] > 1138 or self.point[1] < 150 or self.point[1] > 675:
            return True
        return False
        
    def isBullet(self):
        return True
