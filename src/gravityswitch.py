#GRAVITY SWITCH 2.0 Main File
#By Javin Zipkin
import pygame
from lib import gameStateInfo as gs
from lib import utility as u
import math
from lib import constants as c

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

#pygame variables 
clock = pygame.time.Clock()
screen = pygame.display.set_mode([c.SCREEN_WIDTH, c.SCREEN_HEIGHT])
pygame.display.set_caption("Gravity Switch 2.0")
done = False
frames = 0

mainStatus = gs.GameStateInfo(screen)
while not mainStatus.quit:
    clock.tick()
    mainStatus.tickTime = clock.get_time() 

    # All displays
    mainStatus.displayProperMode()
    
    # All sources of user input
    mainStatus.mouseX = mouseX = pygame.mouse.get_pos()[0]
    mainStatus.mouseY = mouseY = pygame.mouse.get_pos()[1]
    for event in pygame.event.get(): 
        mainStatus.process(event)
    # All game logic
    mainStatus.update()
    # Debug: Display FPS
    u.screenText(10, 10, screen, "FPS: " + str(int(clock.get_fps())), 15)
    pygame.display.flip()

mainStatus.levelDumpFile.write(mainStatus.level.toString())
mainStatus.levelDumpFile.close()
pygame.quit()