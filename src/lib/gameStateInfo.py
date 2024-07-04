import pygame
from .premadeLevels import *
from . import level
from . import player
from . import entity
from . import specialEntities as special 
from .constants import *
from .loadAssets import *
class GameStateInfo:
    def __init__(self, pygameScreen):
        # Pygame variables
        self.quit: bool = False
        self.frames: int = 0
        self.screen: pygame.Surface = pygameScreen
        self.screenWidth: int = self.screen.get_width()
        self.screenHeight: int = self.screen.get_height()
        self.mouseX: int = 0
        self.mouseY: int = 0
        self.timer = pygame.time.Clock()
        # Aesthetic variables
        self.colors = colorsWorldA
        # Mode functions
        self.mode: str = "Title Screen"
        # For each mode, we use different functions.
        self.modeDisplayDict = {
            "Title Screen" : self.displayTitle,
            "Gameplay" : self.displayLevel,
            "Level Editor" : self.displayLevelEditor,
            "Game Over" : self.displayGameOver,
            "Level Select" : self.displayLevelSelect
        }
        self.modeInputDict = {
            "Title Screen" : self.processTitle,
            "Gameplay" : self.processGameplay,
            "Level Editor" : self.processEditor,
            "Game Over" : self.processGameOver,
            "Level Select" : self.processLevelSelect
            
        }
        # Gameplay statuses
        self.world: list[level.Level] = worldA
        self.levelNumber: int = 0
        self.level: level.Level = self.world[self.levelNumber]
        # self.level.background = (80, 0, 0)
        self.advance: bool = True
        # Level editor info
        self.gridSize: int = GRID_SIZE
        self.point1: tuple = (0, 0)
        self.point2: tuple = (0, 0)
        self.levelDumpFile = open("levelDump.txt", "w")
        self.editDirection = "up"
        self.editUses = 0
        self.doAdvance = True
        # Level select info
        self.scrollMod: int = 0

    def update(self):
        self.frames += 1
        
        # Player movement occurs in the update, with speed independent of framerate.
        self.timer.tick()
        self.level.update(self.timer.get_time())
        
        if (self.level.isComplete()) and self.advance:
            self.level.reset()
            self.levelNumber += 1
            self.level = self.world[self.levelNumber % len(self.world)] 
        elif (self.level.playerIsDead()):
            self.mode = "Game Over"
            self.level.reset()

    def displayProperMode(self):
        self.modeDisplayDict[self.mode]()
    def displayTitle(self):
        self.screen.blit(titleImage, (0,0))
    def displayBackground(self):
        self.screen.fill(self.level.background)
    def displayLevelSelect(self):
        self.screen.blit(levelSelectImage, (0, self.scrollMod))
    
    def displayLevel(self):
        self.displayBackground()
        self.level.display(self.screen)
        
    def displayGameOver(self):
        self.screen.fill((0, 0, 0))
        self.screenText(50, 50, "Game Over...", 25)
        self.screenText(50, 150, "You flew off into infinity!", 25)
        self.screenText(50, 250, "Press any key to restart.", 25)

    
    def displayLevelEditor(self):
        self.advance = False
        self.displayBackground()
        self.level.display(self.screen)
        # 25 pixel grid
        for i in range(0, SCREEN_SIZE, self.gridSize):
            pygame.draw.line(self.screen, (75, 75, 75), (i, 0), (i, SCREEN_HEIGHT))
            pygame.draw.line(self.screen, (75, 75, 75), (0, i), (SCREEN_WIDTH, i))
        # editor pointers
        pygame.draw.circle(self.screen, (255, 0, 0), self.point1, 5)
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
        # For multiple players, check if everyone is stopped.
        allStopped = True
        for p in self.level.players:
            if p.direction != "stop":
                allStopped = False
        # Clicking the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                self.level.reset()
                self.mode = "Level Editor"
        # Key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
            elif event.key == pygame.K_r:
                self.level.reset()
            elif (event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT,
                             pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]) and allStopped:
                for p in self.level.players:
                    p.keyMove(event.key)
            elif event.key == pygame.K_ESCAPE:
                self.mode = "Title Screen"
            elif event.key == pygame.K_SLASH:
                self.level.reset()
                self.mode = "Level Editor"
    
    def processTitle(self, event: pygame.event.Event):
        #PLAY: (81, 183) to (322, 265)
        #LVL SELECT: (354, 322) to (597, 402)

        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_SPACE:
                self.mode = "Gameplay"
            if event.key == pygame.K_BACKSPACE:
                self.doAdvance = not self.doAdvance
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # title screen BUTTONS
                if 81 <= self.mouseX <= 322 and 183 <= self.mouseY <= 265:
                    self.mode = "Gameplay"
                elif 354 <= self.mouseX <= 597 and 322 <= self.mouseY <= 402:
                    self.mode = "Level Select"
                elif 155 <= self.mouseX <= 395 and 457 <= self.mouseY <= 538:
                    self.mode = "Level Editor"
                    self.level = editorLevel
                    self.advance = False
                    self.world = worldA
                    self.levelNumber = 0
    
    def processLevelSelect(self, event: pygame.event.Event):        
        if event.type == pygame.MOUSEWHEEL:
            self.scrollMod += 20 * event.y
            self.scrollMod = min(0, self.scrollMod)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.mode = "Title Screen"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.selectLevel()

    def processEditor(self, event: pygame.event.Event):
        a = self.point1
        b = self.point2
        # Adjust points if necessary
        # if(a[0] - 5 > b[0] or a[1] - 5 > b[1]):
        #     temp = (a[0], a[1])
        #     self.point1 = self.point2
        #     self.point2 = temp
        # Keys add objects to level
        if event.type == pygame.KEYDOWN:
            # Erase
            if event.key == pygame.K_BACKSPACE:
                self.level.erase(a[0], a[1])
            # Undo
            if event.key == pygame.K_z:
                if len(self.level.levelObjects) > 0:
                    self.level.levelObjects.pop()
            elif event.key == pygame.K_SPACE:
                self.level.levelObjects.append(entity.Entity(a[0], a[1], 
                                                            b[0], b[1], self.colors["platform"]))
            elif event.key == pygame.K_t:
                self.level.levelObjects.append(special.Teleporter(a[0], a[1], 
                                                            b[0], b[1], self.editUses))
            elif event.key == pygame.K_a:
                self.level.levelObjects.append(special.Antiplatform(a[0], a[1], 
                                                            b[0], b[1], self.colors["platform"]))
            elif event.key == pygame.K_o:
                self.level.levelObjects.append(special.Cloud(a[0], a[1], 
                                                            b[0], b[1]))
            elif event.key == pygame.K_l:
                self.level.levelObjects.append(special.Lever(a[0], a[1], 
                                                            b[0], b[1], self.editDirection))
            elif event.key == pygame.K_r:
                self.level.levelObjects.append(special.Tar(a[0], a[1], 
                                                            b[0], b[1], self.editDirection))
            elif event.key == pygame.K_p:
                self.level.players.append(player.Player(a[0], a[1], self.colors["player"], self.gridSize, False))
            elif event.key == pygame.K_v:
                self.level.players.append(player.Player(a[0], a[1], self.colors["inverted"], self.gridSize, True))    
                
                
            elif event.key == pygame.K_c:
                self.level.levelObjects.append(entity.Coin(a[0], a[1], self.colors["coin"]))
            elif event.key == pygame.K_n:
                self.level.levelObjects.append(special.NullCube(a[0], a[1]))
            # Text Location
            elif event.key == pygame.K_TAB:
                self.level.textLocation = (a[0], a[1])
                self.level.textColor = self.colors["text"]
                self.level.text = input()
            
            # Write/Save
            elif event.key == pygame.K_w:
                self.levelDumpFile.write(self.level.toString())
            # Change direction for directed objects
            elif event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                self.editDirection = player.directionDict[event.key]
            elif event.key == pygame.K_i:
                self.level.levelObjects.append(special.Redirector(a[0], a[1], self.editDirection))
            # Change uses for teleporters and possibly other objects in the future
            elif event.key == pygame.K_0:
                self.editUses = 0
            elif event.key == pygame.K_1:
                self.editUses = 1
            elif event.key == pygame.K_2:
                self.editUses = 2
            elif event.key == pygame.K_3:
                self.editUses = 3
            elif event.key == pygame.K_4:
                self.editUses = 4
                
            
            elif event.key == pygame.K_ESCAPE:
                self.mode = "Title Screen"
            elif event.key == pygame.K_SLASH:
                self.mode = "Gameplay"
                self.level.solidify()
        
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
    
    def selectLevel(self):
        mouseModY = self.mouseY - self.scrollMod
        for planet, selector in worldInfo:
            for i, (x, y) in enumerate(selector):
                if (x <= self.mouseX <= x + LEVEL_SQUARE_SIZE) and \
                (y <= mouseModY <= y + LEVEL_SQUARE_SIZE):
                    self.beamDown(planet, i)
    
    def beamDown(self, destination, num):
        self.levelNumber = num
        self.world = destination
        self.level = destination[num]
        self.level.reset()
        self.advance = self.doAdvance
        self.mode = "Gameplay"
        if destination == worldA:
            self.colors = colorsWorldA
        elif destination == worldB:
            self.colors = colorsWorldB
        elif destination == worldC:
            self.colors = colorsWorldC
        elif destination == worldD:
            self.colors = colorsWorldD
        elif destination == worldChallenge:
            self.colors = colorsWorldChallenge
                   
        
        
        
