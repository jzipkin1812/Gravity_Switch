from . import entity
from . import player
from . import utility as u

class Level:
    def __init__(self, players, levelObjects):
        self.players: list[player.Player] = players
        self.levelObjects: list[entity.Block] = levelObjects
    def display(self, screen):
        for p in self.players:
            p.display(screen)
        for b in self.levelObjects:
            b.display(screen)