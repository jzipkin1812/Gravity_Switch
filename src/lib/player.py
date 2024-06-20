class Player:
    def __init__(self, x1, y1, color = (102, 205, 170), size = 25):
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + size
        self.y2 = y1 + size
        self.xv = 0
        self.yv = 0
        self.size = size
        self.direction = "stop"

    #This is only for debug, so I can view the player stats
    def __repr__(self):
        return(str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) \
            + ", " + str(self.xv) + ", " + str(self.yv))
