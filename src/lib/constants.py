SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
SCREEN_SIZE = 650
GRID_SIZE = 25
GAME_SPEED = 0.5
LEVELTEXTSIZE = 45

colorsWorldA = {
    "platform" : (100, 149, 237),
    "player" : (102, 205, 170),
    "inverted" : (205, 170, 102),
    "special" : (250, 0, 200),
    "coin" : (123, 104, 238),
    "cloud" : (220, 220, 220),
    "background" : (0, 0, 80),
    "text" : (240, 240, 240),
    "gridPlatforms" : False
}

colorsWorldB = {
    "platform" : (85, 51, 51),
    "player" : (255, 255, 68),
    "inverted" : (68, 255, 255),
    "special" : (240, 25, 5),
    "coin" : (204, 68, 34),
    "cloud" : (234, 218, 181),
    "background" : (255, 102, 0),
    "text" : (0, 0, 0),
    "gridPlatforms" : False
}

colorsWorldC = {
    "platform" : (49, 87, 54),
    "player" : (89, 129, 45),
    "inverted" : (45, 89, 129),
    "special" : (144, 169, 85),
    "coin" : (144, 69, 85),
    "cloud" : (236, 243, 158),
    "background" : (19, 42, 19),
    "text" : (150, 150, 150),
    "gridPlatforms" : False
}

colorsWorldD = {
    "platform" : (113, 113, 140),
    "player" : (60, 60, 60),
    "inverted" : (255, 255, 224),
    "special" : (144, 169, 85),
    "coin" : (128, 0, 128),
    "cloud" : (255, 255, 224),
    "background" : (93, 136, 226),
    "text" : (30, 30, 30),
    "gridPlatforms" : False
}

colorsWorldE = {
    "platform" : (205, 133, 63),
    "player" : (100, 149, 237),
    "inverted" : (255, 255, 224),
    "special" : (144, 169, 85),
    "coin" : (255, 165, 0),
    "cloud" : (255, 255, 224),
    "background" : (240, 223, 121),
    "text" : (0, 0, 255),
    "gridPlatforms" : False
}

colorsWorldF = {
    "platform" : (198, 255, 0),
    "player" : (255, 0, 171),
    "inverted" : (0, 255, 104),
    "special" : (255, 243, 179),
    "coin" : (255, 255, 0),
    "cloud" : (255, 255, 224),
    "background" : (125, 28, 148),
    "text" : (255, 243, 179),
    "gridPlatforms" : True
}


colorsWorldChallenge = {
    "platform" : (255, 255, 224),
    "player" : (245, 0, 0),
    "inverted" : (0, 0, 245),
    "special" : (144, 169, 85),
    "coin" : (20, 240, 20),
    "cloud" : (220, 220, 220),
    "background" : (20, 20, 20),
    "text" : (255, 255, 255),
}

allColors = [
    colorsWorldA,
    colorsWorldB,
    colorsWorldC,
    colorsWorldD,
    colorsWorldE,
    colorsWorldF,
]


GLOBALCOLORS = colorsWorldF

LEVEL_SQUARE_SIZE = 75
levelSelectWorldA = [
(40, 208),
(196, 186),
(326, 147),
(464, 182),
(549, 271),
(434, 321),
(308, 280),
(169, 300),
(44, 380),
(165, 436),
]

levelSelectWorldB = [
(41, 553),
(146, 606),
(277, 617),
(391, 533),
(532, 556),
(459, 654),
(322, 750),
(373, 903),
(230, 851),
(132, 803),

]

levelSelectWorldC = [
(35, 978),
(149, 1048),
(277, 1077),
(419, 1082),
(535, 1029),
(555, 1183),
(425, 1237),
(293, 1283),
(149, 1306),
(239, 1410),
]


levelSelectWorldD = [
(410, 1449),
(537, 1415),
(522, 1537),
(381, 1593),
(492, 1681),
(337, 1729),
(439, 1801),
(374, 1929),
(267, 1856),
(237, 1982),
]

levelSelectWorldE = [
(379, 2132),
(234, 2158),
(90, 2139),
(36, 2248),
(93, 2356),
(223, 2384),
(363, 2353),
(477, 2277),
(506, 2403),
(373, 2497),
]

levelSelectWorldF = [
(65, 2613),
(102, 2733),
(65, 2848),
(140, 2957),
(205, 2855),
(248, 2973),
(320, 2859),
(353, 2977),
(436, 2874),
(522, 2777),
]

levelSelectWorldChallenge = [
(311, 413),
(45, 697),
(77, 1418),
(142, 1829),
(528, 2147),
(308, 2652)
]

levelSelections = [levelSelectWorldA, 
                   levelSelectWorldB, 
                   levelSelectWorldC, 
                   levelSelectWorldD,
                   levelSelectWorldE,
                   levelSelectWorldF]


palleteSelections = {
    "Player" : [19, 117, 86, 172],
    "Entity" : [119, 121, 190, 189],
    "Coin" : [230, 122, 279, 170],
    "Nullcube" : [358, 125, 426, 180],
    "Cloud" : [464, 121, 642, 177],
    "Redirector" : [36, 218, 121, 287],
    "Antiplatform" : [201, 222, 329, 289],
    "Teleporter" : [382, 217, 519, 282],
    "Lever" : [555, 225, 623, 390],
    "BeatBlockA" : [18, 428, 136, 494],
    "BeatBlockB" : [152, 428, 273, 494],
    "Tar" : [16, 331, 132, 390],
    "InvertedPlayer" : [200, 328, 317, 387],
    "Resizer" : [302, 420, 397, 515],
    "Text" : [410, 429, 527, 495],
    "Stone" : [540, 422, 627, 509],
    "Quicksand" : [413, 325, 528, 424],
}