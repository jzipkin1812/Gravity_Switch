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

def dashedLine(surface, color, startPos, endPos, dashLength=10, spaceLength=5, width=1):
    # Calculate direction vector
    x1, y1 = startPos
    x2, y2 = endPos
    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)
    angle = math.atan2(dy, dx)

    # Normalize direction vector
    dash_space = dashLength + spaceLength
    num_dashes = int(distance // dash_space)

    for i in range(num_dashes + 1):
        startX = x1 + (i * dash_space) * math.cos(angle)
        startY = y1 + (i * dash_space) * math.sin(angle)
        endX = startX + dashLength * math.cos(angle)
        endY = startY + dashLength * math.sin(angle)

        if math.hypot(endX - x1, endY - y1) > distance:
            break  # Avoid overshooting

        pygame.draw.line(surface, color, (startX, startY), (endX, endY), width)


def playSound(channel : int, soundObj):
    pygame.mixer.Channel(channel).play(soundObj)
