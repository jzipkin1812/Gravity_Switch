from . import utility as u
from . import player as p
from .entity import *
from .constants import *
import pygame

class NullCube(Entity):
    def __init__(self, x, y, color = (250, 0, 200)):
        super().__init__(x, y, x + GRID_SIZE, y + GRID_SIZE, color)
    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            self.dead = True
            player.x = self.x1
            player.y = self.y1
            player.stop()
            return(True)
        else:
            return(False)
    def display(self, screen):
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 3)
    def toString(self):
        return("s.NullCube(" + str(self.x1) + ", " + str(self.y1) + ")")
    def copy(self):
        return(NullCube(self.x1, self.y1, (self.color[0], self.color[1], self.color[2])))

class Teleporter(Entity):
    def __init__(self, x, y, color = (250, 0, 200)):
        super().__init__(x, y, x + GRID_SIZE, y + GRID_SIZE, color)
    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            self.dead = True
            player.x = self.x1
            player.y = self.y1
            player.stop()
            return(True)
        else:
            return(False)
    def display(self, screen):
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 3)
    def toString(self):
        return("s.NullCube(" + str(self.x1) + ", " + str(self.y1) + ")")
    def copy(self):
        return(NullCube(self.x1, self.y1, (self.color[0], self.color[1], self.color[2])))

class Redirector(Entity):
    def __init__(self, x, y, direction = "up", color = (250, 200, 0)):
        super().__init__(x, y, x + GRID_SIZE, y + GRID_SIZE, color)
        self.direction = direction
    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            player.x = self.x1
            player.y = self.y1
            player.stop()
            player.direction = self.direction
            return(True)
        else:
            return(False)
    def display(self, screen):
        centerX = self.x1 + GRID_SIZE / 2
        centerY = self.y1 + GRID_SIZE / 2
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 3)
        if self.direction == "up":
            pygame.draw.line(screen, self.color, (centerX, centerY), (centerX, self.y1))
        elif self.direction == "down":
            pygame.draw.line(screen, self.color, (centerX, centerY), (centerX, self.y2))
        elif self.direction == "left":
            pygame.draw.line(screen, self.color, (centerX, centerY), (self.x1, centerY))
        elif self.direction == "right":
            pygame.draw.line(screen, self.color, (centerX, centerY), (self.x2, centerY))
    def toString(self):
        return("s.Redirector(" + str(self.x1) + ", " + str(self.y1) + ", \"" + self.direction + "\")")
    def copy(self):
        return(Redirector(self.x1, self.y1, self.direction, (self.color[0], self.color[1], self.color[2])))
   
class Cloud(Entity):
    def __init__(self, x1, y1, x2, y2, color = (200, 200, 200)):
        super().__init__(x1, y1, x2, y2, color)
    def collide(self, player: p.Player) -> bool:
        yv = player.yv * player.vMod
        bottom = round(player.y + player.size)
        tryDown = round(bottom + yv)
        if player.direction == "down" and tryDown >= self.y1 >= bottom and self.inXRange(player):
            player.y = self.y1 - player.size
            player.stop()
            return(True)
        return(False)
    def toString(self):
        return("s.Cloud(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ")")
    def copy(self):
        return(Cloud(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2])))

class Antiplatform(Entity):
    def __init__(self, x1, y1, x2, y2, color = (85, 51, 51)):
        super().__init__(x1, y1, x2, y2, color)
        self.activated = False
        self.solid = False
    def collide(self, player: p.Player) -> bool:
        if self.solid:
            super().collide(player)
        elif not self.activated:
            if(self.willTouch(player)):
                self.activated = True
        else:
            if not self.willTouch(player):
                self.solid = True
    def display(self, screen):
        if self.solid:
            super().display(screen)
        else:
            u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 3)
    def toString(self):
        return("s.Antiplatform(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ")")
    def copy(self):
        return(Antiplatform(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2])))
    
class Teleporter(Entity):
    def __init__(self, x1, y1, x2, y2, uses = 0, color = (144, 169, 85)):
        super().__init__(x1, y1, x2, y2, color)
        self.uses = uses
        
    
    def display(self, screen):
        x11 = self.x1
        x12 = self.x1 + GRID_SIZE
        y11 = self.y1
        y12 = self.y1 + GRID_SIZE
        
        center1 = (x11 + GRID_SIZE / 2, y11 + GRID_SIZE / 2)
        
        x21 = self.x2
        x22 = self.x2 + GRID_SIZE
        y21 = self.y2
        y22 = self.y2 + GRID_SIZE
        
        center2 = (x21 + GRID_SIZE / 2, y21 + GRID_SIZE / 2)
        # Main square
        width = 3
        u.betterRect(screen, x11, y11, x12, y12, self.color, width)
        u.betterRect(screen, x21, y21, x22, y22, self.color, width)
        # Uses indicators
        useWidth = 0
        if self.uses > 3:
            pygame.draw.polygon(screen, self.color, [(x11, y11), center1, (x11, y12)], useWidth)
            pygame.draw.polygon(screen, self.color, [(x21, y21), center2, (x21, y22)], useWidth)
        if self.uses > 2:
            pygame.draw.polygon(screen, self.color, [(x12, y11), center1, (x11, y11)], useWidth)
            pygame.draw.polygon(screen, self.color, [(x22, y21), center2, (x21, y21)], useWidth)
        if self.uses > 1:
            pygame.draw.polygon(screen, self.color, [(x12, y12), center1, (x12, y11)], useWidth)
            pygame.draw.polygon(screen, self.color, [(x22, y22), center2, (x22, y21)], useWidth) 
        if self.uses > 0:
            pygame.draw.polygon(screen, self.color, [(x11, y12), center1, (x12, y12)], useWidth)
            pygame.draw.polygon(screen, self.color, [(x21, y22), center2, (x22, y22)], useWidth)
        
    def erase(self, x, y):
        if(self.x1 == x and self.y1 == y) or (self.x2 == x and self.y2 == y):
            self.dead = True
        
            
    
    def collide(self, player: p.Player) -> bool:
        t1 = Entity(self.x1, self.y1, self.x1 + GRID_SIZE, self.y1 + GRID_SIZE)
        t2 = Entity(self.x2, self.y2, self.x2 + GRID_SIZE, self.y2 + GRID_SIZE)
        did: bool = False
        
        if t1.willTouch(player):
            player.x = t2.x1
            player.y = t2.y1
            did = True
        elif t2.willTouch(player):
            player.x = t1.x1
            player.y = t1.y1
            did = True
        
        if (did):
            self.uses -= 1
            if self.uses == 0:
                self.dead = True
        
        return did
    def toString(self):
        return("s.Teleporter(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ", " \
            + str(self.uses) + ", " + str(self.color) + ")")
    def copy(self):
        return(Teleporter(self.x1, self.y1, self.x2, self.y2, self.uses, (self.color[0], self.color[1], self.color[2])))


class Lever(Entity):
    def __init__(self, x1, y1, x2, y2, direction = "up", color = (49, 87, 54)):
        super().__init__(x1, y1, x2, y2, color)
        self.direction = direction
        self.hollow = False
    def collide(self, player: p.Player) -> bool:
        # Hollowness
        if(not self.willTouch(player)):
            self.hollow = False
            return False
        elif self.hollow:
            return False
        # If you are counteracting the lever collide normally
        if(player.direction == u.invert(self.direction)):
            super().collide(player)
        # Else swappy swap and don't collide just yet
        elif self.willTouch(player):
            self.direction = u.invert(self.direction)
            self.hollow = True
    def display(self, screen):
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 2)
        if self.direction == "up":
            u.betterRect(screen, self.x1, self.y1, self.x2, (self.y1 + self.y2) // 2, self.color, 0)
        elif self.direction == "down":
            u.betterRect(screen, self.x1, (self.y1 + self.y2) // 2, self.x2, self.y2, self.color, 0)
        elif self.direction == "right":
            u.betterRect(screen, (self.x2 + self.x1) // 2, self.y1, self.x2, self.y2, self.color, 0)
        elif self.direction == "left":
            u.betterRect(screen, self.x1, self.y1, (self.x2 + self.x1) // 2, self.y2, self.color, 0)
    def toString(self):
        return("s.Lever(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ", \"" + self.direction + "\")")
    def copy(self):
        return(Lever(self.x1, self.y1, self.x2, self.y2, self.direction, (self.color[0], self.color[1], self.color[2])))
    

class Tar(Entity):
    def __init__(self, x1, y1, x2, y2, direction = "up", color = (47, 79, 79)):
        super().__init__(x1, y1, x2, y2, color)
        self.direction = direction
    def collide(self, player: p.Player) -> bool:
        # Players stick to tar
        if(self.isTouching(player) and player.direction == u.invert(self.direction)):
            player.stop()
        
    def display(self, screen):
        if self.direction == "up":
            u.betterRect(screen, self.x1, self.y1, self.x2, (self.y1 + self.y2) // 2, self.color, 0)
        elif self.direction == "down":
            u.betterRect(screen, self.x1, (self.y1 + self.y2) // 2, self.x2, self.y2, self.color, 0)
        elif self.direction == "right":
            u.betterRect(screen, (self.x2 + self.x1) // 2, self.y1, self.x2, self.y2, self.color, 0)
        elif self.direction == "left":
            u.betterRect(screen, self.x1, self.y1, (self.x2 + self.x1) // 2, self.y2, self.color, 0)
    def toString(self):
        return("s.Tar(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ", \"" + self.direction + "\")")
    def copy(self):
        return(Tar(self.x1, self.y1, self.x2, self.y2, self.direction, (self.color[0], self.color[1], self.color[2])))