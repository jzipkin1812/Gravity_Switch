#GRAVITY SWITCH 2.0 Main File
#By Javin Zipkin
import pygame
import random
from lib import gameStateInfo as gs
from lib import player
from lib import entity
from lib import utility as u
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

    # Background handling
    screen.fill((0, 0, 0))
    # All displays
    mainStatus.displayProperMode()
    
    # All sources of user input
    mainStatus.mouseX = mouseX = pygame.mouse.get_pos()[0]
    mainStatus.mouseY = mouseY = pygame.mouse.get_pos()[1]
    for event in pygame.event.get(): 
        mainStatus.process(event)
    
    # All game logic
    mainStatus.update()

    # Debug: Display mouse position x and y
    u.screenText(10, 10, screen, "x: " + str(mouseX) + " / y: " + str(mouseY), 20)
    # Debug: Display FPS
    u.screenText(10, 40, screen, "FPS: " + str(int(clock.get_fps())), 20)
    pygame.display.flip()
pygame.quit()