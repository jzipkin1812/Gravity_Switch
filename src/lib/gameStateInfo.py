import pygame
class GameStateInfo:
    def __init__(self, pygameScreen, backgroundColor = (100, 100, 200)):
        # Pygame variables
        self.quit: bool = False
        self.frames: int = 0
        self.screen: pygame.Surface = pygameScreen
        self.screenWidth: int = self.screen.get_width()
        self.screenHeight: int = self.screen.get_height()
        # Aesthetic variables
        self.backgroundColor = backgroundColor
        # Mode functions
        self.mode = "Title Screen"
        # For each mode, we display different things.
        self.modeDisplayDict = {
            "Title Screen" : self.displayBackground
        }

    def updateFrames(self):
        self.frames += 1

    def displayProperMode(self):
        self.modeDisplayDict[self.mode]()

    def displayBackground(self):
        self.screen.fill(self.backgroundColor)
