# Javin Zipkin
# Gravity Switch
# Period 1

#Module initialization
import pygame
import random
pygame.init()
clock = pygame.time.Clock()
#player object type
class player:
    def __init__(self, x1, y1, x2, y2, color = (102, 205, 170), size = 25):
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.xv = 0
        self.yv = 0
        self.size = size
        self.direction = "stop"

    #This is only for debug, so I can view the player stats
    def __repr__(self):
        return(str(player.x1) + ", " + str(player.y1) + ", " + str(player.x2) + ", " + str(player.y2) \
            + ", " + str(player.xv) + ", " + str(player.yv))
#level design
#These functions are made for convenience, none are actually necessary but the code would be REALLY messy without them
def random_color(min = 0, max = 255):
    return (random.randint(min, max), random.randint(min, max), random.randint(min, max))
def arena50(left = True):
    global platforms
    if left:
        platforms.append([0, 0, 50, 500])
    platforms.append([0, 450, 500, 500])
    platforms.append([0, 0, 500, 50])
    platforms.append([450, 0, 500, 500])
def cleararena():
    global platforms, winspace, nullcubes, clouds, antiplatforms, redirectors, teleporters, levers
    platforms = []
    winspace = []
    nullcubes = []
    clouds = []
    redirectors = []
    antiplatforms = []
    teleporters = []
    levers = []
def playerplace(x, y):
    global player
    player.x1 = x
    player.y1 = y
def collidingWithRect(rect):
    return ((player.x1 in range(rect[0], rect[2])  or  player.x2 in range(rect[0], rect[2])) \
    and (player.y1 in range(rect[1], rect[3])  or  player.y2 in range(rect[1], rect[3]))) and safety == 0
def snapshot(tl = True, tr = True, bl = True, br = True):
    global platforms
    x = player.size
    #Top left
    if tl:
        platforms.append([0,0,x * 4, x * 2])
        platforms.append([0,0,x * 2, x * 4])
    #Bottom right
    if br:
        platforms.append([500 - x * 4, 500 - x * 2, 500, 500])
        platforms.append([500 - x * 2, 500 - x * 4, 500, 500])
    #Top right
    if tr:
        platforms.append([500 - x * 4, 0, 500,x * 2])
        platforms.append([500 - x * 2, 0, 500, x * 4])
    #Bottom left
    if bl:
        platforms.append([0,500 - x * 4, x * 2,500])
        platforms.append([0,500 - x * 2, x * 4,500])

def switchlevels():
    global level
    cleararena()
    funcArr = ["nothing", level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10, \
    level_11, level_12, level_13, level_14, level_15, level_16, level_17, level_18, level_19, level_20, level_21, level_22, level_23, level_24]
    #lower the level to the max one if you've finished all the levels
    while level >= len(funcArr):
        level -= 1
    #change the player size based on levels
    if level % 10 == 0:
        player.size = 15
    else:
        player.size = 25
    #If theres no more levels, just restart the current level otherwise start the new level
    funcArr[level]()

def drawLevelObjects():
    #draw the null cubes
    for cube in nullcubes:
        betterRect(nullcubecol, cube[0], cube[1], cube[0] + player.size, cube[1] + player.size, 2)        
    #draw the platforms
    for platform in platforms:
        betterRect(platformcol, platform[0], platform[1], platform[2], platform[3], 0)        
    #draw the win space
    for space in winspace:
        betterRect(winspacecol, space[0], space[1], space[0] + player.size, space[1] + player.size, 0)        
    #draw the clouds
    for cloud in clouds:
        betterRect(cloudcol, cloud[0], cloud[1], cloud[2], cloud[3], 0) 

    #draw the redirectors
    for director in redirectors:
        center =  [(director[0] * 2 + player.size) // 2, (director[1] * 2 + player.size) // 2 ]
        betterRect(directorcol, director[0], director[1], director[0] + player.size, director[1] + player.size, 2) 
        if director[2] == "down":
            pygame.draw.line(screen, directorcol, center, (center[0], director[1] + player.size), 2)
        if director[2] == "up":
            pygame.draw.line(screen, directorcol, center, (center[0], director[1]), 2)
        if director[2] == "left":
            pygame.draw.line(screen, directorcol, center, (director[0], center[1]), 2)
        if director[2] == "right":
            pygame.draw.line(screen, directorcol, center, (director[0] + player.size, center[1]), 2)    
    #draw the levers 
    for lever in levers:
        betterRect(platformcol, lever[0], lever[1], lever[2], lever[3], 2)
        if lever[4] == "down":
            betterRect(platformcol, lever[0], lever[1], lever[2], (lever[1] + lever[3]) // 2, 0)
        elif lever[4] == "up":
            betterRect(platformcol, lever[0], (lever[1] + lever[3]) // 2, lever[2], lever[3], 0)
        elif lever[4] == "left":
            betterRect(platformcol, (lever[2] + lever[0]) // 2, lever[1], lever[2], lever[3], 0)
        elif lever[4] == "right":
            betterRect(platformcol, lever[0], lever[1], (lever[2] + lever[0]) // 2, lever[3], 0)
    #draw the antiplatforms
    for anti in antiplatforms:
        if anti[4] == False:
            betterRect(platformcol, anti[0], anti[1], anti[2], anti[3], 2)
        else:
            betterRect(platformcol, anti[0], anti[1], anti[2], anti[3], 0)

    #draw the teleporters
    teleColors = [nullcubecol, cloudcol, player.color]
    for i in range(len(teleporters)):
        #center1 = [(tele[0] * 2 + player.size) // 2, (tele[1] * 2 + player.size) // 2 ]
        #center2 = [(tele[2] * 2 + player.size) // 2, (tele[3] * 2 + player.size) // 2 ]
        #pygame.draw.line(screen, nullcubecol, center1, center2, 2)
        betterRect(teleColors[i], teleporters[i][0], teleporters[i][1], teleporters[i][0] + player.size, teleporters[i][1] + player.size, 2)
        betterRect(teleColors[i], teleporters[i][2], teleporters[i][3], teleporters[i][2] + player.size, teleporters[i][3] + player.size, 2)
#these are integral functions for level design
# Note: Some of the lists get really long because the levels are complex but I'm
# not cutting off the lines because it's more convenient in my case to have longer lines
# than to have more of them (specifically in this section of the code)
def level_1():
    global platforms, winspace, nullcubes, clouds
    platforms = [[50, 50, 100, 450], [50, 50, 450, 100], [50, 400, 450, 450], [400, 50, 450, 450], [300, 150, 450, 200]]
    winspace = [[150, 200]]
    playerplace(100, 100)
def level_2():
    global platforms, winspace, nullcubes, clouds
    platforms = [[0, 0, 50, 500], [0, 450, 500, 500], [0, 0, 500, 50], [450, 0, 500, 350], [200, 0, 250, 200], [150, 275, 200, 325]]
    winspace = [[250, 390], [55, 420]]
    playerplace(50, 50)
def level_3():
    global platforms, winspace, nullcubes, clouds
    playerplace(50, 50)
    snapshot()
    nullcubes = [[238, 424], [238, 225]]
    winspace = [[475, 225]]
def level_4():
    global platforms, winspace, nullcubes, clouds
    playerplace(1, 424)
    platforms = [[400,0,500,50], [450,0,500,100], [0, 450, 500, 500], [450, 350, 500, 500], [200, 250, 250, 400], [0, 100, 50, 300], [0, 250, 50, 400], [0, 350, 100, 400]]
    nullcubes = [[225, 50], [350, 125], [350, 223]]
    winspace = [[50, 325], [350, 300]]
def level_5():
    global platforms, winspace, nullcubes, clouds
    playerplace(100, 424)
    platforms = [[0, 250, 50, 500], [50, 0, 300, 50], [50, 450, 200, 500], [200, 250, 250, 500], [450, 250, 500, 500]]
    winspace = [[0, 78]]
    nullcubes = [[350, 224]]
    clouds = [[50, 250, 200, 275], [250, 350, 450, 375], [250, 100, 450, 125]]
def level_6():
    global platforms, winspace, nullcubes, clouds
    playerplace(263, 274)
    platforms = [[0, 0, 50, 175], [75, 450, 500, 500], [250, 300, 300, 500], [250, 0, 400, 50], [450, 100, 500, 200], [0, 0, 150, 50]]
    winspace = [[301, 424], [225, 0], [224, 424]]
    nullcubes = [[75, 274], [300, 200]]
    clouds = [[300, 150, 400, 175], [51, 150, 150, 175], [300, 300, 400, 325]]
def level_7():
    global platforms, winspace, nullcubes, clouds
    playerplace(51, 424)
    platforms = [[0, 0, 50, 500], [0, 0, 500, 50], [0, 450, 500, 500], [450, 0, 500, 270], [450, 400, 500, 500], [0, 0, 150, 100], [400, 150, 450, 200], [200, 400, 250, 500], [50, 300, 100, 350]]
    winspace = [[100, 325], [124, 275], [250, 174]]
    nullcubes = [[250, 275]]
    clouds = [[350, 350, 500, 375]]
def level_8():
    global platforms, winspace, nullcubes, clouds
    playerplace(51, 424)
    platforms = [[0, 150,50, 500], [0, 450, 400, 500], [375, 0, 500, 50], [450, 150, 500, 500]]
    winspace = [[238, 424,], [238, 125], [238, 51], [238, 225]]
    nullcubes = [[51, 50], [423, 225]]
    clouds = [[50, 150, 125, 175], [375, 150, 450, 175]]
def level_9():
    global platforms, winspace, nullcubes, clouds
    playerplace(50, 50)
    platforms = [[0, 0, 150, 50], [0, 300, 50, 500], [0, 450, 500, 500], [451, 300, 500, 500]]
    winspace = [[425, 0],[200, 50], [200, 175], [425, 112], [238, 424]]
    nullcubes = [[425, 50], [425, 175]]
    clouds = [[0, 200, 150, 225]]
def level_10():
    global platforms, winspace, nullcubes, clouds
    #LARGER LEVEL STATS
    #player Size, Cube Thickness, Winspace Thickness is 15. Platform Thickness is 30. Cloud Thickness is 15.
    player.size = 15
    playerplace(454, 31)
    platforms = [[0, 370, 30, 500], [440, 355, 500, 385], [470, 355, 500, 500], [185, 185, 215, 315], [200, 0, 299, 30], [270, 100, 300, 200]]
    winspace = [[135, 350], [255, 300], [215, 335], [275, 386], [360, 135], [215, 100], [301, 65]]
    nullcubes = [[135, 170], [215, 386], [300, 300], [300, 454], [30, 300]]
    clouds = [[130, 401, 160, 416], [440, 150, 500, 165], [215, 185, 269, 200]]
    #make the arena thing
    snapshot(tl = False)
def level_11():
    global platforms, winspace, redirectors
    player.size = 25
    playerplace(51, 424)
    redirectors = [[51, 150, "right"], [200, 51, "down"], [200, 250, "right"], [424, 250, "up"]]
    winspace = [[200, 150], [312, 250], [424, 150]]
    nullcubes = []
    snapshot()
def level_12():
    global platforms, winspace, redirectors, antiplatforms
    playerplace(51, 424)
    redirectors = []
    winspace = [[51, 150], [275, 0], [424, 150]]
    antiplatforms = [[50, 225, 450, 275, False],[225, 50, 275, 450, False]]
    snapshot()
def level_13():
    global platforms, winspace, redirectors, antiplatforms
    playerplace(50, 424)
    redirectors = [[240, 351, "up"], [424, 125, "down"], [425, 50, "left"]]
    winspace = [[50, 250], [240, 50], [424, 424]]
    snapshot(tr = False)
    antiplatforms = [ [150, 0, 200, 498, False], [300, 0, 350, 350, False], [0, 150, 150, 200, False], [350, 300, 498, 350, False]]
def level_14():
    global platforms, winspace, redirectors, antiplatforms
    playerplace(200, 200)
    redirectors = [[351, 0, "left"], [425, 450, "left"], [200, 450, "up"], [50, 450, "right"]]
    winspace = [[424, 249], [0, 326], [351, 125]]
    platforms = [[0, 0, 50, 325], [450, 0, 500, 325], [150, 100, 300, 150]]
    antiplatforms = [[300, 425, 350, 498, False], [300, 100, 350, 325, False], [150, 275, 500, 325, False]]
def level_15():
    global platforms, winspace, redirectors, antiplatforms
    playerplace(112, 0)
    redirectors = [[375, 395, "left"],[423, 423, "up"], [112, 423, "up"],  [375, 0, "down"]]
    winspace = [[375, 262], [112, 212]]
    platforms = [[250, 450, 300, 500], [450, 0, 500, 500], [0, 0, 50, 500], [200, 100, 250, 350], [50, 100, 100, 150], [150, 100, 200, 150]]
    antiplatforms = [[250, 200, 300, 250, False],[201, 100, 499, 150, False], [50, 300, 200, 350, False]]
def level_16():
    global platforms, winspace, antiplatforms, redirectors
    playerplace(155, 0)
    antiplatforms = [[125, 225, 375, 275, False], [225, 125, 275, 375, False]]
    winspace = [[275, 390], [380, 325], [155, 275], [275, 275], [50, 160], [424, 275]]
    redirectors = [[325, 0, "down"], [51, 325, "right"], [325, 474, "up"]]
    platforms = [[125, 450, 325, 500], [0, 0, 50, 500], [450, 0, 500, 500]]
def level_17():
    global platforms, winspace, antiplatforms, redirectors
    playerplace(245, 200)
    winspace = [[101, 160], [205, 300], [205, 424], [351, 51], [51, 375], [152, 226], [325, 200], [274, 51], [51, 175]]
    platforms = [[0, 0, 50, 150], [0, 225, 50, 500], [155, 400, 205, 500], [300, 0, 350, 105]]
    antiplatforms = [[400, 255, 500, 305, False], [100, 200, 150, 350, False], [200, 105, 350, 155, False]]
    redirectors = [[424, 200, "up"], [245, 349, "right"], [50, 79, "right"], [152, 200, "down"], [179, 226, "right"]]
    arena50(False)
def level_18():
    global platforms, winspace, antiplatforms, redirectors
    playerplace(0, 51)
    winspace = [[300, 325], [200, 51], [51, 350], [424, 150], [425, 424], [200, 300]]
    redirectors = [[50, 0, "down"], [200, 173, "down"], [152, 350, "down"]]
    platforms = [[0, 200, 50, 500], [300, 0, 500, 50], [450, 0, 500, 350], [0, 450, 500, 500]]
    antiplatforms = [[350, 200, 500, 250, False],[100, 350, 150, 500, False], [100, 250, 150, 350, False], [350, 349, 500, 400, False], [50, 200, 350, 250, False], [300, 50, 350, 250,False]]
def level_19():
    global platforms, winspace, antiplatforms, redirectors
    playerplace(125, 150)
    arena50()
    redirectors = [[250, 424, "left"], [51, 424, "up"], [51, 51, "right"], [424, 51, "down"], [424, 424, "left"]]
    antiplatforms = [[0, 275, 100, 325, False], [176, 0, 225, 225, False], [0, 176, 225, 225, False], [300, 0, 350, 275, False], [300, 275, 500, 325, False]]
    winspace = [[51, 350], [300, 424], [274, 51], [274, 150], [125, 350], [125, 51], [350, 51], [51, 150], [424, 150]]
def level_20():
    global platforms, winspace, antiplatforms, redirectors
    playerplace(31, 187)
    platforms = [[0, 160, 30, 230], [470, 0, 500, 260], [117, 400, 160, 430]]
    snapshot()
    winspace = [[160, 115], [270, 260], [270, 115], [30, 261], [455, 315], [345, 30], [300, 160], [130, 187], [30, 80], [130, 300], [300, 455]]
    antiplatforms = [[285, 300, 315, 400, False], [100, 0, 130, 160, False], [0, 230, 100, 260, False], [0, 130, 100, 160, False]]
    redirectors = [[345, 75, "left"], [345, 385, "up"], [454, 100, "down"], [200, 114, "left"], [200, 214, "up"]]
def level_21():
    global platforms, winspace, teleporters
    playerplace(51, 51)
    platforms = [[0, 225, 100, 275]]
    teleporters = [[237, 51, 237, 424]]
    snapshot()
    winspace = [[50, 424], [350, 200]]
def level_22():
    global platforms, winspace, levers
    playerplace(200, 424)
    arena50()
    winspace = [[130, 200]]
    levers = [[250, 225, 450, 275, "up"], [250, 326, 300, 500, "left"]]
def level_23():
    global platforms, winspace, levers, teleporters 
    playerplace(51, 51)
    platforms = [[150, 150, 200, 376], [150, 150, 350, 200], [450, 150, 500, 500]]
    snapshot(bl = False, tr = False)
    winspace = [[300, 275], [300, 200], [200, 475], [350, 380]]
    teleporters = [[424, 51, 51, 424]]
    levers = [[300, 300, 500, 350, "down"], [0, 325, 150, 375, "down"]]
def level_24():
    global platforms, winspace, levers, teleporters 
    playerplace(238, 276)
    platforms = [[400, 0, 500, 50], [238, 450, 362, 500], [264, 0, 312, 100], [0, 0, 312, 50], [0, 450, 200, 500], [0, 400, 50, 500], [450, 400, 500, 500]]
    winspace = [[0, 200], [425, 51], [325, 424]]
    teleporters = [[238, 200, 51, 276]]
    levers = [[350, 225, 500, 275, "down"], [150, 0, 200, 275, "left"]]
#MAIN
#i hate the pygame rect function so this is better yaBy
def betterRect(color, x1, y1, x2, y2, width):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)

#player init
player = player(0, 0, 0, 0)
#starting level
level = 1
#debug (Should always be True except when testing/level designing)
screenFill = True
#frames
frames = 0
safety = 3
#setting up the screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
#these variables track if the player has quit the game or not, and if they have touched an obstacle
done = False
lose = False
#colors
platformcol = (100, 149, 237)
player.color = (102, 205, 170)
nullcubecol = (250, 0, 200)
winspacecol = (123, 104, 238)
cloudcol = (220, 220, 220)
screencol = (0, 0, 80)
directorcol = player.color

#text display initialization
basicfont = pygame.font.SysFont(None, 48)
smaller = pygame.font.SysFont(None,  40)
larger = pygame.font.SysFont(None,  180)
youLose = basicfont.render('You lose!', True, (255, 255, 255), (0, 0, 0))
pressSpace = basicfont.render('Press space to restart.', True, (255, 255, 255), (0, 0, 0))
title = basicfont.render('GRAVITY SWITCH', True, player.color, (0, 0, 80))
play = basicfont.render('Play', True, platformcol, screencol)
controls = basicfont.render('Controls', True, nullcubecol, screencol)
arrowKeyText = smaller.render('Use arrow keys to move', True, platformcol, screencol)
qText = smaller.render('Press q to restart level', True, player.color, screencol)
spaceText = smaller.render('Press space to respawn after losing', True, winspacecol, screencol)
returnMenuText = smaller.render('Press m to return to the menu', True, nullcubecol, screencol)
whichLevel = larger.render(str(level), True, platformcol, screencol)
levelSelectText = smaller.render('Level Select', True, winspacecol, screencol)
instructions = [arrowKeyText, qText, spaceText, returnMenuText]

#player.direction - up, down, right, left, stop
player.direction = "stop"

#PLATFORM TYPES
#platforms stop you 
platforms = []
#you can go through the bottom, right, and left of clouds, but you can't go through the top
clouds = []
#winspace lets you move to the next level
winspace = []
#null cubes let you reposition, but only once
nullcubes = []
#redirectors push you in a certain direction and don't go away
redirectors = []
#the first time you hit an antiplatform, you pass through it and it becomes a normal platform
antiplatforms = []
#teleporters...teleport you
teleporters = []
#Levers switch from up to down or left to right when you hit them, blocking you depending on your player.direction
levers = []
#rAnDoM vArIaBlEs because the code is SO OPTIMIZED
incube = False
detectacube = False
indirect = False
detectDirect = False
playing = False
controlView = False
selectView = False
inLever = False
leverDetect = False
holdingMouse = False
switchlevels()
while not done:
    lose = False
    restart = False
    frames = 0
    #level = 1
    while not done and not playing:
        #TITLE SCREEN
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True

        screen.fill((screencol))

        #show text
        screen.blit(title, (102, 100))
        screen.blit(play, (215, 230))
        screen.blit(controls, (67, 382))
        screen.blit(levelSelectText, (280, 386))
        #draw the squares
        betterRect(nullcubecol, 50, 350, 225, 450, 5)
        betterRect(winspacecol, 275, 350, 450, 450, 5)
        betterRect(platformcol, 150, 200, 350, 300, 5)
        #check mouse position and pressed
        mousey = (pygame.mouse.get_pos()[1])
        mousex = (pygame.mouse.get_pos()[0])
        pressed = pygame.mouse.get_pressed()[0]
        #play if you're clicking on play
        if pressed and 150 <= mousex <= 350 and 200 <= mousey <= 300:
            playing = True
        #view the controls if you're clicking on Controls
        if pressed and 50 <= mousex <= 225 and 350 <= mousey <= 450:
            controlView = True
        if pressed and 275 <= mousex <= 450 and 350 <= mousey <= 450:
            selectView = True
        #control scheme viewer
        while controlView and not done:
            #view controls through text
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True
            screen.fill((screencol))
            #draw text
            for i in range(len(instructions)):
                screen.blit(instructions[i], (15, i * 75 + 10))
            #return to menu
            if pygame.key.get_pressed()[pygame.K_m]:
                controlView = False
            #update display
            pygame.display.flip()
        #level selector
        while selectView and not done:
            #change level
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True
            screen.fill((screencol))
            #draw level display text
            screen.blit(whichLevel, (180, 150))
            screen.blit(returnMenuText, (57, 400))
            #draw arrows
            pygame.draw.polygon(screen, platformcol, ([(110, 160), (150, 250), (70, 250)]), 0)
            pygame.draw.polygon(screen, platformcol, ([(390, 250), (430, 160), (350, 160)]), 0)
            #check mouse position and pressed
            mousey = (pygame.mouse.get_pos()[1])
            mousex = (pygame.mouse.get_pos()[0])
            pressed = pygame.mouse.get_pressed()[0]
            if pygame.mouse.get_pressed()[0]:
                if holdingMouse == False:
                    if 70 <= mousex <= 150 and 160 <= mousey <= 250:
                        level += 1
                        safety = 5
                        switchlevels()
                    elif 350 <= mousex <= 430 and 160 <= mousey <= 250 and level > 1:
                        safety = 5
                        level -= 1
                        switchlevels()
                    holdingMouse = True
            else:
                holdingMouse = False
            #change the text based on level
            whichLevel = larger.render(str(level), True, platformcol, screencol)    
            #return to menu
            if pygame.key.get_pressed()[pygame.K_m]:
                selectView = False
            #update display
            pygame.display.flip()

        #update display
        pygame.display.flip()
    while not done and not lose:
        #MAIN GAME
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True 
        #fps limit
        clock.tick(80)
        #The "Safety Frames" make sure nothing changes right when you start a level
        if safety > 0:
            safety -= 1
        frames += 1

        #clear screen + add background color
        if screenFill:
            screen.fill((screencol))

        #debug mouse position print

        mousey = (pygame.mouse.get_pos()[1])
        mousex = (pygame.mouse.get_pos()[0])
        if pygame.mouse.get_pressed()[0]:
            pass
            #print(str(mousex) + ", " + str(mousey))

        #check keys
        keys = pygame.key.get_pressed()
        #up key
        if keys[pygame.K_UP] and player.direction == "stop" and holding == False: 
            player.direction = "up"
            holding = True
        #down key
        elif keys[pygame.K_DOWN] and player.direction == "stop" and holding == False:
            player.direction = "down"
            holding = True
        #left key
        elif keys[pygame.K_LEFT] and player.direction == "stop" and holding == False:
            player.direction = "left"
            holding = True
        #right key
        elif keys[pygame.K_RIGHT] and player.direction == "stop" and holding == False:
            player.direction = "right"
            holding = True
        #return to menu
        if keys[pygame.K_m]:
            lose = True
            restart = True
            playing = False
        #not holding anything
        else:
            holding = False
        #restart key
        if keys[pygame.K_q]:
            lose = True

        #calculate if the player has won or not
        for i in winspace:
            #condition
            if collidingWithRect([i[0], i[1], i[0] + player.size, i[1] + player.size]):
                winspace.remove(i)
                if winspace == []:
                    level += 1
                    player.direction = "stop"
                    player.xv = 0
                    player.yv = 0
                    safety = 5
                    switchlevels()

        #PLATFORMS
        for i in platforms:
            #condition
            if collidingWithRect(i):
                if player.direction == "down":
                    player.y1 = i[1] - player.size - 1
                elif player.direction == "up":
                    player.y1 = i[3] + 1
                elif player.direction == "right":
                    player.x1 = i[0] - player.size - 1
                elif player.direction == "left":
                    player.x1 = i[2] + 1
                player.direction = "stop"
        #CLOUDS
        for i in clouds:
            #condition - only collide if you're going down
            if collidingWithRect(i) and player.direction == "down":
                
                player.y1 = i[1] - player.size - 1
                player.direction = "stop"
        
        #NULL CUBES
        for i in nullcubes:
            #condition
            if collidingWithRect([i[0], i[1], i[0] + player.size, i[1] + player.size]): 
                #stop the player
                player.direction = "stop"
                incube = True
                #place the player into the cube
                playerplace(i[0], i[1])
                #nullcube goes away when u touch it
                nullcubes.remove(i)

        #REDIRECTORS
        detectDirect = False
        for i in redirectors:
            #condition
            if collidingWithRect([i[0], i[1], i[0] + player.size, i[1] + player.size]): 
                detectDirect = True
                if indirect == False:
                    #"stick" the player into the redirector, then send them out
                    player.xv = 0
                    player.yv = 0
                    player.direction = i[2]
                    playerplace(i[0], i[1])
                    indirect = True
        if detectDirect == False:
            indirect = False

        #TELEPORTERS
        detectTele = False
        for i in teleporters:
            #condition
            if collidingWithRect([i[0], i[1], i[0] + player.size, i[1] + player.size]): 
                detectTele = True
                if inTele == False:
                    player.x1 = i[2]
                    player.y1 = i[3]
                    inTele = True
            if collidingWithRect([i[2], i[3], i[2] + player.size, i[3] + player.size]): 
                detectTele = True
                if inTele == False:
                    player.x1 = i[0]
                    player.y1 = i[1]
                    inTele = True
        if detectTele == False:
            inTele = False

        #LEVERS
        leverDetect = False
        for i in levers:    
            #condition
            if collidingWithRect(i):
                leverDetect = True
                if inLever == False:
                    inLever = True
                    #normal platform collision
                    if player.direction == "down":
                        if i[4] == "down":
                            player.direction = "stop"
                            player.y1 = i[1] - player.size - 1
                        else: 
                            i[4] = player.direction
                    elif player.direction == "up":
                        if i[4] == "up":
                            player.y1 = i[3] + 1
                            player.direction = "stop"
                        else: 
                            i[4] = player.direction
                    elif player.direction == "right":
                        if i[4] == "right":
                            player.x1 = i[0] - player.size - 1
                            player.direction = "stop"
                        else: 
                            i[4] = player.direction
                    elif player.direction == "left":
                        if i[4] == "left":
                            player.x1 = i[2] + 1
                            player.direction = "stop"
                        else: 
                            i[4] = player.direction
        if leverDetect == False:
            inLever = False

        #ANTIPLATFORMS
        antiDetect = False
        for i in antiplatforms:
            #condition
            if collidingWithRect(i):
                antiDetect = True
                if inAnti == False:
                    #"fill" the platform when you touch it
                    if i[4] == False and safety == 0:
                        i[4] = True
                        inAnti = True
                    #normal platform collision
                    else:
                        if player.direction == "down":
                            player.y1 = i[1] - player.size - 1
                        elif player.direction == "up":
                            player.y1 = i[3] + 1
                        elif player.direction == "right":
                            player.x1 = i[0] - player.size - 1
                        elif player.direction == "left":
                            player.x1 = i[2] + 1
                        player.direction = "stop"
        if antiDetect == False:
            inAnti = False

        #Change color scheme based on how far u are in the game
        #colors
        if level > 20:
            platformcol = (49, 87, 54)
            player.color = (89, 129, 45)
            nullcubecol = (144, 169, 85)
            winspacecol = (144, 69, 85)
            cloudcol = (236, 243, 158)
            screencol = (19, 42, 19)
        elif level > 10:
            platformcol = (85, 51, 51)
            player.color = (255, 255, 68)
            nullcubecol = (255, 25, 5)
            winspacecol = (204, 68, 34)
            cloudcol = (234, 218, 181)
            screencol = (255, 102, 0)
        else:
            platformcol = (100, 149, 237)
            player.color = (102, 205, 170)
            nullcubecol = (250, 0, 200)
            winspacecol = (123, 104, 238)
            cloudcol = (220, 220, 220)
            screencol = (0, 0, 80)
        #also change the main menu stuff
        title = basicfont.render('GRAVITY SWITCH', True, player.color, screencol)
        play = basicfont.render('Play', True, platformcol, screencol)
        controls = basicfont.render('Controls', True, nullcubecol, screencol)
        arrowKeyText = smaller.render('Use arrow keys to move', True, platformcol, screencol)
        qText = smaller.render('Press q to restart level', True, player.color, screencol)
        spaceText = smaller.render('Press space to respawn after losing', True, winspacecol, screencol)
        returnMenuText = smaller.render('Press m to return to the menu', True, nullcubecol, screencol)
        instructions = [arrowKeyText, qText, spaceText, returnMenuText]
        levelSelectText = smaller.render('Level Select', True, winspacecol, screencol)
        directorcol = player.color

        #lose the game if u go out of bounds
        if player.x1 < 0 or player.x2 > screen_width or player.y1 < 0 or player.y2 > screen_height:
            lose = True
            switchlevels()
        
        #self explanatory
        drawLevelObjects()

        #increase velocity based on player.direction
        if player.direction == "stop":
            player.xv = 0
            player.yv = 0
        elif player.direction == "up":
            if frames % 3 == 0 and player.yv >= -8:
                player.yv -= 2
        elif player.direction == "down":
            if frames % 3 == 0 and player.yv <= 8:
                player.yv += 2
        elif player.direction == "left":
            if frames % 3 == 0 and player.xv >= -8:
                player.xv -= 2
        elif player.direction == "right":
            if frames % 3 == 0 and player.xv <= 8:
                player.xv += 2

        #actually carry out the player movement based on velocity
        player.x1 += player.xv #x
        player.y1 += player.yv #y
        player.x2 = player.x1 + player.size
        player.y2 = player.y1 + player.size

        #draw the player
        betterRect(player.color, player.x1, player.y1, player.x2, player.y2, 0)
        pygame.display.flip()
        #debug stat print
        #print(player)
    while not restart and not done:
        #This is the 'u lose' screen
        #clear screen
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    done = True 
        screen.blit(youLose, (180, 202))
        screen.blit(pressSpace, (100, 230))
        #reset velocity
        player.xv = 0
        player.yv = 0 
        #restart the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            restart = True
            player.direction = "stop"
            switchlevels()
        #return to menu
        if keys[pygame.K_m]:
            lose = True
            restart = True
            playing = False
        pygame.display.flip()
pygame.quit()