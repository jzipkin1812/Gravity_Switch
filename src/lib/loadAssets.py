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


# Path to the assets directory (inside lib/assets)
assets_dir = resource_path("assets")

# Load images
titleImage = pygame.image.load(os.path.join(assets_dir, "titleScreen.png"))
levelSelectImage = pygame.image.load(os.path.join(assets_dir, "levelSelect.png"))
gameOverImage = pygame.image.load(os.path.join(assets_dir, "gameover.png"))
howToPlayImage = pygame.image.load(os.path.join(assets_dir, "howToPlay.png"))
