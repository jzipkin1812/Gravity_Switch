import pygame
from . import utility as u
from . import player as p
from .constants import *
from .loadAssets import *
import random

class Entity:
    # This monotonically increasing counter
    # tracks how recently items have been added to a level.
    globalCtr = 0
    def __init__(self, x1, y1, x2, y2, color = (100, 149, 237)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.dead = False
        self.required = False
        self.timestamp = Entity.globalCtr
        Entity.globalCtr += 1
    def display(self, screen, gridlike = False):
        if(gridlike):
            self.displayGridlike(screen)
        else:
            u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 0)

    def displayGridlike(self, screen):
        spacing = GRID_SIZE / 2
        lineWidth = 2
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)

        left = self.x1
        top = self.y1
        right = self.x2
        bottom = self.y2
        y = top
        while y < bottom:
            dx = min(width, bottom - y)
            pygame.draw.line(screen, self.color, (left, y), (left + dx, y + dx), lineWidth)
            y += spacing
        while y > top:
            dx = min(width, y - top)
            pygame.draw.line(screen, self.color, (left, y), (left + dx, y - dx), lineWidth)
            y -= spacing

        
        x = left
        while x < right:
            dy = min(height, right - x)
            pygame.draw.line(screen, self.color, (x, top), (x + dy, top + dy), lineWidth)
            x += spacing
        while x > left:
            dy = min(height, x - left)
            pygame.draw.line(screen, self.color, (x, top), (x - dy, top + dy), lineWidth)
            x -= spacing
        
        x = left
        while x < right:
            dy = min(height, right - x)
            pygame.draw.line(screen, self.color, (x, bottom), (x + dy, bottom - dy), lineWidth)
            x += spacing
        while x > left:
            dy = min(height, x - left)
            pygame.draw.line(screen, self.color, (x, bottom), (x - dy, bottom - dy), lineWidth)
            x -= spacing


        
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 2)
    
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
        # Debug: Marks platforms red when hit to tell me whether they can be removed without consequence
        # if did:
        #     self.color = (255, 0, 0)
        if did:
            u.playSound(1, random.choice(bumpSounds))
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
        return(f"b.Entity({self.x1}, {self.y1}, {self.x2}, {self.y2}, {self.color})")
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
        result = (Entity(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2])))
        result.timestamp = self.timestamp
        return(result)
    
    def erase(self, x, y):
        if (self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2):
            self.dead = True

    def isOn(self):
        return(False)
    
    def order(self) -> int:
        return(1)
        
        
class Coin(Entity):
    def __init__(self, x, y, color = GLOBALCOLORS["coin"]):
        super().__init__(x, y, x + GRID_SIZE, y + GRID_SIZE, color)
        self.required = True
    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            self.dead = True
            u.playSound(1, coinSound)
            return(True)
        else:
            return(False)
    def display(self, screen, gridlike = False):
        # print(self.color)
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 0)
    def toString(self):
        return("b.Coin(" + str(self.x1) + ", " + str(self.y1) + "," + str((self.color[0], self.color[1], self.color[2])) + ")")
    def copy(self):
        result = Coin(self.x1, self.y1, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def order(self) -> int:
        return(2)