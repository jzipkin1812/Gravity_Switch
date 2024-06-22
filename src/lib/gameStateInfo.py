import pygame
from .premadeLevels import *
from . import level
from . import player
from . import entity
from . import specialEntities as special 
from .constants import *
class GameStateInfo:
    def __init__(self, pygameScreen):
        global GLOBALCOLORS
        # Pygame variables
        self.quit: bool = False
        self.frames: int = 0
        self.screen: pygame.Surface = pygameScreen
        self.screenWidth: int = self.screen.get_width()
        self.screenHeight: int = self.screen.get_height()
        self.mouseX: int = 0
        self.mouseY: int = 0
        # Aesthetic variables
        self.colors = GLOBALCOLORS = colorsWorldB
        # Mode functions
        self.mode: str = "Gameplay"
        # For each mode, we use different functions.
        self.modeDisplayDict = {
            "Title Screen" : self.displayBackground,
            "Gameplay" : self.displayLevel,
            "Level Editor" : self.displayLevelEditor,
            "Game Over" : self.displayGameOver,
        }
        self.modeInputDict = {
            "Title Screen" : self.processTitle,
            "Gameplay" : self.processGameplay,
            "Level Editor" : self.processEditor,
            "Game Over" : self.processGameOver,
        }
        # Gameplay statuses
        self.world: list[level.Level] = worldB
        self.levelNumber: int = 0
        self.level: level.Level = self.world[self.levelNumber]
        # self.level.background = (80, 0, 0)
        self.advance = True
        
        # Level editor info
        self.gridSize: int = GRID_SIZE
        self.point1: tuple = (0, 0)
        self.point2: tuple = (0, 0)
        self.levelDumpFile = open("levelDump.txt", "w")
        self.editDirection = "up"

    def update(self):
        self.frames += 1
        self.level.update()
        if (self.level.isComplete()) and self.advance:
            self.level.reset()
            self.levelNumber += 1
            self.level = self.world[self.levelNumber % len(self.world)] 
        elif (self.level.playerIsDead()):
            self.mode = "Game Over"

    def displayProperMode(self):
        self.modeDisplayDict[self.mode]()

    def displayBackground(self):
        self.screen.fill(self.colors["background"])
    
    def displayLevel(self):
        self.displayBackground()
        self.level.display(self.screen)
        
    def displayGameOver(self):
        self.screen.fill((0, 0, 0))
        self.screenText(50, 50, "Game Over...", 50)
        self.screenText(50, 150, "You flew off into infinity!", 50)
        self.screenText(50, 250, "Press any key to restart.", 50)

    
    def displayLevelEditor(self):
        self.advance = False
        self.displayBackground()
        self.level.display(self.screen)
        # 25 pixel grid
        for i in range(0, SCREEN_SIZE, self.gridSize):
            pygame.draw.line(self.screen, (75, 75, 75), (i, 0), (i, SCREEN_HEIGHT))
            pygame.draw.line(self.screen, (75, 75, 75), (0, i), (SCREEN_WIDTH, i))
        # pos1 indicator
        pygame.draw.circle(self.screen, (0, 0, 0), self.point1, 5)
        pygame.draw.circle(self.screen, (255, 255, 255), self.point2, 5)
    
    def process(self, event: pygame.event.Event):
        # Clicking x button
        if event.type == pygame.QUIT:
            self.quit = True
            
        self.modeInputDict[self.mode](event)
    
    def processGameOver(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            self.mode = "Gameplay"
            self.level.reset()
    
        
    def processGameplay(self, event: pygame.event.Event):
        # Clicking the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                self.mode = "Level Editor"
        # Key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
            if event.key == pygame.K_r:
                self.level.reset()
            if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT,
                             pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                for p in self.level.players:
                    if p.direction == "stop":
                        p.keyMove(event.key)
    
    def processTitle(self, event: pygame.event.Event):
        pass

    def processEditor(self, event: pygame.event.Event):
        a = self.point1
        b = self.point2
        # Keys add objects to level
        if event.type == pygame.KEYDOWN:
            # Erase
            if event.key == pygame.K_BACKSPACE:
                self.level.levelObjects = [e for e in self.level.levelObjects if not 
                                           (e.x1 <= a[0] <= e.x2 and e.y1 <= a[1] <= e.y2)]
                self.level.players = [p for p in self.level.players if not 
                                      (p.x == a[0] and p.y == a[1])]
            if event.key == pygame.K_SPACE:
                print(self.colors["platform"])
                self.level.levelObjects.append(entity.Entity(a[0], a[1], 
                                                            b[0], b[1], self.colors["platform"]))
            if event.key == pygame.K_a:
                self.level.levelObjects.append(special.Antiplatform(a[0], a[1], 
                                                            b[0], b[1]))
            if event.key == pygame.K_l:
                self.level.levelObjects.append(special.Cloud(a[0], a[1], 
                                                            b[0], b[1]))
            if event.key == pygame.K_p:
                self.level.players.append(player.Player(a[0], a[1], self.colors["player"], self.gridSize))
            if event.key == pygame.K_c:
                self.level.levelObjects.append(entity.Coin(a[0], a[1], self.colors["coin"]))
            if event.key == pygame.K_n:
                self.level.levelObjects.append(special.NullCube(a[0], a[1]))
            # Write/Save
            if event.key == pygame.K_w:
                self.levelDumpFile.write(self.level.toString())
            # Change direction for directed objects
            if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                self.editDirection = player.directionDict[event.key]
                self.level.levelObjects.append(special.Redirector(a[0], a[1], self.editDirection))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Middle Mouse: Swap modes and solidify level contents
            if event.button == 2:
                self.mode = "Gameplay"
                self.level.solidify()
            # Left mouse: Set point1
            if event.button == 1:
                self.point1 = (self.mouseX - (self.mouseX % self.gridSize), self.mouseY - (self.mouseY % self.gridSize))
            # Right mouse: Set point2
            if event.button == 3:
                self.point2 = (self.mouseX - (self.mouseX % self.gridSize) + self.gridSize, self.mouseY - (self.mouseY % self.gridSize)  + self.gridSize)
    
    def screenText(self, x, y, text = "Default", size = 100, color = [250, 250, 250], background = None):
        tempFont = pygame.font.SysFont("msgothic", size)
        tempText = tempFont.render(text, True, color, background)
        self.screen.blit(tempText, (x, y))
            
        
        
