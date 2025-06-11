from .. import level
from .. import player as p
from .. import entity as b
from .. import specialEntities as s
from ..constants import *

F1 = level.Level(
    players = [
        p.Player(125.0, 425.0,(255, 0, 171), inverted = False),
    ],
    levelObjects = [
        s.Resizer(100, 250, 3,(255, 243, 179)),
        b.Entity(50, 50, 75, 75, (198, 255, 0)),
        b.Entity(250, 50, 275, 75, (198, 255, 0)),
        b.Entity(275, 225, 300, 250, (198, 255, 0)),
        b.Entity(50, 175, 75, 200, (198, 255, 0)),
        b.Entity(625, 0, 650, 150, (198, 255, 0)),
        b.Entity(575, 475, 600, 600, (198, 255, 0)),
        b.Entity(575, 625, 650, 650, (198, 255, 0)),
        b.Entity(100, 625, 175, 650, (198, 255, 0)),
        b.Entity(150, 475, 400, 600, (198, 255, 0)),
        b.Entity(0, 475, 125, 600, (198, 255, 0)),
        b.Entity(0, 0, 25, 475, (198, 255, 0)),
        b.Entity(625, 475, 650, 650, (198, 255, 0)),
        b.Entity(475, 250, 500, 275, (198, 255, 0)),
        b.Entity(475, 200, 500, 225, (198, 255, 0)),
        b.Entity(475, 150, 500, 175, (198, 255, 0)),
        b.Entity(475, 100, 500, 125, (198, 255, 0)),
        b.Entity(475, 50, 500, 75, (198, 255, 0)),
        b.Entity(475, 300, 500, 325, (198, 255, 0)),
        b.Entity(475, 350, 500, 375, (198, 255, 0)),
        b.Entity(475, 400, 500, 425, (198, 255, 0)),
        b.Entity(475, 450, 500, 475, (198, 255, 0)),
        b.Entity(475, 500, 500, 525, (198, 255, 0)),
        b.Entity(475, 550, 500, 575, (198, 255, 0)),
        b.Coin(375, 425,(255, 255, 0)),
        b.Coin(475, 600,(255, 255, 0)),
        b.Coin(475, 25,(255, 255, 0)),
        b.Entity(0, 0, 650, 25, (198, 255, 0)),
    ],
    background = (125, 28, 148),
    text = "1.Level Up!",
    textLocation = (50, 350),
    textColor = (255, 243, 179),
)

F2 = level.Level(

)

F3 = level.Level()
F4 = level.Level()
F5 = level.Level()
F6 = level.Level()
F7 = level.Level()
F8 = level.Level()
F9 = level.Level()
F10 = level.Level()
