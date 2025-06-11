from .. import level
from .. import player as p
from .. import entity as b
from .. import specialEntities as s
from ..constants import *

A1 = level.Level(
    players = [
        p.Player(150.0, 150.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(50, 50, 100, 600, (100, 149, 237)),
        b.Entity(50, 50, 600, 100, (100, 149, 237)),
        b.Entity(550, 50, 600, 600, (100, 149, 237)),
        b.Entity(50, 550, 600, 600, (100, 149, 237)),
        b.Entity(350, 275, 600, 325, (100, 149, 237)),
        b.Coin(200, 325,(123, 104, 238)),
    ],
    background = (0, 0, 80),
    text = "1.Out of the Nest",
    textLocation = (100, 600),
    textColor = (240, 240, 240),
)
A2 = level.Level(
    players = [
        p.Player(100.0, 100.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Coin(350, 100,(123, 104, 238)),
        b.Entity(325, 250, 375, 375, (100, 149, 237)),
        b.Entity(100, 325, 150, 375, (100, 149, 237)),
        b.Entity(50, 550, 600, 600, (100, 149, 237)),
        b.Entity(550, 475, 600, 600, (100, 149, 237)),
        b.Coin(100, 425,(123, 104, 238)),
        b.Coin(525, 325,(123, 104, 238)),
        b.Entity(50, 325, 100, 550, (100, 149, 237)),
        b.Entity(450, 50, 600, 100, (100, 149, 237)),
    ],
    background = (0, 0, 80),
    text = "2.To Infinity and Beyond",
    textLocation = (0, 600),
    textColor = (240, 240, 240),
)
A3 = level.Level(
    players = [
        p.Player(100.0, 100.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(50, 50, 100, 225, (100, 149, 237)),
        b.Entity(50, 50, 225, 100, (100, 149, 237)),
        b.Entity(50, 425, 100, 600, (100, 149, 237)),
        b.Entity(50, 550, 225, 600, (100, 149, 237)),
        s.NullCube(325, 525),
        b.Entity(425, 550, 600, 600, (100, 149, 237)),
        b.Entity(550, 425, 600, 600, (100, 149, 237)),
        b.Entity(550, 50, 600, 225, (100, 149, 237)),
        b.Entity(425, 50, 600, 100, (100, 149, 237)),
        s.NullCube(325, 350),
        b.Coin(475, 350,(123, 104, 238)),
    ],
    background = (0, 0, 80),
    text = "3.New Friends",
    textLocation = (150, 150),
    textColor = (240, 240, 240),
)
A4 = level.Level(
    players = [
        p.Player(50.0, 500.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(50, 525, 550, 575, (100, 149, 237)),
        b.Entity(550, 375, 600, 575, (100, 149, 237)),
        b.Entity(550, 50, 600, 175, (100, 149, 237)),
        b.Entity(475, 50, 600, 100, (100, 149, 237)),
        s.NullCube(300, 100),
        b.Entity(50, 350, 175, 400, (100, 149, 237)),
        b.Coin(100, 325,(123, 104, 238)),
        b.Entity(50, 150, 100, 400, (100, 149, 237)),
        b.Entity(300, 275, 350, 400, (100, 149, 237)),
        s.NullCube(425, 175),
        s.NullCube(425, 250),
        b.Coin(425, 325,(123, 104, 238)),
    ],
    background = (0, 0, 80),
    text = "4.Use Wisely",
    textLocation = (125, 575),
    textColor = (240, 240, 240),
)                                                  
A5 = level.Level(
    players = [
        p.Player(125.0, 575.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(0, 350, 50, 650, (100, 149, 237)),
        b.Entity(0, 600, 275, 650, (100, 149, 237)),
        b.Entity(225, 350, 275, 650, (100, 149, 237)),
        s.Cloud(50, 350, 225, 375),
        s.Cloud(325, 475, 600, 500),
        s.Cloud(225, 200, 550, 225),
        b.Coin(25, 175,(123, 104, 238)),
        b.Entity(475, 275, 525, 400, (100, 149, 237)),
        b.Entity(75, 50, 400, 100, (100, 149, 237)),
    ],
    background = (0, 0, 80),
    text = "5.Up in the Clouds",
    textLocation = (75, 0),
    textColor = (240, 240, 240),
)
A6 = level.Level(
    players = [
        p.Player(325.0, 325.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(0, 600, 650, 650, (100, 149, 237)),
        b.Entity(0, 0, 200, 50, (100, 149, 237)),
        b.Entity(0, 0, 50, 225, (100, 149, 237)),
        s.Cloud(50, 200, 200, 225),
        b.Coin(250, 25,(123, 104, 238)),
        b.Entity(325, 0, 500, 50, (100, 149, 237)),
        b.Entity(275, 350, 400, 400, (100, 149, 237)),
        b.Entity(275, 550, 400, 600, (100, 149, 237)),
        b.Coin(250, 575,(123, 104, 238)),
        b.Coin(400, 575,(123, 104, 238)),
        s.NullCube(100, 325),
        s.Cloud(400, 350, 525, 375),
        s.Cloud(400, 200, 525, 225),
        b.Entity(600, 125, 650, 225, (100, 149, 237)),
        s.NullCube(400, 250),
    ],
    background = (0, 0, 80),
    text = "6.A True Challenge",
    textLocation = (100, 450),
    textColor = (240, 240, 240),
)
A7 = level.Level(
    players = [
        p.Player(50.0, 575.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(0, 0, 50, 650, (100, 149, 237)),
        b.Entity(0, 0, 650, 50, (100, 149, 237)),
        b.Entity(600, 0, 650, 350, (100, 149, 237)),
        b.Entity(600, 525, 650, 650, (100, 149, 237)),
        b.Entity(0, 600, 650, 650, (100, 149, 237)),
        s.Cloud(425, 400, 650, 425),
        b.Entity(500, 150, 650, 200, (100, 149, 237)),
        b.Coin(200, 350,(123, 104, 238)),
        b.Entity(50, 50, 250, 100, (100, 149, 237)),
        b.Entity(275, 550, 325, 600, (100, 149, 237)),
        s.NullCube(350, 350),
        b.Coin(350, 250,(123, 104, 238)),
        b.Coin(150, 375,(123, 104, 238)),
        b.Entity(0, 375, 150, 425, (100, 149, 237)),
    ],
    background = (0, 0, 80),
    text = "7.Amoeba",
    textLocation = (100, 150),
    textColor = (240, 240, 240),
)
A8 = level.Level(
    players = [
        p.Player(50.0, 575.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(0, 600, 500, 650, (100, 149, 237)),
        b.Entity(0, 225, 50, 600, (100, 149, 237)),
        s.Cloud(50, 225, 175, 250),
        b.Entity(600, 225, 650, 650, (100, 149, 237)),
        s.Cloud(475, 225, 600, 250),
        s.NullCube(575, 325),
        b.Coin(325, 325,(123, 104, 238)),
        b.Coin(325, 575,(123, 104, 238)),
        b.Coin(325, 200,(123, 104, 238)),
        b.Entity(475, 0, 650, 50, (100, 149, 237)),
        b.Coin(325, 50,(123, 104, 238)),
        s.NullCube(50, 50),
    ],
    background = (0, 0, 80),
    text = "8.Ladder",
    textLocation = (225, 425),
    textColor = (240, 240, 240),
)
A9 = level.Level(
    players = [
        p.Player(125.0, 50.0,(102, 205, 170)),
    ],
    levelObjects = [
        b.Entity(0, 0, 300, 50, (100, 149, 237)),
        s.Cloud(50, 225, 250, 250),
        b.Entity(0, 375, 50, 650, (100, 149, 237)),
        b.Entity(0, 600, 650, 650, (100, 149, 237)),
        b.Entity(600, 375, 650, 650, (100, 149, 237)),
        b.Coin(375, 50,(123, 104, 238)),
        b.Coin(375, 200,(123, 104, 238)),
        b.Coin(375, 575,(123, 104, 238)),
        s.NullCube(575, 200),
        s.NullCube(575, 50),
        b.Coin(575, 125,(123, 104, 238)),
        b.Coin(575, 0,(123, 104, 238)),
    ],
    background = (0, 0, 80),
    text = "9.Redundancy",
    textLocation = (125, 350),
    textColor = (240, 240, 240),
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
    background = (0, 0, 30),
)
