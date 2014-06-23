import Room
import random
import queue

class ListQueue(queue.PriorityQueue):
    # @overrides(queue.PriorityQueue)
    def __cmp__(self, other):
        return len(self) - len(other)
    
class Floor(object):
    
    def longestPath(self, current, path):
        neighbors = []
        paths = ListQueue()
        doors = self.rooms[current[0]][current[1]].doors
        if doors[0]:
            if current[0] > 0:
                    neighbors.append((current[0] - 1, current[1]))
        if doors[1]:
            if current[1] < len(self.rooms[0]) - 1:
                    neighbors.append((current[0], current[1] + 1))
        if doors[2]:
            if current[0] < len(self.rooms[0]) - 1:
                    neighbors.append((current[0] + 1, current[1]))
        if doors[3]:
            if current[1] > 0:
                    neighbors.append((current[0], current[1] - 1))
        for neighbor in neighbors:
            if neighbor in path:
                neighbors.remove(neighbor)
        if len(neighbors) == 0:
            return path
        else:
            for neighbor in neighbors:
                path.append(neighbor)
                paths.put(self.longestPath(neighbor, path))
        return paths.get()

    def __init__(self, rows, cols, tileRows, tileCols):
        self.rooms = [[Room.Room(row, col, tileRows, tileCols, [[0 for col in range(tileCols)] for row in range(tileRows)]) for col in range(cols)] for row in range(rows)]
        self.currentRoom = (0, 0)
        current = (0, 0)
        roomStack = []
        totalRooms = rows * cols
        visitedRooms = 1
        
        while visitedRooms < totalRooms:
            neighbors = []
            if  current[0] > 0:
                if self.rooms[current[0] - 1][ current[1]].numDoors() == 0:
                    neighbors.append([current[0] - 1, current[1]])
            if current[0] < rows - 1:
                if self.rooms[current[0] + 1][ current[1]].numDoors() == 0:
                    neighbors.append([current[0] + 1, current[1]])
            if current[1] > 0:
                if self.rooms[current[0]][ current[1] - 1].numDoors() == 0:
                    neighbors.append([current[0], current[1] - 1])
            if current[1] < cols - 1:
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
        
        self.bossRoom = self.longestPath((0, 0), [(0, 0)])[-1]