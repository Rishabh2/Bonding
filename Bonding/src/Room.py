import Tile
import pygame

class Room(object):
    
    def __init__(self, floorRow, floorCol, layout=[[0 for col in range(13)] for row in range(7)]):
        self.floorRow = floorRow
        self.floorCol = floorCol
        self.doors = [False, False, False, False]  # N,E,S,W
        self.layout = [[Tile.Tile(layout[row][col]) for col in range(13)] for row in range(7)]
    
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
        bugger = True
        
    def mapdraw(self, rowP, colP, length, offset, screen):
        rowPos = rowP * length + offset
        colPos = colP * length + offset
        if not self.doors[0]:
            pygame.draw.line(screen, [255, 255, 255], [colPos, rowPos], [colPos + length, rowPos])
        if not self.doors[1]:
            pygame.draw.line(screen, [255, 255, 255], [colPos + length, rowPos], [colPos + length, rowPos + length])
        if not self.doors[2]:
            pygame.draw.line(screen, [255, 255, 255], [colPos, rowPos + length], [colPos + length, rowPos + length])
        if not self.doors[3]:
            pygame.draw.line(screen, [255, 255, 255], [colPos, rowPos], [colPos, rowPos + length])
        bugger = True
            
