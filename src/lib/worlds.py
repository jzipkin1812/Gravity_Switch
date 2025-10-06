from . import level
from . import player as p
from . import entity as b
from . import specialEntities as s
from .constants import *

from .levels.worldA import *
from .levels.worldB import *
from .levels.worldC import *
from .levels.worldD import *
from .levels.worldE import *
from .levels.worldF import *
from .levels.challenge import *

editorLevel = level.Level(

)

worldA = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]
worldB = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10]
worldC = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10]
worldD = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10]
worldE = [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10]
worldF = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10]
worldChallenge = [ChallengeA, ChallengeB, ChallengeC, ChallengeD, ChallengeE, ChallengeF]

worldInfo = [
    (worldA, levelSelectWorldA),
    (worldB, levelSelectWorldB),
    (worldC, levelSelectWorldC),
    (worldD, levelSelectWorldD),
    (worldE, levelSelectWorldE),
    (worldF, levelSelectWorldF),
    (worldChallenge, levelSelectWorldChallenge)
]

def nextWorld(w):
    if w == worldA:
        return(worldB)
    elif w == worldB:
        return(worldC)
    elif w == worldC:
        return(worldD)
    elif w == worldD:
        return(worldE)
    elif w == worldE:
        return(worldF)
    elif w == worldChallenge:
        return(worldChallenge)
    else:
        return(worldA)