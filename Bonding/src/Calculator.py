import math
import random

class Calculator(object):
    def __init__(self):
        pass
    
    def distance(self, point1, point2):
        return math.sqrt((point1[1] - point2[1]) ** 2 + (point1[0] - point2[0]) ** 2)
    
    def lineDistance(self, point, line1, line2):
        if line1[0] == line2[0]:
            return abs(point[0] - line1[0])
        if line1[1] == line2[1]:
            return abs(point[1] - line1[1])
        a = (line2[1] - line1[1]) / (line2[0] - line1[0])
        c = line1[1] - line1[0] * a
        b = -1 / a
        d = point[1] - point[0] * b
        return abs(self.distance((((d - c) / (a - b)), (a * ((d - c) / (a - b)) + c)), point))
    
    def moveTo(self, point1, point2, distance):
        theta = math.atan2(point2[1] - point1[1], point2[0] - point1[0])
        return (point1[0] + distance * math.cos(theta), point1[1] + distance * math.sin(theta))
    
    def between(self, p1, l1, l2):
        return (l1[0] < p1[0] < l2[0] or l1[0] > p1[0] > l2[0]) and (l1[1] < p1[1] < l2[1] or l1[1] > p1[1] > l2[1])
    

