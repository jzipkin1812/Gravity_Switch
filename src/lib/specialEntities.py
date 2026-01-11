from . import utility as u
from . import player as p
from .entity import *
from .constants import *
import pygame
import math

class NullCube(Entity):
    def __init__(self, x, y, color = (250, 0, 200)):
        super().__init__(x, y, x + GRID_SIZE, y + GRID_SIZE, color)
    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            self.dead = True
            player.x = self.x1
            player.y = self.y1
            player.stop()
            u.playSound(1, nullcubeSound)
            return(True)
        else:
            return(False)
    def display(self, screen, gridlike = False):
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 3)
    def toString(self):
        return(f"s.NullCube({self.x1}, {self.y1})")
    def copy(self):
        result = NullCube(self.x1, self.y1, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "NullCube",
            "x": self.x1,
            "y": self.y1,
            "color": self.color,
        }
    

class Resizer(Entity):
    def __init__(self, x, y, multiplier = 3, color = (255, 243, 179)):
        super().__init__(x, y, x + GRID_SIZE * multiplier, y + GRID_SIZE * multiplier, color)
        self.multiplier = multiplier
        self.small = GRID_SIZE
        self.large = GRID_SIZE * multiplier
        divider = float(multiplier)
        self.x3 = self.x1 +     int((self.x2 - self.x1) / divider)
        self.x4 = self.x1 + 2 * int((self.x2 - self.x1) / divider)
        self.y3 = self.y1 +     int((self.y2 - self.y1) / divider)
        self.y4 = self.y1 + 2 * int((self.y2 - self.y1) / divider)


    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            # Case 1: Grow
            if(player.size < self.large):
                player.x = self.x1
                player.y = self.y1
                player.size = self.large
                u.playSound(2, growingSound)
                # player.stop()
            # Case 2: Shrink
            else:
                player.x = self.x3
                player.y = self.y3
                player.size = self.small
                u.playSound(2, shrinkingSound)
                # player.stop()
            return(True)
        else:
            return(False)
    def toDict(self):
        return {
            "type": "Resizer",
            "x": self.x1,
            "y": self.y1,
            "multiplier": self.multiplier,
            "color": self.color,
        }

    def display(self, screen, gridlike = False):
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 2)
        u.betterRect(screen, self.x3, self.y3, self.x4, self.y4, self.color, 2)
    def toString(self):
        return(f"s.Resizer({self.x1}, {self.y1}, {self.multiplier}, {self.color})")
    def copy(self):
        result = (Resizer(self.x1, self.y1, self.multiplier, (self.color[0], self.color[1], self.color[2])))
        result.timestamp = self.timestamp
        return(result)

class Redirector(Entity):
    def __init__(self, x, y, direction = "up", color = (250, 200, 0)):
        super().__init__(x, y, x + GRID_SIZE, y + GRID_SIZE, color)
        self.direction = direction
    def collide(self, player: p.Player) -> bool:
        if self.willTouch(player):
            # TODO: Improve this?
            # For big players (world F onward) collision is more complex as
            # we want to center the player on the redirector
            # if(player.size > GRID_SIZE ):
            #     if(player.direction == "left" or player.direction == "right"):
            #         player.x = self.x1 - GRID_SIZE
            #         player.y = self.y1
            #     elif(player.direction == "up" or player.direction == "down"):
            #         player.x = self.x1
            #         player.y = self.y1 - GRID_SIZE
            #     player.stop()
            #     player.direction = self.direction
            #     return(True)
            player.x = self.x1
            player.y = self.y1
            player.stop()
            player.direction = self.direction
            u.playSound(1, redirectorSounds[self.direction])
            return(True)
        else:
            return(False)
    def display(self, screen, gridlike = False):
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
        return(f"s.Redirector({self.x1}, {self.y1}, \"{self.direction}\")")
    def copy(self):
        result = Redirector(self.x1, self.y1, self.direction, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "Redirector",
            "x": self.x1,
            "y": self.y1,
            "direction": self.direction,
            "color": self.color,
        }

   
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
            u.playSound(1, cloudSound)
            return(True)
        return(False)
    def toString(self):
        return(f"s.Cloud({self.x1}, {self.y1}, {self.x2}, {self.y2}, {self.color})")
    def copy(self):
        result = Cloud(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "Cloud",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "color": self.color,
        }


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
                u.playSound(2, antiplatformSound)
        else:
            if not self.willTouch(player):
                self.solid = True
    def display(self, screen, gridlike = False):
        if self.solid:
            super().display(screen, gridlike)
        else:
            u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 3)
    def toString(self):
        return(f"s.Antiplatform({self.x1}, {self.y1}, {self.x2}, {self.y2}, {self.color})")
    def copy(self):
        result = Antiplatform(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "Antiplatform",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "color": self.color,
        }

    
class Teleporter(Entity):
    def __init__(self, x1, y1, x2, y2, uses = 0, color = (144, 169, 85)):
        super().__init__(x1, y1, x2, y2, color)
        self.uses = uses
        
    
    def display(self, screen, gridlike = False):
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
                u.playSound(2, teleporterSounds[0])
                self.dead = True
            elif self.uses == 1 or self.uses == 2:
                u.playSound(2, teleporterSounds[self.uses])
            else:
                u.playSound(2, teleporterSounds[3])
        return did
    def toString(self):
        return(f"s.Teleporter({self.x1}, {self.y1}, {self.x2}, {self.y2}, {self.uses}, {self.color})")
    def copy(self):
        result = Teleporter(self.x1, self.y1, self.x2, self.y2, self.uses, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "Teleporter",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "uses": self.uses,
            "color": self.color,
        }



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
            pygame.mixer.Channel(4).play(leverSound)
    def display(self, screen, gridlike = False):
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
        return(f"s.Lever({self.x1}, {self.y1}, {self.x2}, {self.y2}, \"{self.direction}\", {self.color})")
    def copy(self):
        result = Lever(self.x1, self.y1, self.x2, self.y2, self.direction, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "Lever",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "direction": self.direction,
            "color": self.color,
        }

    

class Tar(Entity):
    def __init__(self, x1, y1, x2, y2, direction = "up", color = (47, 79, 79)):
        super().__init__(x1, y1, x2, y2, color)
        self.direction = direction
    def collide(self, player: p.Player) -> bool:
        # Players stick to tar
        if(self.isTouching(player) and player.direction == u.invert(self.direction) and 
           (abs(player.xv) < 1) and (abs(player.yv) < 1)):
            player.stop()
        
    def display(self, screen, gridlike = False):
        if self.direction == "up":
            u.betterRect(screen, self.x1, self.y1, self.x2, (self.y1 + self.y2) // 2, self.color, 0)
        elif self.direction == "down":
            u.betterRect(screen, self.x1, (self.y1 + self.y2) // 2, self.x2, self.y2, self.color, 0)
        elif self.direction == "right":
            u.betterRect(screen, (self.x2 + self.x1) // 2, self.y1, self.x2, self.y2, self.color, 0)
        elif self.direction == "left":
            u.betterRect(screen, self.x1, self.y1, (self.x2 + self.x1) // 2, self.y2, self.color, 0)
    def toString(self):
        return(f"s.Tar({self.x1}, {self.y1}, {self.x2}, {self.y2}, \"{self.direction}\")")
    def copy(self):
        result = Tar(self.x1, self.y1, self.x2, self.y2, self.direction, (self.color[0], self.color[1], self.color[2]))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "Tar",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "direction": self.direction,
            "color": self.color,
        }


class BeatBlock(Entity):
    solidParity = "blue"
    def inverse(p: str) -> str:
        if p == "blue":
            return "red"
        else:
            return "blue"
        
    def __init__(self, x1, y1, x2, y2, parity = "blue", color = None):
        if color is None:
            if parity == "blue":
                color = (0, 0, 205)
            else:
                color = (240, 89, 132)
        super().__init__(x1, y1, x2, y2, color)
        self.parity = parity
    def isOn(self) -> bool:
        return(BeatBlock.solidParity == self.parity)
    def collide(self, player: p.Player) -> bool:
        if self.isOn():
            result = super().collide(player)
            if result:
                BeatBlock.solidParity = BeatBlock.inverse(BeatBlock.solidParity)
                u.playSound(1, beatBlockSound)
            return(result)
        else:   
            return(False)
    def display(self, screen, gridlike = False):
        if self.isOn():
            super().display(screen)
        else:
            u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 3)
    def toString(self):
        return(f"s.BeatBlock({self.x1}, {self.y1}, {self.x2}, {self.y2}, \"{self.parity}\", {self.color})")
    def copy(self):
        result = (BeatBlock(self.x1, self.y1, self.x2, self.y2, self.parity, self.color))
        result.timestamp = self.timestamp
        return(result)
    def toDict(self):
        return {
            "type": "BeatBlock",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "parity": self.parity,
            "color": self.color,
        }

    
class Quicksand(Entity):
    def __init__(self, x1, y1, x2, y2, direction = "down", color = (139, 69, 19)):
        super().__init__(x1, y1, x2, y2, color)
        self.direction = direction
        self.activated = False
        self.settled = False
        
        self.xv = 0
        self.yv = 0
        
        self.accel: float = .025
        self.maxVelocity: int = 15
        self.vMod: float = 1
        
    def isOn(self):
        return(BeatBlock.solidParity == self.parity)
    def collide(self, player: p.Player) -> bool:
        noCrush = (player.direction != u.invert(self.direction))
        did = super().collide(player)
        if (did) and noCrush and (not self.settled):
            self.activated = True
        return(did)
    
    def display(self, screen, gridlike = False):
        super().display(screen)
        if not (self.settled or self.activated):
            self.drawSpikes(screen)
    
    def drawSpikes(self, screen):
        if self.direction == "up":
            for x in range(self.x1, self.x2, GRID_SIZE):
                pygame.draw.polygon(screen, self.color, [(x, self.y1), 
                                                         (x + GRID_SIZE / 2, self.y1 - GRID_SIZE / 2), 
                                                         (x + GRID_SIZE, self.y1)])
        if self.direction == "down":
            for x in range(self.x1, self.x2, GRID_SIZE):
                pygame.draw.polygon(screen, self.color, [(x, self.y2), 
                                                         (x + GRID_SIZE / 2, self.y2 + GRID_SIZE / 2), 
                                                         (x + GRID_SIZE, self.y2)])
        if self.direction == "left":
            for y in range(self.y1, self.y2, GRID_SIZE):
                pygame.draw.polygon(screen, self.color, [(self.x1, y), 
                                                         (self.x1 - GRID_SIZE / 2, y + GRID_SIZE / 2), 
                                                         (self.x1, y + GRID_SIZE)])
        if self.direction == "right":
            for y in range(self.y1, self.y2, GRID_SIZE):
                pygame.draw.polygon(screen, self.color, [(self.x2, y), 
                                                         (self.x2 + GRID_SIZE / 2, y + GRID_SIZE / 2), 
                                                         (self.x2, y + GRID_SIZE)])


    def toString(self):
        return(f"s.Quicksand({self.x1}, {self.y1}, {self.x2}, {self.y2}, \"{self.direction}\", {self.color})")
    def copy(self):
        result = (Quicksand(self.x1, self.y1, self.x2, self.y2, self.direction, (self.color[0], self.color[1], self.color[2])))
        result.timestamp = self.timestamp
        return(result)

    def getVmod(self, milliseconds):
        self.vMod = (milliseconds) * GAME_SPEED
        
    def updateMove(self, milliseconds):
        if (self.settled) or (not self.activated):
            return
        accelMod = self.accel * (milliseconds) * GAME_SPEED
        
        if self.direction == "right" or self.direction == "left":
            self.x1 += self.xv * self.vMod
            self.x2 += self.xv * self.vMod
        if self.direction == "up" or self.direction == "down":
            self.y1 += self.yv * self.vMod
            self.y2 += self.yv * self.vMod
        
        if self.direction == "stop":
            self.xv = self.yv = 0
            self.x1 = round(self.x1)
            self.y1 = round(self.y1)
            self.x2 = round(self.x2)
            self.y2 = round(self.y2)
        elif self.direction == "up":
            self.yv = max(self.yv - accelMod, -1 * self.maxVelocity)
        elif self.direction == "down":
            self.yv = min(self.yv + accelMod, self.maxVelocity)
        elif self.direction == "left":
            self.xv = max(self.xv - accelMod, -1 * self.maxVelocity)
        elif self.direction == "right":
            self.xv = min(self.xv + accelMod, self.maxVelocity)
    
    def quicksandCollide(self, other: Entity) -> bool:
        # Ignore collisions if this isn't moving.
        if (self.settled) or (not self.activated):
            return
        # Ignore collisions with certain types.
        if not (type(other) == Entity or 
                (type(other) == BeatBlock and other.isOn()) or
                type(other) == Quicksand and not other.activated or 
                type(other) == Stone or
                type(other) == Antiplatform and other.solid):
            return
        
        xv = self.xv * self.vMod
        yv = self.yv * self.vMod

        xSize = self.x2 - self.x1
        ySize = self.y2 - self.y1
        
        right = round(self.x2)
        tryRight = round(right + xv)
        
        left = round(self.x1)
        tryLeft = round(left + xv)
        
        top = round(self.y1)
        tryUp = round(top + yv)
        
        bottom = round(self.y2)
        tryDown = round(bottom + yv)
        did = False

        if self.direction == "right" and right <= other.x1 <= tryRight and self.qInYRange(other):
            self.x1 = other.x1 - xSize
            self.x2 = other.x1
            did = True
        elif self.direction == "left" and tryLeft <= other.x2 <= left and self.qInYRange(other):
            self.x1 = other.x2
            self.x2 = other.x2 + xSize
            did = True
        elif self.direction == "up" and top >= other.y2 >= tryUp and self.qInXRange(other):
            self.y1 = other.y2
            self.y2 = other.y2 + ySize
            did = True
        elif self.direction == "down" and tryDown >= other.y1 >= bottom and self.qInXRange(other):
            self.y1 = other.y1 - ySize
            self.y2 = other.y1
            did = True

        if did:
            self.activated = False
            self.settled  = True
            self.roundToGrid()
            u.playSound(2, sandThudSound)
        return(did)

    def qInYRange(self, other: Entity) -> bool:
        isAbove = (other.y2 <= self.y1)
        isBelow = (other.y1 >= self.y2)
        return not(isAbove or isBelow)
    def qInXRange(self, other: Entity) -> bool:
        isLeft = (other.x2 <= self.x1)
        isRight = (other.x1 >= self.x2)
        return not(isLeft or isRight) 
    
    def roundToGrid(self):
        def myround(num):
            return GRID_SIZE * round(num / GRID_SIZE)
        self.x1 = myround(self.x1)
        self.y1 = myround(self.y1)
        self.x2 = myround(self.x2)
        self.y2 = myround(self.y2)
    def toDict(self):
        return {
            "type": "Quicksand",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "direction": self.direction,
            "color": self.color,
        }

class Stone(Entity):
    def __init__(self, x1, y1, x2, y2, color = (150, 150, 150)):
        super().__init__(x1, y1, x2, y2, color)
        
        self.xv = 0
        self.yv = 0
        
        self.accel: float = 0
        self.maxVelocity: int = 15
        self.vMod: float = 1

        self.playerPushing = None
        self.direction : str = "stop"

        avgLength = math.sqrt((x2 - x1) * (y2 - y1))
        modLength = 225 - avgLength
        

        self.startSpeed = max(0.2, min(1, (modLength / 225.0)))
        # print(avgLength, self.startSpeed)

    def display(self, screen, unused = False):
        super().display(screen, False)
        d = 3
        borderWidth = 2
        borderColor = (self.color[0]/d, self.color[1]/d, self.color[2]/d)
        u.dashedLine(screen, borderColor, (self.x1, self.y1), (self.x1, self.y2), 5, 5, borderWidth)
        u.dashedLine(screen, borderColor, (self.x2, self.y1), (self.x2, self.y2), 5, 5, borderWidth)
        u.dashedLine(screen, borderColor, (self.x1, self.y1), (self.x2, self.y1), 5, 5, borderWidth)
        u.dashedLine(screen, borderColor, (self.x1, self.y2), (self.x2, self.y2), 5, 5, borderWidth)
        # u.betterRect(screen, self.x1, self.y1, self.x2, self.y2,
        #               (self.color[0]/d, self.color[1]/d, self.color[2]/d), borderWidth)
        
    def collide(self, player: p.Player) -> bool:
        # Always collide
        pastDir = player.direction
        did = super().collide(player)
        # Push if heavy, otherwise just collide
        if (did) and (player.size > GRID_SIZE):
            self.direction = pastDir
            self.playerPushing = player
            player.direction = "freeze"
            # Set constant velocity for push
            if(self.direction == "down"):
                self.yv = self.startSpeed
            elif(self.direction == "up"):
                self.yv = -1 * self.startSpeed
            elif(self.direction == "left"):
                self.xv = -1 * self.startSpeed
            elif(self.direction == "right"):
                self.xv = self.startSpeed
            u.playSound(1, stoneSlideSound)
        return(did)
    
    def toString(self):
        return(f"s.Stone({self.x1}, {self.y1}, {self.x2}, {self.y2})")
    def copy(self):
        result = (Stone(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2])))
        result.timestamp = self.timestamp
        return(result)

    def getVmod(self, milliseconds):
        self.vMod = (milliseconds) * GAME_SPEED
        
    def updateMove(self, milliseconds):
        if (self.direction == "stop"):
            return
        accelMod = self.accel * (milliseconds) * GAME_SPEED
        
        if self.direction == "right" or self.direction == "left":
            self.x1 += self.xv * self.vMod
            self.x2 += self.xv * self.vMod
            # Player carries with it
            self.playerPushing.x += self.xv * self.vMod
        if self.direction == "up" or self.direction == "down":
            self.y1 += self.yv * self.vMod
            self.y2 += self.yv * self.vMod
            # Player carries with it
            self.playerPushing.y += self.yv * self.vMod
        
        if self.direction == "stop":
            self.xv = self.yv = 0
            self.x1 = round(self.x1)
            self.y1 = round(self.y1)
            self.x2 = round(self.x2)
            self.y2 = round(self.y2)
        elif self.direction == "up":
            self.yv = max(self.yv - accelMod, -1 * self.maxVelocity)
        elif self.direction == "down":
            self.yv = min(self.yv + accelMod, self.maxVelocity)
        elif self.direction == "left":
            self.xv = max(self.xv - accelMod, -1 * self.maxVelocity)
        elif self.direction == "right":
            self.xv = min(self.xv + accelMod, self.maxVelocity)
    
    def stoneCollide(self, other: Entity) -> bool:
        # Ignore collisions if this isn't moving.
        if self.direction == "stop":
            return False
        
        # Stones don't care at all about coins,
        # but the player pushing them should be able to collide with coins
        # while frozen.
        # To process this collision, we temporarily (e.g. just within this function)
        # set the direction of the player.
        if(type(other) == Coin):
            self.playerPushing.direction = self.direction
            other.collide(self.playerPushing)
            self.playerPushing.direction = "freeze"

        
        # Ignore collisions with certain types.
        if not (type(other) == Entity or 
                (type(other) == BeatBlock and other.isOn()) or
                (type(other) == Quicksand and not other.activated) or 
                type(other) == Stone or
                type(other) == Antiplatform and other.solid):
            return False
        
        
        
        xv = self.xv * self.vMod
        yv = self.yv * self.vMod

        xSize = self.x2 - self.x1
        ySize = self.y2 - self.y1
        
        right = round(self.x2)
        tryRight = round(right + xv)
        
        left = round(self.x1)
        tryLeft = round(left + xv)
        
        top = round(self.y1)
        tryUp = round(top + yv)
        
        bottom = round(self.y2)
        tryDown = round(bottom + yv)
        did = False

        # If the pushing player collides with an object, we also stop.
        if(other.isTouching(self.playerPushing)):
            self.direction = "stop"
            self.playerPushing.direction = "stop"
            self.playerPushing.roundToGrid()
            self.roundToGrid()
            u.playSound(1, random.choice(bumpSounds))
            return(did)


        if self.direction == "right" and (right <= other.x1 <= tryRight and self.qInYRange(other)) :
            self.x1 = other.x1 - xSize
            self.x2 = other.x1
            did = True
        elif self.direction == "left" and (tryLeft <= other.x2 <= left and self.qInYRange(other)) :
            self.x1 = other.x2
            self.x2 = other.x2 + xSize
            did = True
        elif self.direction == "up" and (top >= other.y2 >= tryUp and self.qInXRange(other)) :
            self.y1 = other.y2
            self.y2 = other.y2 + ySize
            did = True
        elif self.direction == "down" and (tryDown >= other.y1 >= bottom and self.qInXRange(other)) :
            self.y1 = other.y1 - ySize
            self.y2 = other.y1
            did = True

        if did:
            self.direction = "stop"
            self.playerPushing.direction = "stop"
            self.playerPushing.roundToGrid()
            self.roundToGrid()
            u.playSound(1, random.choice(bumpSounds))
        return(did)

    def qInYRange(self, other: Entity) -> bool:
        isAbove = (other.y2 <= self.y1)
        isBelow = (other.y1 >= self.y2)
        return not(isAbove or isBelow)
    def qInXRange(self, other: Entity) -> bool:
        isLeft = (other.x2 <= self.x1)
        isRight = (other.x1 >= self.x2)
        return not(isLeft or isRight) 
    
    def roundToGrid(self):
        def myround(num):
            return GRID_SIZE * round(num / GRID_SIZE)
        self.x1 = myround(self.x1)
        self.y1 = myround(self.y1)
        self.x2 = myround(self.x2)
        self.y2 = myround(self.y2)
    def toDict(self):
        return {
            "type": "Stone",
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2,
            "color": self.color,
        }

    
def entityFromDict(d : dict):
    t = d["type"]

    if t == "NullCube":
        return NullCube(d["x"], d["y"], d["color"])

    elif t == "Resizer":
        return Resizer(d["x"], d["y"], d["multiplier"], d["color"])

    elif t == "Redirector":
        return Redirector(d["x"], d["y"], d["direction"], d["color"])

    elif t == "Cloud":
        return Cloud(d["x1"], d["y1"], d["x2"], d["y2"], d["color"])

    elif t == "Antiplatform":
        return Antiplatform(d["x1"], d["y1"], d["x2"], d["y2"], d["color"])

    elif t == "Teleporter":
        return Teleporter(d["x1"], d["y1"], d["x2"], d["y2"], d["uses"], d["color"])

    elif t == "Lever":
        return Lever(d["x1"], d["y1"], d["x2"], d["y2"], d["direction"], d["color"])

    elif t == "Tar":
        return Tar(d["x1"], d["y1"], d["x2"], d["y2"], d["direction"], d["color"])

    elif t == "BeatBlock":
        return BeatBlock(d["x1"], d["y1"], d["x2"], d["y2"], d["parity"], d["color"])

    elif t == "Quicksand":
        return Quicksand(d["x1"], d["y1"], d["x2"], d["y2"], d["direction"], d["color"])

    elif t == "Stone":
        return Stone(d["x1"], d["y1"], d["x2"], d["y2"], d["color"])
    
    elif t == "Coin" :
        return Coin(d["x"], d["y"], d["color"])

    elif t == "Entity" :
        return Entity(d["x1"], d["y1"], d["x2"], d["y2"], d["color"])

    raise ValueError(f"Unknown entity type: {t}")