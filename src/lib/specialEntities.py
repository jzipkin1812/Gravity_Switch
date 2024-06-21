from . import utility as u
from . import player as p
from .entity import *
from .constants import *

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
    
class Cloud(Entity):
    def __init__(self, x1, y1, x2, y2, color = (200, 200, 200)):
        super().__init__(x1, y1, x2, y2, color)
    def collide(self, player: p.Player) -> bool:
        bottom = round(player.y + player.size)
        tryDown = round(bottom + player.yv)
        if player.direction == "down" and tryDown >= self.y1 >= bottom and self.inXRange(player):
            player.y = self.y1 - player.size
            player.stop()
            return(True)
        return(False)
    def toString(self):
        return("s.Cloud(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ")")
    def copy(self):
        return(Cloud(self.x1, self.y1, self.x2, self.y2, (self.color[0], self.color[1], self.color[2])))