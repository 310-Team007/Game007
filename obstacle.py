import pygame
from pygame.sprite import Group
import constants as c

Sprite = pygame.sprite.Sprite 

class Obstacle(Sprite):
    """Creates and draws an obstacle"""

    def __init__(self, color, width, height):
        
        self.location = (0,0)

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        # Fill entire image with one color, change for actual project
        self.image.fill(color)

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()

    # Move this method to display
    def draw_obstacle(self, obstacle_pos):
        """Draws obstacle"""
        # pygame.draw.rect(self.screen, "red", obstacle_pos, c.OBSTACLE_WIDTH)