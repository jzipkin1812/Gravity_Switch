from . import utility as u
from . import player as p
from .constants import *
class Entity:
    def __init__(self, x1, y1, x2, y2, color = (100, 149, 237)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.dead = False
        self.required = False

    
    def display(self, screen):
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 0)
    
    def collide(self, player: p.Player) -> bool:
        xv = player.xv * player.vMod
        yv = player.yv * player.vMod
        
        right = round(player.x + player.size)
        tryRight = round(right + xv)
        
        left = round(player.x)
        tryLeft = round(left + xv)
        
        top = round(player.y)
        tryUp = round(top + yv)
        
        bottom = round(player.y + player.size)
        tryDown = round(bottom + yv)
        did = False
        
        if player.direction == "stop":   
            return(False)
        
        elif player.direction == "right" and right <= self.x1 <= tryRight and self.inYRange(player):
            player.x = self.x1 - player.size
            player.stop()
            did = True
        elif player.direction == "left" and tryLeft <= self.x2 <= left and self.inYRange(player):
            player.x = self.x2
            player.stop()
            did = True
        elif player.direction == "up" and top >= self.y2 >= tryUp and self.inXRange(player):
                # print(self.inXRange(player))
                player.y = self.y2
                player.stop()
                did = True
        elif player.direction == "down" and tryDown >= self.y1 >= bottom and self.inXRange(player):
            player.y = self.y1 - player.size
            player.stop()
            did = True
        
        # if did:
        #     self.color = (200, 0, 0)
        return(did)
    def inYRange(self, player: p.Player) -> bool:
        isAbove = (player.y + player.size) <= self.y1
        isBelow = (player.y) >= self.y2
        return not(isAbove or isBelow)
    def inXRange(self, player: p.Player) -> bool:
        isLeft = (player.x + player.size) <= self.x1
        isRight = (player.x) >= self.x2
        return not(isLeft or isRight)
    def isTouching(self, player):
        isLeft = (player.x + player.size) <= self.x1
        isRight = (player.x) >= self.x2
        isAbove = (player.y + player.size) <= self.y1
        isBelow = (player.y) >= self.y2
        return(not(isLeft or isRight or isAbove or isBelow))
    def toString(self):
        return("b.Entity(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ", " + str(self.color) + ")")
    def willTouch(self, player: p.Player):
        xv = player.xv * player.vMod
        yv = player.yv * player.vMod
        
        right = round(player.x + player.size)
        tryRight = round(right + xv)
        
        left = round(player.x)
        tryLeft = round(left + xv)
        
        top = round(player.y)
        tryUp = round(top + yv)
        
        bottom = round(player.y + player.size)
        tryDown = round(bottom + yv)
        
        if player.direction == "stop":   
            return(False)

        elif ((player.direction == "right" and right <= self.x1 <= tryRight and self.inYRange(player)) or 
             (player.direction == "left" and tryLeft <= self.x2 <= left and self.inYRange(player)) or 
             (player.direction == "up" and top >= self.y2 >= tryUp and self.inXRange(player)) or 
             (player.direction == "down" and tryDown >= self.y1 >= bottom and self.inXRange(player))):
            return(True)
        
    def copy(self):
        return(Entity(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2])))

    def erase(self, x, y):
        if (self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2):
            self.dead = True

    def isOn(self):
        return(False)
        
        
class Coin(Entity):
    def __init__(self, x, y, color = GLOBALCOLORS["coin"]):
        super().__init__(x, y, x + GRID_SIZE, y + GRID_SIZE, color)
        self.required = True
    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            self.dead = True
            return(True)
        else:
            return(False)
    def display(self, screen):
        # print(self.color)
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 0)
    def toString(self):
        return("b.Coin(" + str(self.x1) + ", " + str(self.y1) + "," + str((self.color[0], self.color[1], self.color[2])) + ")")
    def copy(self):
        return(Coin(self.x1, self.y1, (self.color[0], self.color[1], self.color[2])))
    