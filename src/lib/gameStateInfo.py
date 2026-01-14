import tkinter
import tkinter.filedialog

import pygame
from .worlds import *
from . import level
from . import player
from . import entity
from . import specialEntities as special 
from . import utility as u
from .constants import *
from .loadAssets import *
import json
import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame.rect import Rect

import pygame_textinput

class GameStateInfo:
    manager = pygame_gui.UIManager((800, 600))

    def __init__(self, pygameScreen : pygame.Surface, pygameManager : pygame_gui.UIManager):
        # Pygame variables
        self.quit: bool = False
        self.frames: int = 0
        self.screen: pygame.Surface = pygameScreen
        self.manager: pygame_gui.UIManager = pygameManager
        self.screenWidth: int = self.screen.get_width()
        self.screenHeight: int = self.screen.get_height()
        self.mouseX: int = 0
        self.mouseY: int = 0
        self.timer = pygame.time.Clock()
        # Global settings variables
        self.showFPS = False
        # GUI variables
        self.saveSelector = None
        self.loadSelector = None
        self.textinput = None

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
            "Level Select" : self.displayLevelSelect,
            "How To Play" : self.displayHowToPlay,
            "Palette" : self.displayPalette,
            "Editor Controls" : self.displayEditorControls,
        }
        self.modeInputDict = {
            "Title Screen" : self.processTitle,
            "Gameplay" : self.processGameplay,
            "Level Editor" : self.processEditor,
            "Game Over" : self.processGameOver,
            "Level Select" : self.processLevelSelect,
            "How To Play" : self.processHowToPlay,
            "Palette" : self.processPalette,
            "Editor Controls" : self.processEditorControls,
        }
        # Gameplay statuses
        self.world: list[level.Level] = worldA
        self.levelNumber: int = 0
        self.level: level.Level = self.world[self.levelNumber]
        # self.level.background = (80, 0, 0)
        self.advance: bool = True
        # Level editor info
        self.gridSize: int = GRID_SIZE
        self.point1: list = [0, 0]
        self.point2: list = [0, 0]
        self.levelDumpFile = open("levelDump.txt", "w")
        self.editDirection = "up"
        self.editUses = 0
        self.doAdvance = True
        self.editorBrush = "Coin"
        self.editorColor = None
        self.colorIndicator = None
        # Level select info
        self.scrollMod: int = 0
        # Unlocked levels
        self.unlocked : list[list[int]] = [[0 for _ in range(11)] for _ in range(6)]
        for row in self.unlocked:
            row[0] = 1
        # ???????
        self.secret = []
        self.code = [pygame.K_j, pygame.K_a, pygame.K_v, pygame.K_i, pygame.K_n]
        self.edoc = [pygame.K_n, pygame.K_i, pygame.K_v, pygame.K_a, pygame.K_j]
        self.coords1 = (0, 0)
        self.coords2 = (0, 0)
        # Start the music!
        u.playMusic(worldAMusic)
    
    def update(self):
        self.frames += 1
        
        # Player movement occurs in the update, with speed independent of framerate.
        self.timer.tick()
        self.level.update(self.timer.get_time())
        # Advancement from normal levels
        if (self.level.isComplete()) and self.advance:
            self.nextLevel()
            # Completing challenge levels sends you back to the level select screen.
            if (self.world == worldChallenge):
                self.mode = "Level Select"
                u.stopMusic()
        # Advancement from editor levels
        elif (self.level.isComplete()) and (self.level.isBeatable()):
            self.level.reset()
            u.playSound(2, editorCompleteSound)
            
        # Death
        elif (self.level.playerIsDead()):
            u.playSound(2, deathSound)
            pygame.mixer.Channel(1).stop()
            u.pauseMusic()
            self.mode = "Game Over"
            self.level.reset()
    
    def nextLevel(self):
        self.level.reset()
        self.levelNumber += 1

        # Unlock next level
        # Upon clearing a world, unlock its challenge level
        if not (self.world is worldChallenge):
            worldIndex = worlds.index(self.world)
            self.unlocked[worldIndex][self.levelNumber] = 1

        # Play sfx and change screen
        if self.world is worldChallenge:
            self.levelNumber -= 1
            u.playSound(3, challengeCompleteSound)
        elif self.levelNumber >= 10:
            newWorld, newScrollMod = nextWorld(self.world)
            if newScrollMod <= 0:
                self.scrollMod = newScrollMod
            newLevelNumber = 0
            self.level.reset()
            self.beamDown(newWorld, newLevelNumber)
            u.pauseMusic()
            u.playSound(3, worldCompleteSound)
            self.mode = "Level Select"
            return
        else:
            u.playSound(3, levelCompleteSounds[self.levelNumber - 1])
        
        self.beamDown(self.world, self.levelNumber)
    
    def displayProperMode(self):
        self.modeDisplayDict[self.mode]()
    
    def displayTitle(self):
        self.screen.blit(titleImage, (0,0))

        # Slashes over sound toggle buttoms
        if not u.doSound:
            pygame.draw.line(self.screen, (255, 0, 0), (538, 18), (572, 52), 3)
            pygame.draw.line(self.screen, (255, 0, 0), (538, 52), (572, 18), 3)
        if not u.doMusic:
            pygame.draw.line(self.screen, (255, 0, 0), (598, 18), (632, 52), 3)
            pygame.draw.line(self.screen, (255, 0, 0), (598, 52), (632, 18), 3)
    
    def displayLevelSelect(self):
        # Main background
        self.screen.blit(levelSelectImage, (0, self.scrollMod))
        # Lock overlays
        offset = 5
        for i in range(6):
            levelsPos = levelSelections[i]
            lock = locks[i]
            challengePos = levelSelectWorldChallenge[i]
            # Locks for regular levels
            for levelNum in range(10):
                if not self.unlocked[i][levelNum]:
                    pos = levelsPos[levelNum]
                    self.screen.blit(lock, (pos[0] + offset, pos[1] + self.scrollMod + offset))
            # Lock for challenge level
            if not self.unlocked[i][10]:
                self.screen.blit(lock, (challengePos[0] + offset, challengePos[1] + self.scrollMod + offset))
    
    def displayLevel(self):
        self.level.display(self.screen)
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            self.displayGrid()
    
    def displayGameOver(self):
        self.screen.blit(gameOverImage, (0, 0))
    
    def displayEditorControls(self):
        self.screen.blit(editorControlsImage, (0, 0))
    
    def displayGrid(self):
        # 25 pixel grid
        for i in range(0, SCREEN_SIZE, self.gridSize):
            pygame.draw.line(self.screen, (75, 75, 75), (i, 0), (i, SCREEN_HEIGHT))
            pygame.draw.line(self.screen, (75, 75, 75), (0, i), (SCREEN_WIDTH, i))
    
    def displayLevelEditor(self):
        self.advance = False
        self.level.display(self.screen)
        self.displayGrid()
        # editor pointers
        pygame.draw.circle(self.screen, (255, 0, 0), self.point1, 5)
        pygame.draw.circle(self.screen, (255, 255, 255), self.point2, 5)
        # text ui
        if self.textinput:
            self.screen.blit(self.textinput.surface, (self.point1[0], self.point1[1]))

    def displayPalette(self):
        self.screen.blit(paletteImage, (0,0))
        x1, y1, x2, y2 = palleteSelections[self.editorBrush]
        u.dashedRect(self.screen, (255, 255, 255), x1, y1, x2, y2, 2)

        if self.editorColor:
            u.betterRect(self.screen, 
                         self.colorIndicator[0], 
                         self.colorIndicator[1], 
                         self.colorIndicator[2], 
                         self.colorIndicator[3],
                         (255, 255, 255), 2)

        # u.dashedRect(self.screen, (255, 255, 255), self.coords1[0], self.coords1[1], self.coords2[0], self.coords2[1], 2)

    def processPalette(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            self.mode = "Level Editor"
            # Upon leaving the palette, color the level according to theme.
            if self.editorColor:
                self.level.colorFromTheme(self.editorColor)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.coords1 = (self.mouseX, self.mouseY)
                # Select a brush
                for (brush, coords) in palleteSelections.items():
                    if coords[0] <= self.mouseX <= coords[2] and coords[1] <= self.mouseY <= coords[3]:
                        self.editorBrush = brush
                # Select a color theme
                for worldNum in range(6):
                    x1 = 145 + 80 * worldNum
                    y1 = 546
                    x2 = x1 + 75
                    y2 = y1 + 75
                    if x1 <= self.mouseX <= x2 and y1 <= self.mouseY <= y2:
                        self.editorColor = allColors[worldNum]
                        self.colors = self.editorColor
                        self.colorIndicator = [x1, y1, x2, y2]
            else:
                self.coords2 = (self.mouseX, self.mouseY)
                print([self.coords1[0], self.coords1[1], self.coords2[0], self.coords2[1]])

    def process(self, event: pygame.event.Event):
        # Clicking x button
        if event.type == pygame.QUIT:
            self.quit = True

        # Global settings: FPS indicator
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            self.showFPS = not self.showFPS
            
        self.modeInputDict[self.mode](event)
    
    def processGameOver(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            self.mode = "Gameplay"
            self.level.reset()
            u.unpauseMusic()
       
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
                u.stopSFX()
            elif (event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT,
                             pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]) and allStopped:
                for p in self.level.players:
                    p.keyMove(event.key)
            elif event.key == pygame.K_ESCAPE:
                self.mode = "Title Screen"
                u.stopSFX()
            elif event.key == pygame.K_SLASH:
                self.level.reset()
                self.mode = "Level Editor"
                u.stopSFX()
    
    def processTitle(self, event: pygame.event.Event):
        #PLAY: (81, 183) to (322, 265)
        #LVL SELECT: (354, 322) to (597, 402)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.doAdvance = not self.doAdvance

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # title screen BUTTONS
                if 81 <= self.mouseX <= 322 and 183 <= self.mouseY <= 265:
                    self.mode = "Gameplay"
                    if self.level is A1:
                        self.mode = "How To Play"
                elif 354 <= self.mouseX <= 597 and 322 <= self.mouseY <= 402:
                    self.mode = "Level Select"
                elif 155 <= self.mouseX <= 395 and 457 <= self.mouseY <= 538:
                    self.mode = "Level Editor"
                    self.level = editorLevel
                    self.advance = False
                    self.world = worldA
                    self.levelNumber = 0
                elif 212 <= self.mouseX <= 335 and 540 <= self.mouseY <= 570:
                    self.mode = "Editor Controls"
                # Sound toggles
                elif 530 <= self.mouseX <= 580 and 10 <= self.mouseY <= 60:
                    u.doSound = not u.doSound
                    if not u.doSound:
                        u.stopSFX()
                elif 590 <= self.mouseX <= 640 and 10 <= self.mouseY <= 60:
                    u.doMusic = not u.doMusic
                    if not u.doMusic:
                        u.stopMusic()
    
    def processEditorControls(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            self.mode = "Title Screen"

    def processLevelSelect(self, event: pygame.event.Event):        
        if event.type == pygame.MOUSEWHEEL:
            self.scrollMod += 20 * event.y
            self.scrollMod = max(min(0, self.scrollMod), -3247 + SCREEN_HEIGHT)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.mode = "Title Screen"
            elif event.key in self.code:
                self.secret.append(event.key)
            else:
                self.secret = []
            
            admin = len(self.secret) == len(self.code)
            reset = len(self.secret) == len(self.code)
            for one, two, three in zip(self.secret, self.code, self.edoc):
                admin = admin and (one == two)
                reset = reset and (one == three)
            if admin:
                self.unlocked = [[1 for _ in range(11)] for _ in range(6)]
                self.secret = []
            elif reset:
                self.resetData()
                self.secret = []

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # print(f"({self.mouseX}, {self.mouseY - self.scrollMod})")
                self.selectLevel()

    def processEditor(self, event: pygame.event.Event):
        a = self.point1
        b = self.point2
        swappedPointerX = False
        swappedPointerY = False
        

        # When a GUI object is present, ignore all other inputs and focus on it.
        if self.isGui() and event.type == pygame_gui.UI_BUTTON_PRESSED:
            # SAVE
            if self.saveSelector and event.ui_element == self.saveSelector.ok_button:
                print("SAVING LEVEL to", self.saveSelector.current_file_path)
                path = self.saveSelector.current_file_path
                if path:
                    try:
                        with open(path, "w") as f:
                            json.dump(self.level.toDict(), f, indent=2)
                    except Exception as e:
                        print("Could not save level:", e)
                self.saveSelector = None
            # LOAD
            elif self.loadSelector and event.ui_element == self.loadSelector.ok_button:
                print("LOADING LEVEL from", self.loadSelector.current_file_path)
                path = self.loadSelector.current_file_path
                if path:
                    try:
                        with open(path, "r") as f:
                            self.level = level.levelFromDict(json.load(f))
                    except:
                        print("Could not load level:", e)
                self.loadSelector = None
            elif self.saveSelector and event.ui_element == self.saveSelector.cancel_button:
                self.saveSelector = None
            elif self.loadSelector and event.ui_element == self.loadSelector.cancel_button:
                self.loadSelector = None
        # Text Input
        elif self.isGui() and self.textinput:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):
                self.level.text = self.textinput.value
                self.textinput = None
            else:
                self.textinput.update([event])
        # All editor commands besides object placement
        elif event.type == pygame.KEYDOWN and (not self.isGui()) and not(event.key == pygame.K_SPACE):
            # Erase
            if event.key == pygame.K_BACKSPACE:
                self.level.erase(a[0], a[1])

            # Switch Modes
            elif event.key == pygame.K_TAB:
                self.mode = "Palette"
            elif event.key == pygame.K_ESCAPE:
                self.mode = "Title Screen"
                self.editorColor = None
                self.colorIndicator = None
            elif event.key == pygame.K_SLASH:
                self.mode = "Gameplay"
                self.level.solidify()

            # Save/Load
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.saveSelector = UIFileDialog(rect=Rect(50, 50, 500, 400), window_title="Save your Level",
                                                 manager=self.manager, allow_picking_directories=False)

            elif event.key == pygame.K_o and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.loadSelector = UIFileDialog(rect=Rect(50, 50, 500, 400), window_title="Load from File",
                                                 manager=self.manager, allow_existing_files_only=False, allow_picking_directories=True)

            # Change  direction for directed objects
            elif event.key in player.directionDict.keys():
                self.editDirection = player.directionDict[event.key]
            
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
            
            # Undo
            if event.key == pygame.K_z:
                if len(self.level.levelObjects) > 0:
                    self.level.levelObjects.sort(key = lambda obj: obj.timestamp)
                    result : entity.Entity = self.level.levelObjects.pop()
                    print("Undid object with timestamp", result.timestamp)
                    self.level.levelObjects.sort(key = lambda obj: obj.order())
            
        # All object placement
        elif (event.type == pygame.KEYDOWN) and (not self.isGui()) and (event.key == pygame.K_SPACE):
            # These commands do not require a pointer swap. Most only use the primary pointer.
            if self.editorBrush == "Text":
                self.textinput = pygame_textinput.TextInputVisualizer(font_object = pygame.font.SysFont("Courier New", LEVELTEXTSIZE), 
                                                                      font_color=self.colors["text"], 
                                                                      cursor_color=self.colors["text"])
                self.level.textLocation = (a[0], a[1])
                self.level.text = ""
                self.level.textColor = self.colors["text"]

            elif self.editorBrush == "Teleporter":
                self.level.levelObjects.append(special.Teleporter(a[0], a[1], 
                                                            b[0], b[1], self.editUses))
            elif self.editorBrush == "Player":
                self.level.players.append(player.Player(a[0], a[1], self.colors["player"], self.gridSize, False))
            elif self.editorBrush == "InvertedPlayer":
                self.level.players.append(player.Player(a[0], a[1], self.colors["inverted"], self.gridSize, True)) 
            elif self.editorBrush == "Coin":
                self.level.levelObjects.append(entity.Coin(a[0], a[1], self.colors["coin"]))
            elif self.editorBrush == "Nullcube":
                self.level.levelObjects.append(special.NullCube(a[0], a[1]))
            elif self.editorBrush == "Resizer":
                self.level.levelObjects.append(special.Resizer(a[0], a[1], 3))
            elif self.editorBrush == "Redirector":
                self.level.levelObjects.append(special.Redirector(a[0], a[1], self.editDirection)) 

            # Platform additions require the pointer swap to get around the infamous pointer bug.
            if(a[0] - 5 > b[0]):
                temp = a[0]
                a[0] = b[0]
                b[0] = temp
                swappedPointerX = True
            if(a[1] - 5 > b[1]):
                temp = a[1]
                a[1] = b[1]
                b[1] = temp
                swappedPointerY = True

            if self.editorBrush == "Entity":
                self.level.levelObjects.append(entity.Entity(a[0], a[1], 
                                                            b[0], b[1], self.colors["platform"]))
            
            elif self.editorBrush == "Antiplatform":
                self.level.levelObjects.append(special.Antiplatform(a[0], a[1], 
                                                            b[0], b[1], self.colors["platform"]))
            elif self.editorBrush == "Cloud":
                self.level.levelObjects.append(special.Cloud(a[0], a[1], 
                                                            b[0], b[1]))
            elif self.editorBrush == "BeatBlockA":
                self.level.levelObjects.append(special.BeatBlock(a[0], a[1], 
                                                            b[0], b[1], "blue"))
            elif self.editorBrush == "BeatBlockB":
                self.level.levelObjects.append(special.BeatBlock(a[0], a[1], 
                                                            b[0], b[1], "red"))
                
            elif self.editorBrush == "Lever":
                self.level.levelObjects.append(special.Lever(a[0], a[1], 
                                                            b[0], b[1], self.editDirection,
                                                            self.colors["platform"]))
            elif self.editorBrush == "Quicksand":
                self.level.levelObjects.append(special.Quicksand(a[0], a[1], 
                                                            b[0], b[1], self.editDirection))
            elif self.editorBrush == "Tar":
                self.level.levelObjects.append(special.Tar(a[0], a[1], 
                                                            b[0], b[1], self.editDirection))
            elif self.editorBrush == "Stone":
                self.level.levelObjects.append(special.Stone(a[0], a[1], 
                                                            b[0], b[1]))
        # Pointer selection         
        elif event.type == pygame.MOUSEBUTTONDOWN and (not self.isGui()):
            # Left mouse: Set point1
            if event.button == 1:
                self.point1 = [self.mouseX - (self.mouseX % self.gridSize), self.mouseY - (self.mouseY % self.gridSize)]
            # Right mouse: Set point2
            if event.button == 3:
                self.point2 = [self.mouseX - (self.mouseX % self.gridSize) + self.gridSize, self.mouseY - (self.mouseY % self.gridSize)  + self.gridSize]
        
        # Adjust points if necessary
        if(swappedPointerX):
            temp = a[0]
            a[0] = b[0]
            b[0] = temp
        if(swappedPointerY):
            temp = a[1]
            a[1] = b[1]
            b[1] = temp

    def screenText(self, x, y, text = "Default", size = 100, color = [250, 250, 250], background = None):
        tempFont = pygame.font.SysFont("msgothic", size)
        tempText = tempFont.render(text, True, color, background)
        self.screen.blit(tempText, (x, y))
    
    def selectLevel(self):
        mouseModY = self.mouseY - self.scrollMod
        for (worldIndex, (planet, selector)) in enumerate(worldInfo):
            for i, (x, y) in enumerate(selector):
                if (x <= self.mouseX <= x + LEVEL_SQUARE_SIZE) and \
                (y <= mouseModY <= y + LEVEL_SQUARE_SIZE):
                    # Is the level unlocked?
                    if planet == worldChallenge and self.unlocked[i][10]:
                        self.beamDown(planet, i)
                    elif planet != worldChallenge and self.unlocked[worldIndex][i]:
                        self.beamDown(planet, i)                    
    
    def beamDown(self, destination, num):

        # Change colors and music
        u.unpauseMusic()
        if destination == worldChallenge:
            self.colors = colorsWorldChallenge
            u.playMusic(allMusic[num])
        elif destination == self.world:
            pass
        elif destination == worldA:
            self.colors = colorsWorldA
            u.playMusic(worldAMusic)
        elif destination == worldB:
            self.colors = colorsWorldB
            u.playMusic(worldBMusic)
        elif destination == worldC:
            self.colors = colorsWorldC
            u.playMusic(worldCMusic)
        elif destination == worldD:
            self.colors = colorsWorldD
            u.playMusic(worldDMusic)
        elif destination == worldE:
            self.colors = colorsWorldE
            u.playMusic(worldEMusic)
        elif destination == worldF:
            self.colors = colorsWorldF
            u.playMusic(worldFMusic)
        
        
        self.levelNumber = num
        self.world = destination
        self.level = destination[num]
        self.level.reset()
        self.advance = self.doAdvance
        self.mode = "Gameplay"
        # In developer mode, the level's background should be set
        if (not self.doAdvance):
            self.level.background = self.colors["background"]
            self.level.solidify()
                   
    def displayHowToPlay(self):
        self.screen.blit(howToPlayImage, (0, 0))
    
    def processHowToPlay(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.mode = "Gameplay"
            elif event.key == pygame.K_ESCAPE:
                self.mode = "Title Screen"
    
    def loadSaveFile(self, f : list[list[int]]):
        self.unlocked = f
        for row in self.unlocked:
            row[0] = 1
    
    def resetData(self):
        self.unlocked = [[0 for _ in range(11)] for _ in range(6)]
        for row in self.unlocked:
            row[0] = 1

    def isGui(self):
        return(self.saveSelector or self.loadSelector or self.textinput)