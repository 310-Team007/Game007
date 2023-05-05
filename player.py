import pygame
from pygame.sprite import _Group

Sprite = pygame.sprite.Sprite 

class  Player(Sprite):
    def __init__(self, color, width, height):
        self.location = (0,0)
        self.health = 10
        self.alive = True

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        # Fill entire image with one color change for actual project
        self.image.fill(color)

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()

    def move():
        pass
    
    def pickupGun(location):
        pass

    def useGun():
        pass
