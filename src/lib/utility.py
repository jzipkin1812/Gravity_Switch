import pygame
import math
# UTILITY FUNCTIONS
def betterRect(screen, x1, y1, x2, y2, color = (0, 0, 0), width = 0):
    pygame.draw.polygon(screen, (color), ([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]), width)

def distanceFormula(x1, y1, x2, y2):
    return(int(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )))

def resize(image, multiplier):
    width = image.get_rect().size[0]
    height = image.get_rect().size[1]
    return(pygame.transform.scale(image, (int(width * multiplier), int(height * multiplier))))

def screenText(x, y, screen, text = "Default", size = 100, color = [250, 250, 250], background = None):
    tempFont = pygame.font.SysFont("Courier New", size)
    tempText = tempFont.render(text, True, color, background)
    screen.blit(tempText, (x, y))
    
def transparentScreenText(x, y, screen, text = "Default", size = 100, color = [250, 250, 250]):
    tempFont = pygame.font.SysFont("Courier New", size)
    tempText = tempFont.render(text, True, color)
    tempText.set_alpha(90)  
    screen.blit(tempText, (x, y))
    
def invert(direction: str) -> str:
    inverted = {
        "up" : "down",
        "down" : "up",
        "left" : "right",
        "right" : "left",
    }
    return(inverted[direction])