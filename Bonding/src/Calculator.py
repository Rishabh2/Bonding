import math
def distance(point, line1, line2):
    a = line2[1] - line1[1] / (line2[0] - line1[0])
    b = line1[1] - line1[0] * a
    c = -1 / a
    d = point[1] - point[0] * c
    return distance([d - c / (a - b)], [a(d - c / (a - b)) + c])

def distance(point1, point2):
    return math.sqrt((point1[1] - point2[1]) ** 2 + (point1[0] - point2[0]) ** 2)
