class Tile(object):
    
    def __init__(self, state):
        self.state = state
        
    def contains(self):
        return self.state