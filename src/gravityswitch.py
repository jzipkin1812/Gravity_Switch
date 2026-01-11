#GRAVITY SWITCH 2.0 Main File
#By Javin Zipkin

import os, sys

if hasattr(sys, "_MEIPASS"):
    os.chdir(sys._MEIPASS)  # run inside the bundle
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame
from lib import gameStateInfo as gs
from lib import utility as u
from lib import constants as c
from lib import loadAssets as a

import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame_gui.elements.ui_button import UIButton
from pygame.rect import Rect



pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

#pygame variables 
clock = pygame.time.Clock()
screen = pygame.display.set_mode([c.SCREEN_WIDTH, c.SCREEN_HEIGHT])
manager = pygame_gui.UIManager((c.SCREEN_WIDTH, c.SCREEN_WIDTH))

pygame.display.set_caption("Gravity Switch 2.0")
done = False
frames = 0

mainStatus = gs.GameStateInfo(screen, manager)
mainStatus.loadSaveFile(a.loadedSave)

while not mainStatus.quit:
    clock.tick(500)
    mainStatus.tickTime = clock.get_time() 

    # All displays
    mainStatus.displayProperMode()
    
    # All sources of user input
    mainStatus.mouseX = mouseX = pygame.mouse.get_pos()[0]
    mainStatus.mouseY = mouseY = pygame.mouse.get_pos()[1]
    allEvents = pygame.event.get()
    for event in allEvents:
        manager.process_events(event)
        mainStatus.process(event)
    # All game logic
    mainStatus.update()
    # Debug: Display FPS
    u.screenText(10, 10, screen, "FPS: " + str(int(clock.get_fps())), 15)
    # Draw special GUI elements (file selector)
    manager.update(mainStatus.tickTime)
    manager.draw_ui(screen)
    pygame.display.update()

mainStatus.levelDumpFile.write(mainStatus.level.toString())
mainStatus.levelDumpFile.close()
pygame.quit()

# SAVE the save file, represented by this 2D array:
with open(a.getSavePath(), "w") as f:
    for row in mainStatus.unlocked:
        f.write(" ".join(map(str, row)) + "\n")
