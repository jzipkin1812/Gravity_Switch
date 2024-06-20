#GRAVITY SWITCH 2.0 Main File
#By Javin Zipkin
import pygame
import random
from .lib import gameStateInfo as gs
from .lib import player
from .lib import block
from .lib import utility as u
import math

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

#Functions that correlate to specific game buttons

#pygame variables 
clock = pygame.time.Clock()
screen_width = 650
screen_height = 650
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Gravity Switch 2.0")
done = False
frames = 0

#The game state object carries almost all the information about everything going on in the game.
#To shorten the game loop, we will be updating the game state's instance variables,
#rather than variables local to this file.
mainStatus = gs.GameStateInfo(screen)

while not mainStatus.quit:
    clock.tick()
    mainStatus.tickTime = clock.get_time() 
    mainStatus.updateFrames()

    # Background handling
    screen.fill((0, 0, 0))
    # All displays
    mainStatus.displayProperMode()
    
    # All sources of user input
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    for event in pygame.event.get(): 
        # Clicking x button
        if event.type == pygame.QUIT:
            mainStatus.quit = True
        # Clicking the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        # Key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
            if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT] and len(mainStatus.buttons) > 0:
                pass
    
    # Update frame-by-frame stuff

    # Debug: Display mouse position x and y
    u.screenText(10, 10, screen, "x: " + str(mouseX) + " / y: " + str(mouseY), 20)
    # Debug: Display FPS
    u.screenText(10, 40, screen, "FPS: " + str(int(clock.get_fps())), 20)
    pygame.display.flip()
pygame.quit()