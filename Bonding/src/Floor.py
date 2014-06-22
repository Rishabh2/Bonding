class Floor(object):

    import Room

    def __init__(self):
        rooms = [[Room.Room(i, j) for i in range(7)] for j in range(7)]
        current = [0, 0]
        roomStack = []
        totalRooms = 49
        visitedRooms = 1
        
        while visitedRooms < totalRooms:
            neighbors = []
            if 1 <= current[0] <= 6:
                if rooms[current[0] - 1, current[1]].numDoors() > 0:
                    neighbors.append([current[0] - 1, current[1]])
            if 0 <= current[0] <= 5:
                if rooms[current[0] + 1, current[1]].numDoors() > 0:
                    neighbors.append([current[0] + 1, current[1]])
            if 1 <= current[1] <= 6:
                if rooms[current[0], current[1] - 1].numDoors() > 0:
                    neighbors.append([current[0], current[1] - 1])
            if 0 <= current[1] < 5:
                if rooms[current[0], current[1] + 1].numDoors() > 0:
                    neighbors.append([current[0], current[1] + 1])
            if len(neighbors) > 0:
                rooms(current).makeDoor(rooms(neighbors[0]))
                roomStack.append(current)
                current = neighbors[0]
                VisitedCells += 1
            else:
                current = roomStack.pop()
                
    def printgrid(self):
        for i in rooms:
            for j in i:
                if j.doors[3]:
                    print(" ")
                else:
                    print("|")
                if j.doors[1]:
                    print(" ")
                else:
                    print("_")
            
