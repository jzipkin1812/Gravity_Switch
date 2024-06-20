import pygame
from . import premadeLevels
class GameStateInfo:
    def __init__(self, pygameScreen, backgroundColor = (120, 120, 225)):
        # Pygame variables
        self.quit: bool = False
        self.frames: int = 0
        self.screen: pygame.Surface = pygameScreen
        self.screenWidth: int = self.screen.get_width()
        self.screenHeight: int = self.screen.get_height()
        # Aesthetic variables
        self.backgroundColor = backgroundColor
        # Mode functions
        self.mode = "Gameplay"
        # For each mode, we display different things.
        self.modeDisplayDict = {
            "Title Screen" : self.displayBackground,
            "Gameplay" : self.displayLevel
        }
        # Gameplay statuses
        self.level = premadeLevels.tutorial

    def update(self):
        # Increment gameInfo state
        self.frames += 1
        self.level.update()
        
        

    def displayProperMode(self):
        self.modeDisplayDict[self.mode]()

    def displayBackground(self):
        self.screen.fill(self.backgroundColor)
    
    def displayLevel(self):
        self.displayBackground()
        self.level.display(self.screen)
    
    def process(self, event: pygame.event.Event):
        # Clicking x button
        if event.type == pygame.QUIT:
            self.quit = True

        # Clicking the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        
        # Key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
            if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT,
                             pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                print("KEYYY")
                for p in self.level.players:
                    p.keyMove(event.key)
        
