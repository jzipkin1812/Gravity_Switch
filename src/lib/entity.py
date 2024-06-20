from . import utility as u
class Entity:
    def __init__(self, x1, y1, x2, y2, color = (100, 50, 200)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    
    def display(self, screen):
        u.betterRect(screen, self.x1, self.y1, self.x2, self.y2, self.color, 0)