import pygame
import math

import constants as c

"""
followed video for basic of getting the background to move
https://www.youtube.com/watch?v=ARt6DLP38-Y

"""

class MovingBackground(): 
    
    def __init__(self):
        
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        
        self.bg = pygame.image.load("images\Render_9.png").convert()
        self.bg_width = self.bg.get_width()
        self.bg_rect = self.bg.get_rect()

        self.scroll = 0
        self.tiles = math.ceil((c.SCREEN_WIDTH / self.bg_width)) + 1
     
    def move_background(self):
        for i in range(0, self.tiles):
            self.screen.blit(self.bg, (i * self.bg_width + self.scroll, 0))
            
        # scroll background
        self.scroll -= 5

        if abs(self.scroll) > self.bg_width:
            self.scroll = 0