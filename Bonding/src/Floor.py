import Room
import random
    
class Floor(object):

    def __init__(self, rows, cols):
        self.rooms = [[Room.Room(row, col) for col in range(cols)] for row in range(rows)]
        current = [0,0]
        roomStack = []
        totalRooms = rows * cols
        visitedRooms = 1
        
        while visitedRooms < totalRooms:
            neighbors = []
            if 1 <= current[0] < rows:
                if self.rooms[current[0] - 1][ current[1]].numDoors() == 0:
                    neighbors.append([current[0] - 1, current[1]])
            if 0 <= current[0] < rows - 1:
                if self.rooms[current[0] + 1][ current[1]].numDoors() == 0:
                    neighbors.append([current[0] + 1, current[1]])
            if 1 <= current[1] < cols:
                if self.rooms[current[0]][ current[1] - 1].numDoors() == 0:
                    neighbors.append([current[0], current[1] - 1])
            if 0 <= current[1] < cols - 1:
                if self.rooms[current[0]][ current[1] + 1].numDoors() == 0:
                    neighbors.append([current[0], current[1] + 1])
            if len(neighbors) > 0:
                num = random.randrange(len(neighbors))
                self.rooms[current[0]][current[1]].makeDoor(self.rooms[neighbors[num][0]][neighbors[num][1]])
                roomStack.append(current)
                current = neighbors[num]
                visitedRooms += 1
            else:
                current = roomStack.pop()

