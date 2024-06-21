from . import utility as u
import pygame
directionDict = {
    pygame.K_DOWN : "down",
    pygame.K_s: "down",

    pygame.K_UP : "up",
    pygame.K_w: "up",

    pygame.K_LEFT : "left",
    pygame.K_a: "left",

    pygame.K_RIGHT : "right",
    pygame.K_d: "right",

}
class Player:
    def __init__(self, x, y, color = (102, 205, 170), size = 25):
        self.color = color
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0
        
        self.size = size
        self.direction = "stop"
        
        self.accel = .025
        self.maxVelocity = 15
        
    
    def display(self, screen):
        u.betterRect(screen, self.x, self.y, self.x + self.size, self.y + self.size, self.color, 0)
    
    def keyMove(self, key):
        self.direction = directionDict[key]
        
    
    def updateMove(self):
        if self.direction == "stop":
            self.xv = self.yv = 0
        elif self.direction == "up":
            self.yv = max(self.yv - self.accel, -1 * self.maxVelocity)
        elif self.direction == "down":
            self.yv = min(self.yv + self.accel, self.maxVelocity)
        elif self.direction == "left":
            self.xv = max(self.xv - self.accel, -1 * self.maxVelocity)
        elif self.direction == "right":
            self.xv = min(self.xv + self.accel, self.maxVelocity)
        
        self.x += self.xv
        self.y += self.yv
    
    def stop(self):
        self.direction = "stop"
        self.xv = self.yv = 0
    
    def copy(self):
        return(Player(self.x, self.y, (self.color[0], self.color[1], self.color[2]), self.size))

    # #This is only for debug, so I can view the player stats
    # def __repr__(self):
    #     return(str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) \
    #         + ", " + str(self.xv) + ", " + str(self.yv))
