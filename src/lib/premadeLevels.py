from . import level
from . import player as p
from . import entity as b

tutorial = level.Level( 
    players = [ 
        p.Player(300, 300) 
    ],
    levelObjects = [
        b.Entity(50, 100, 500, 150),
        b.Entity(100, 500, 200, 550)
    ]
)