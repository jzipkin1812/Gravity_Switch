from . import entity
from . import player
from . import utility as u
from . import specialEntities as s
from .constants import *
from .loadAssets import bumpSounds
import pygame
import random

class Level:
    def __init__(self, players = [], levelObjects = [], background = (0, 0, 0), text = "", textLocation = (0, 0), textColor = (150, 150, 150), gridPlatforms = False):
        # Mutable level objects and players
        self.players: list[player.Player] = players
        self.levelObjects: list[entity.Entity] = levelObjects
        
        # Save the original state of the level so that it may be reset later
        self.origPlayers: list[player.Player] = []
        for p in players:
            self.origPlayers.append(p.copy())
            
        self.origObjects: list[entity.Entity] = []
        for o in levelObjects:
            self.origObjects.append(o.copy())
        # Sort objects
        self.levelObjects.sort(key = lambda obj: obj.order())
        # Aesthetics
        self.background: tuple = background
        self.text: str = text
        self.textLocation: tuple = textLocation
        self.textColor: tuple = textColor
        self.gridPlatforms: bool = gridPlatforms
    
    def isComplete(self) -> bool:
        for obj in self.levelObjects:
            if obj.required:
                return(False)
        return(True)
    
    def isBeatable(self):
        foundCoin = False
        for obj in self.origObjects:
            if type(obj) == entity.Coin:
                foundCoin = True
        return(len(self.players) > 0 and foundCoin)
    
    def playerIsDead(self) -> bool:
        for p in self.players:
            if p.x > SCREEN_WIDTH or p.y > SCREEN_HEIGHT or p.x < 0 or p.y < 0:
                return(True)
        return(False)
    
    def display(self, screen):
        screen.fill(self.background)
        u.transparentScreenText(self.textLocation[0], self.textLocation[1], 
                                screen, self.text, LEVELTEXTSIZE, self.textColor)
        for p in self.players:
            p.display(screen)
        for b in self.levelObjects:
            b.display(screen, self.gridPlatforms)
        
    def update(self, milliseconds = 1):
        # print(milliseconds)
        # Delete all dead objects.
        self.levelObjects = [entity for entity in self.levelObjects if not entity.dead]
        # Execute all collisions. Then, update player movements based on the result.
        for p in self.players:
            p.getVmod(milliseconds)
            for b in self.levelObjects:
                b.collide(p)
                if type(b) == s.Quicksand:
                    # Quicksand moves and collides with other entities
                    b.getVmod(milliseconds)
                    for otherPlatform in self.levelObjects:
                        if not (otherPlatform is b):
                            b.quicksandCollide(otherPlatform)
                    b.updateMove(milliseconds)
                elif type(b) == s.Stone:
                    # Stones moves and collides with other entities
                    b.getVmod(milliseconds)
                    for otherPlatform in self.levelObjects:
                        if not (otherPlatform is b):
                            did = b.stoneCollide(otherPlatform)
                            if did:
                                u.playSound(1, random.choice(bumpSounds))
                    b.updateMove(milliseconds)

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
        result += "    text = \"" + self.text + "\",\n"
        result += "    textLocation = " + str(self.textLocation) + ",\n"
        result += "    textColor = " + str(self.textColor) + ",\n"
        result += ")"
        return(result)

    def reset(self):
        self.players = []
        for op in self.origPlayers:
            self.players.append(op.copy())
            
        self.levelObjects = []
        for oo in self.origObjects:
            self.levelObjects.append(oo.copy())

        self.levelObjects.sort(key = lambda obj: obj.order())
            
        s.BeatBlock.solidParity = "blue" 
    
    def solidify(self):
        self.origPlayers = []
        for p in self.players:
            self.origPlayers.append(p.copy())
            
        self.origObjects = []
        for o in self.levelObjects:
            self.origObjects.append(o.copy())
        self.levelObjects.sort(key = lambda obj: obj.order())
    
    def erase(self, x, y):
        for o in self.levelObjects:
            o.erase(x, y)
        self.levelObjects = [entity for entity in self.levelObjects if not entity.dead]
        self.players = [p for p in self.players if not 
                                      (p.x == x and p.y == y)]
        self.solidify()

    def toDict(self):
        result = {
            "players" : [p.toDict() for p in self.players],
            "background" : [self.background[0], self.background[1], self.background[2]],
            "text" : self.text, 
            "textLocation" : [self.textLocation[0], self.textLocation[1]],
            "textColor" : [self.textColor[0], self.textColor[1], self.textColor[2]],
            "levelObjects" : [
                obj.toDict() for obj in self.levelObjects
            ],
            "gridPlatforms" : self.gridPlatforms
        }
        return(result)
    
    def colorFromTheme(self, theme : dict):
        # Color basic attributes
        self.background = theme["background"]
        self.textColor = theme["text"]
        self.gridPlatforms = theme["gridPlatforms"]

        # Color players
        for player in self.players:
            if player.inverted:
                player.color = theme["inverted"]
            else:
                player.color = theme["player"]
        # Color objects
        for obj in self.levelObjects:
            t = type(obj)
            if t == s.Antiplatform or t == s.Lever or t == entity.Entity:
                obj.color = theme["platform"]
            elif t == s.Coin:
                obj.color = theme["coin"]
            elif t == s.Cloud:
                obj.color = theme["cloud"]

def levelFromDict(data : dict):
    result = Level(
        [player.playerFromDict(p) for p in data["players"]],
        [s.entityFromDict(obj) for obj in data["levelObjects"]],
        (data["background"][0], data["background"][1], data["background"][2]),
        data["text"],
        (data["textLocation"][0], data["textLocation"][1]),
        (data["textColor"][0], data["textColor"][1], data["textColor"][2]),
        (data.get("gridPlatforms", False))
    )
    return(result)

