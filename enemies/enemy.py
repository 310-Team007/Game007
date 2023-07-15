import pygame
import constants as c

"""
Authors: 
Kaleb Schauerhamer
Jacob Gunderson
"""

Sprite = pygame.sprite.Sprite 
class Enemy(Sprite):
    def __init__(self, width, height):
        self.health = 1
        self.alive = True
        
        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = c.SCREEN_WIDTH
        self.rect.y = c.GROUND

    def set_health(self, health):
        self.health = health

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def EnemyShoot(self):
        pass

    def EnemyMelee(self):
        pass