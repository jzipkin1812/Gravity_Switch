from . import level
from . import player as p
from . import entity as b

emptyLevel = level.Level(
players = [],
levelObjects = [],
)


A1 = level.Level(
    players = [
        p.Player(150, 150),
    ],
    levelObjects = [
        b.Entity(50, 50, 100, 600),
        b.Entity(50, 50, 600, 100),
        b.Entity(550, 50, 600, 600),
        b.Entity(50, 550, 600, 600),
        b.Entity(350, 275, 600, 325),
        b.Coin(200, 325),
    ],
)

A2 = level.Level(
    players = [
        p.Player(100, 100),
    ],
    levelObjects = [
        b.Coin(350, 100),
        b.Entity(325, 250, 375, 375),
        b.Entity(100, 325, 150, 375),
        b.Entity(50, 550, 600, 600),
        b.Entity(550, 475, 600, 600),
        b.Coin(100, 425),
        b.Coin(525, 325),
        b.Entity(50, 325, 100, 550),
        b.Entity(450, 50, 600, 100),
    ],
)

A3 = emptyLevel
A4 = emptyLevel                                                      
A5 = emptyLevel
A6 = emptyLevel
A7 = emptyLevel
A8 = emptyLevel
A9 = emptyLevel
A10 = emptyLevel 

worldA = [A1, A2]

