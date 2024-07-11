import pygame
import os
from . import utility as u
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

path = os.getcwd() + "\\lib\\assets\\"
titleImage = pygame.image.load(path + "titleScreen.png")
levelSelectImage = pygame.image.load(path + "levelSelect.png")
gameOverImage = pygame.image.load(path + "gameover.png")
howToPlayImage = pygame.image.load(path + "howToPlay.png")
