from . import entity
from . import player
from . import utility as u
from .constants import *

class Level:
    def __init__(self, players = [], levelObjects = [], background = (0, 0, 0), text = "", textLocation = (0, 0)):
        # Mutable level objects and players
        self.players: list[player.Player] = players
        self.levelObjects: list[entity.Block] = levelObjects
        
        # Save the original state of the level so that it may be reset later
        self.origPlayers: list[player.Player] = []
        for p in players:
            self.origPlayers.append(p.copy())
            
        self.origObjects: list[entity.Block] = []
        for o in levelObjects:
            self.origObjects.append(o.copy())
        
        # Aesthetics
        self.background = background
        self.text: str = text
        self.textLocation: tuple = textLocation
    
    def isComplete(self) -> bool:
        for obj in self.levelObjects:
            if obj.required:
                return(False)
        return(True)
    
    def playerIsDead(self) -> bool:
        for p in self.players:
            if p.x > SCREEN_WIDTH or p.y > SCREEN_HEIGHT or p.x < 0 or p.y < 0:
                return(True)
        return(False)
    
    def display(self, screen):
        # screen.fill(self.background)
        u.transparentScreenText(self.textLocation[0], self.textLocation[1], screen, self.text, 70, (150, 150, 150))
        for p in self.players:
            p.display(screen)
        for b in self.levelObjects:
            b.display(screen)
        
    def update(self, milliseconds = 1):
        # print(milliseconds)
        # Delete all dead objects.
        self.levelObjects = [entity for entity in self.levelObjects if not entity.dead]
        # Execute all collisions. Then, update player movements based on the result.
        for p in self.players:
            p.getVmod(milliseconds)
            for b in self.levelObjects:
                b.collide(p)
            p.updateMove(milliseconds)
    def toString(self) -> str:
        result: str = "level.Level(\n    players = [\n"
        # All players
        for p in self.players:
            result += "        " + p.toString() + ",\n"
        result += "    ],\n"
        
        result += "    levelObjects = [\n"
        # All entities
        for o in self.levelObjects:
            result += "        " + o.toString() + ",\n"
        result += "    ],\n"
        result += "    background = " + str(self.background) + ",\n"
        result += ")"
        return(result)

    def reset(self):
        self.players = []
        for op in self.origPlayers:
            self.players.append(op.copy())
            
        self.levelObjects = []
        for oo in self.origObjects:
            self.levelObjects.append(oo.copy())
    
    def solidify(self):
        self.origPlayers = []
        for p in self.players:
            self.origPlayers.append(p.copy())
            
        self.origObjects = []
        for o in self.levelObjects:
            self.origObjects.append(o.copy())