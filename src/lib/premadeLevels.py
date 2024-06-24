from . import level
from . import player as p
from . import entity as b
from . import specialEntities as s
from .constants import *

editorLevel = level.Level(
    
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
A3 = level.Level(
    players = [
        p.Player(100, 100),
    ],
    levelObjects = [
        b.Entity(50, 50, 100, 225),
        b.Entity(50, 50, 225, 100),
        b.Entity(50, 425, 100, 600),
        b.Entity(50, 550, 225, 600),
        s.NullCube(325, 525),
        b.Entity(425, 550, 600, 600),
        b.Entity(550, 425, 600, 600),
        b.Entity(550, 50, 600, 225),
        b.Entity(425, 50, 600, 100),
        s.NullCube(325, 350),
        b.Coin(475, 350),
    ],
)
A4 = level.Level(
    players = [
        p.Player(50, 500),
    ],
    levelObjects = [
        b.Entity(50, 525, 550, 575),
        b.Entity(550, 375, 600, 575),
        b.Entity(550, 50, 600, 175),
        b.Entity(475, 50, 600, 100),
        s.NullCube(300, 100),
        b.Entity(50, 350, 175, 400),
        b.Coin(100, 325),
        b.Entity(50, 150, 100, 400),
        b.Entity(300, 275, 350, 400),
        s.NullCube(425, 175),
        s.NullCube(425, 250),
        b.Coin(425, 325),
    ],
)                                                      
A5 = level.Level(
    players = [
        p.Player(125, 575),
    ],
    levelObjects = [
        b.Entity(0, 350, 50, 650),
        b.Entity(0, 600, 275, 650),
        b.Entity(225, 350, 275, 650),
        s.Cloud(50, 350, 225, 375),
        s.Cloud(325, 475, 600, 500),
        s.Cloud(225, 200, 550, 225),
        b.Coin(25, 175),
        b.Entity(475, 275, 525, 400),
        b.Entity(75, 50, 400, 100),
    ],
)
A6 = level.Level(
    players = [
        p.Player(325, 325),
    ],
    levelObjects = [
        b.Entity(0, 600, 650, 650),
        b.Entity(0, 0, 200, 50),
        b.Entity(0, 0, 50, 225),
        s.Cloud(50, 200, 200, 225),
        b.Coin(250, 25),
        b.Entity(325, 0, 500, 50),
        b.Entity(275, 350, 400, 400),
        b.Entity(275, 550, 400, 600),
        b.Coin(250, 575),
        b.Coin(400, 575),
        s.NullCube(100, 325),
        s.Cloud(400, 350, 525, 375),
        s.Cloud(400, 200, 525, 225),
        b.Entity(600, 125, 650, 225),
        s.NullCube(400, 250),
    ],
)
A7 = level.Level(
    players = [
        p.Player(50, 575),
    ],
    levelObjects = [
        b.Entity(0, 0, 50, 650),
        b.Entity(0, 0, 650, 50),
        b.Entity(600, 0, 650, 350),
        b.Entity(600, 525, 650, 650),
        b.Entity(0, 600, 650, 650),
        s.Cloud(425, 400, 650, 425),
        b.Entity(500, 150, 650, 200),
        b.Coin(200, 350),
        b.Entity(50, 50, 250, 100),
        b.Entity(275, 550, 325, 600),
        s.NullCube(350, 350),
        b.Coin(350, 250),
        b.Coin(150, 375),
        b.Entity(0, 375, 150, 425),
    ],
)
A8 = level.Level(
    players = [
        p.Player(50, 575),
    ],
    levelObjects = [
        b.Entity(0, 600, 500, 650),
        b.Entity(0, 225, 50, 600),
        s.Cloud(50, 225, 175, 250),
        b.Entity(600, 225, 650, 650),
        s.Cloud(475, 225, 600, 250),
        s.NullCube(575, 325),
        b.Coin(325, 325),
        b.Coin(325, 575),
        b.Coin(325, 200),
        b.Entity(475, 0, 650, 50),
        b.Coin(325, 50),
        s.NullCube(50, 50),
    ],
)
A9 = level.Level(
    players = [
        p.Player(125, 50),
    ],
    levelObjects = [
        b.Entity(0, 0, 300, 50),
        s.Cloud(50, 225, 250, 250),
        b.Entity(0, 375, 50, 650),
        b.Entity(0, 600, 650, 650),
        b.Entity(600, 375, 650, 650),
        b.Coin(375, 50),
        b.Coin(375, 200),
        b.Coin(375, 575),
        s.NullCube(575, 200),
        s.NullCube(575, 50),
        b.Coin(575, 125),
        b.Coin(575, 0),
    ],
)
A10 = level.Level(
    players = [
        p.Player(300, 275),
    ],
    levelObjects = [
        s.NullCube(525, 275),
        b.Coin(525, 150),
        b.Entity(450, 0, 625, 50),
        s.Cloud(25, 375, 225, 400),
        s.NullCube(50, 275),
        b.Entity(0, 600, 400, 650),
        b.Coin(200, 275),
        b.Coin(300, 375),
        b.Coin(475, 575),
        b.Entity(600, 0, 650, 225),
        b.Entity(550, 525, 600, 650),
        b.Entity(550, 525, 650, 575),
        s.NullCube(300, 50),
        s.NullCube(300, 525),
        b.Coin(200, 525),
        b.Entity(0, 525, 50, 650),
        s.Cloud(225, 175, 400, 200),
        b.Coin(50, 150),
    ],
)

worldA = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]
for l in worldA:
    l.background = (0, 0, 80)
A10.background = (0, 0, 40)

B1 = level.Level(
    players = [
        p.Player(100, 525,(255, 255, 68)),
    ],
    levelObjects = [
        s.Redirector(100, 250, "right"),
        s.Redirector(525, 350, "up"),
        s.Redirector(225, 350, "right"),
        s.Redirector(225, 100, "down"),
        b.Coin(225, 250,(204, 68, 34)),
        b.Coin(375, 100,(204, 68, 34)),
        b.Coin(525, 250,(204, 68, 34)),
        b.Entity(475, 50, 600, 100, (85, 51, 51)),
        b.Entity(550, 50, 600, 175, (85, 51, 51)),
        b.Entity(50, 50, 100, 175, (85, 51, 51)),
        b.Entity(50, 50, 175, 100, (85, 51, 51)),
        b.Entity(50, 475, 100, 600, (85, 51, 51)),
        b.Entity(50, 550, 175, 600, (85, 51, 51)),
        b.Entity(475, 550, 600, 600, (85, 51, 51)),
        b.Entity(550, 475, 600, 600, (85, 51, 51)),
    ],
    background = (255, 102, 0),
)
B2 = level.Level(
    players = [
        p.Player(100, 525,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(50, 50, 100, 175, (85, 51, 51)),
        b.Entity(50, 50, 175, 100, (85, 51, 51)),
        b.Entity(50, 475, 100, 600, (85, 51, 51)),
        b.Entity(50, 550, 175, 600, (85, 51, 51)),
        b.Entity(475, 550, 600, 600, (85, 51, 51)),
        b.Entity(550, 475, 600, 600, (85, 51, 51)),
        b.Entity(550, 50, 600, 175, (85, 51, 51)),
        b.Entity(475, 50, 600, 100, (85, 51, 51)),
        s.Antiplatform(100, 300, 550, 350),
        s.Antiplatform(300, 100, 350, 550),
        b.Coin(100, 225,(204, 68, 34)),
        b.Coin(525, 225,(204, 68, 34)),
        b.Coin(350, 25,(204, 68, 34)),
    ],
    background = (255, 102, 0),
)
B3 = level.Level(
    players = [
        p.Player(100, 525,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(50, 50, 100, 175, (85, 51, 51)),
        b.Entity(50, 50, 175, 100, (85, 51, 51)),
        b.Entity(50, 475, 100, 600, (85, 51, 51)),
        b.Entity(50, 550, 175, 600, (85, 51, 51)),
        b.Entity(550, 475, 600, 600, (85, 51, 51)),
        b.Coin(100, 375,(204, 68, 34)),
        s.Antiplatform(50, 250, 250, 300),
        s.Antiplatform(250, 50, 300, 550),
        s.Antiplatform(425, 50, 475, 475),
        s.Antiplatform(475, 425, 600, 475),
        b.Coin(350, 100,(204, 68, 34)),
        s.Redirector(525, 225, "down"),
        s.Redirector(525, 100, "left"),
        s.Redirector(350, 475, "up"),
        b.Coin(525, 525,(204, 68, 34)),
        b.Entity(525, 550, 550, 600, (85, 51, 51)),
    ],
    background = (255, 102, 0),
)
B4 = level.Level(
    players = [
        p.Player(350, 250,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(0, 0, 50, 400, (85, 51, 51)),
        b.Entity(600, 0, 650, 400, (85, 51, 51)),
        s.Antiplatform(300, 350, 600, 400),
        s.Antiplatform(450, 150, 500, 350),
        b.Entity(300, 150, 450, 200, (85, 51, 51)),
        b.Coin(500, 175,(204, 68, 34)),
        b.Coin(575, 325,(204, 68, 34)),
        s.Redirector(500, 25, "left"),
        s.Antiplatform(450, 450, 500, 600),
        s.Redirector(575, 525, "left"),
        s.Redirector(350, 525, "up"),
        s.Redirector(50, 525, "right"),
        b.Coin(150, 400,(204, 68, 34)),
    ],
    background = (255, 102, 0),
)
B5 = level.Level(
    players = [
        p.Player(150, 50,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(200, 150, 275, 200, (85, 51, 51)),
        s.Redirector(525, 50, "down"),
        b.Entity(600, 0, 650, 650, (85, 51, 51)),
        s.Redirector(575, 550, "up"),
        s.Redirector(525, 500, "left"),
        s.Antiplatform(325, 300, 375, 350),
        s.Redirector(150, 525, "up"),
        b.Entity(325, 550, 375, 600, (85, 51, 51)),
        s.Antiplatform(50, 425, 275, 475),
        b.Entity(275, 150, 325, 475, (85, 51, 51)),
        b.Coin(150, 300,(204, 68, 34)),
        b.Entity(50, 150, 125, 200, (85, 51, 51)),
        b.Entity(0, 0, 50, 650, (85, 51, 51)),
        s.Antiplatform(325, 150, 600, 200),
        b.Coin(525, 350,(204, 68, 34)),
    ],
    background = (255, 102, 0),
)
B6 = level.Level(
    players = [
        p.Player(450.0, 375.0,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(600, 150, 650, 325, (85, 51, 51)),
        b.Entity(475, 275, 650, 325, (85, 51, 51)),
        b.Entity(475, 275, 525, 450, (85, 51, 51)),
        b.Entity(350, 400, 525, 450, (85, 51, 51)),
        b.Entity(350, 400, 400, 575, (85, 51, 51)),
        b.Entity(225, 525, 400, 575, (85, 51, 51)),
        b.Entity(225, 525, 275, 650, (85, 51, 51)),
        s.Antiplatform(475, 150, 525, 275),
        s.Redirector(50, 375, "right"),
        s.Redirector(450, 50, "left"),
        s.Redirector(325, 150, "right"),
        s.Redirector(525, 50, "left"),
        s.Antiplatform(350, 275, 400, 400),
        s.Antiplatform(225, 400, 350, 450),
        b.Coin(125, 450,(204, 68, 34)),
        b.Entity(0, 0, 50, 400, (85, 51, 51)),
        b.Coin(575, 250,(204, 68, 34)),
        s.Antiplatform(275, 0, 325, 75),
        b.Coin(250, 250,(204, 68, 34)),
    ],
    background = (255, 102, 0),
    text = "6. \"Staircase\"",
    textLocation = (285, 590),
)
B7 = level.Level(
    players = [
        p.Player(25, 50,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(0, 600, 650, 650, (85, 51, 51)),
        b.Entity(600, 0, 650, 450, (85, 51, 51)),
        s.Antiplatform(450, 450, 650, 500),
        b.Entity(0, 275, 50, 650, (85, 51, 51)),
        b.Entity(400, 0, 600, 50, (85, 51, 51)),
        b.Coin(575, 200,(204, 68, 34)),
        s.Redirector(275, 250, "down"),
        s.Antiplatform(150, 325, 200, 450),
        s.Antiplatform(150, 450, 200, 600),
        s.Redirector(200, 450, "down"),
        b.Coin(50, 450,(204, 68, 34)),
        b.Coin(275, 375,(204, 68, 34)),
        b.Coin(400, 425,(204, 68, 34)),
        b.Coin(575, 575,(204, 68, 34)),
        s.Redirector(50, 0, "down"),
        b.Coin(275, 50,(204, 68, 34)),
        s.Antiplatform(400, 50, 450, 325),
        s.Antiplatform(450, 275, 600, 325),
        s.Antiplatform(50, 275, 400, 325),
    ],
    background = (255, 102, 0),
    text = "7. \"Trapdoors\"",
    textLocation = (50, 120),
)
B8 = level.Level(
    players = [
        p.Player(50, 50,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(0, 50, 50, 100, (85, 51, 51)),
        s.Redirector(400, 50, "up"),
        b.Coin(100, 400,(204, 68, 34)),
        b.Coin(375, 250,(204, 68, 34)),
        s.Redirector(225, 50, "up"),
        b.Entity(0, 550, 50, 650, (85, 51, 51)),
        b.Entity(0, 200, 50, 350, (85, 51, 51)),
        b.Entity(600, 550, 650, 600, (85, 51, 51)),
        s.Antiplatform(475, 200, 525, 600),
        b.Entity(0, 0, 425, 50, (85, 51, 51)),
        b.Entity(550, 0, 650, 50, (85, 51, 51)),
        s.Antiplatform(50, 200, 175, 250),
        s.Antiplatform(275, 50, 325, 100),
        b.Entity(400, 600, 650, 650, (85, 51, 51)),
        b.Entity(150, 600, 250, 650, (85, 51, 51)),
        s.Antiplatform(300, 400, 350, 650),
        s.Antiplatform(175, 350, 350, 400),
        b.Coin(425, 325,(204, 68, 34)),
    ],
    background = (255, 102, 0),
)
B9 = level.Level(
    players = [
        p.Player(125, 200,(255, 255, 68)),
    ],
    levelObjects = [
        b.Entity(0, 600, 650, 650, (85, 51, 51)),
        b.Entity(600, 0, 650, 650, (85, 51, 51)),
        b.Entity(0, 0, 650, 50, (85, 51, 51)),
        b.Entity(0, 50, 50, 600, (85, 51, 51)),
        b.Coin(50, 200,(204, 68, 34)),
        s.Redirector(50, 50, "right"),
        b.Coin(125, 50,(204, 68, 34)),
        b.Entity(225, 225, 275, 275, (85, 51, 51)),
        s.Antiplatform(50, 225, 225, 275),
        s.Antiplatform(225, 50, 275, 225),
        s.Antiplatform(425, 50, 475, 375),
        s.Antiplatform(425, 375, 600, 425),
        s.Redirector(575, 575, "left"),
        s.Redirector(50, 575, "up"),
        s.Redirector(325, 575, "left"),
        b.Coin(425, 575,(204, 68, 34)),
        b.Coin(575, 200,(204, 68, 34)),
        b.Coin(400, 200,(204, 68, 34)),
        b.Coin(400, 50,(204, 68, 34)),
        b.Coin(475, 50,(204, 68, 34)),
        s.Redirector(575, 50, "down"),
        s.Antiplatform(50, 375, 100, 425),
        b.Coin(50, 450,(204, 68, 34)),
        b.Coin(125, 450,(204, 68, 34)),
    ],
    background = (255, 102, 0),
)
B10 = level.Level(
    players = [
        p.Player(75.0, 575.0,(255, 255, 68)),
    ],
    levelObjects = [
        s.Redirector(400, 575, "up"),
        b.Entity(525, 0, 650, 50, (85, 51, 51)),
        s.Redirector(400, 0, "down"),
        s.Redirector(575, 350, "up"),
        s.Antiplatform(150, 0, 200, 100),
        s.Cloud(325, 450, 500, 475),
        b.Coin(175, 425,(204, 68, 34)),
        b.Entity(0, 600, 225, 650, (85, 51, 51)),
        b.Entity(600, 50, 650, 125, (85, 51, 51)),
        s.NullCube(75, 50),
        s.NullCube(400, 350),
        s.Antiplatform(325, 225, 500, 275),
        s.NullCube(75, 200),
        b.Coin(200, 300,(204, 68, 34)),
        s.Redirector(575, 275, "up"),
        b.Coin(525, 275,(204, 68, 34)),
        b.Coin(525, 350,(204, 68, 34)),
        b.Entity(0, 300, 50, 400, (85, 51, 51)),
    ],
    background = (80, 0, 0),
)

worldB = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10]


worldInfo = [
    (worldA, levelSelectWorldA),
    (worldB, levelSelectWorldB),
]