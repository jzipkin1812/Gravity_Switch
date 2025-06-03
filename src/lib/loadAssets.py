import pygame
import os
from . import utility as u

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

path = os.path.join(os.getcwd(), "lib", "assets")

titleImage = pygame.image.load(os.path.join(path, "titleScreen.png"))
levelSelectImage = pygame.image.load(os.path.join(path, "levelSelect.png"))
gameOverImage = pygame.image.load(os.path.join(path, "gameover.png"))
howToPlayImage = pygame.image.load(os.path.join(path, "howToPlay.png"))
