import pygame
import os
import sys
from . import utility as u

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()


def resource_path(relative_path: str) -> str:
    """
    Return the absolute path to a resource.
    Works for development and for PyInstaller .exe/.app bundles.
    """
    if hasattr(sys, "_MEIPASS"):
        # Running from PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running from source; base this on the current file’s directory
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

def loadImage(name : str):
    return pygame.image.load(os.path.join(assets_dir, "img", name))

def loadSound(name : str):
    return pygame.mixer.Sound(os.path.join(assets_dir, "sfx", name))

# Path to the assets directory (inside lib/assets)
assets_dir = resource_path("assets")

# Load images
titleImage = loadImage("titleScreen.png")
levelSelectImage = loadImage("levelSelect.png") 
gameOverImage = loadImage("gameover.png") 
howToPlayImage = loadImage("howToPlay.png") 

# Load sounds
# Channels: 0 = Music, 1 = collision SFX, 2 = special SFX
bumpSounds = [
    loadSound("bump1.wav"),
    loadSound("bump2.wav"),
    loadSound("bump3.wav"),
    loadSound("bump4.wav"),
    loadSound("bump5.wav"),
    loadSound("bump6.wav"),
]

redirectorSounds = {
    "down" : loadSound("redirectorDown.wav"),
    "up" : loadSound("redirectorUp.wav"),
    "left" : loadSound("redirectorLeft.wav"),
    "right" : loadSound("redirectorRight.wav"),
}

nullcubeSound = loadSound("nullcube.wav")
coinSound = loadSound("coin.wav")
deathSound = loadSound("death.wav")
teleporterSounds = [
    loadSound("teleport0.wav"),
    loadSound("teleport1.wav"),
    loadSound("teleport2.wav"),
    loadSound("teleport3.wav"),
]
cloudSound = loadSound("cloud.wav")
leverSound = loadSound("lever.wav")
antiplatformSound = loadSound("antiplatform.wav")

growingSound = loadSound("growing.wav")
shrinkingSound = loadSound("shrinking.wav")
beatBlockSound = loadSound("pop.wav")

levelCompleteSounds = [
    loadSound(f"levelComplete{i}.wav") for i in range(1, 11)
]
worldCompleteSound = loadSound("worldComplete.wav")
sandThudSound = loadSound("sandthud.wav")
stoneSlideSound = loadSound("stone.wav")
challengeCompleteSound = loadSound("challengeComplete.wav")

locks = [loadImage("lock" + str(i) + ".png") for i in range(6)]

def getSavePath():
    # Windows
    if sys.platform == "win32": 
        base = os.environ.get("APPDATA", os.path.expanduser("~"))
    # Mac
    elif sys.platform == "darwin":
        base = os.path.expanduser("~/Library/Application Support")
    # Linux
    else:
        base = os.path.expanduser("~/.local/share")

    save_dir = os.path.join(base, "GravitySwitchData")
    os.makedirs(save_dir, exist_ok=True)
    return os.path.join(save_dir, "gsSave.txt")

savePath = getSavePath()
if os.path.exists(savePath):
    print("FOUND SAVE FILE AT", savePath)
    try:
        with open(savePath, "r") as f:
            loadedSave = [
                [int(x) for x in line.strip().split()]
                for line in f
                if line.strip()
            ]
    except:
        print("The save file is malformed. Defaulting to new save.")
        loadedSave = [[0 for _ in range(11)] for _ in range(11)]
else:
    print("No save data found.")
    # Create a default save if none exists
    loadedSave = [[0 for _ in range(11)] for _ in range(11)]

