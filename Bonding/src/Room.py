class Room(object):
    
    import Tile
    
    def __init__(self, floorx, floory, layout=[[0 for i in range(13)] for j in range(7)]):
        self.floorx = floorx
        self.floory = floory
        self.doors = [False, False, False, False]  # N,S,E,W
        for i in layout:
            for j in layout[i]:
                self.layout[i][j] = Tile.Tile(layout[i][j])
                
    def numDoors(self):
        return self.doors.count(True)
    
    def makeDoor(self, other):
        if self.floory < other.floory:
            addnum = 0
        if self.floory > other.floory:
            addnum = 1
        if self.floorx > other.floorx:
            addnum = 2
        if self.floorx < other.floorx:
            addnum = 3
        self.doors[addNum] = True
        other.doors[addNum + 2 % 4] = True
