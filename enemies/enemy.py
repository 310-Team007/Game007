import pygame

"""
Authors: 
Kaleb Schauerhamer
Jacob Gunderson
"""

Sprite = pygame.sprite.Sprite 
class Enemy(Sprite):
    def __init__(self, width, height):
        self.health = int
        self.alive = True
        
        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()

    def set_health(self, health):
        self.health = health

    def EnemyShoot():
        pass

    def EnemyMelee():
        pass