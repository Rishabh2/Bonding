import Tile
import pygame

class Room(object):
    
    def __init__(self, floorRow, floorCol, tileRows, tileCols, layout):
        self.floorRow = floorRow
        self.floorCol = floorCol
        self.doors = [False, False, False, False]  # N,E,S,W
        self.layout = [[Tile.Tile(layout[row][col]) for col in range(tileCols)] for row in range(tileRows)]
    
    def numDoors(self):
        return self.doors.count(True)
    
    def makeDoor(self, other):
        addNum = 5
        if self.floorRow > other.floorRow:
            addNum = 0
        if self.floorCol < other.floorCol:
            addNum = 1
        if self.floorRow < other.floorRow:
            addNum = 2
        if self.floorCol > other.floorCol:
            addNum = 3
        self.doors[addNum] = True
        other.doors[(addNum + 2) % 4] = True
