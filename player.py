import pygame
from pygame.sprite import _Group

Sprite = pygame.sprite.Sprite 

class  Player(Sprite):
    def __init__(self):
        self.location = (0,0)
        self.health = 10
        self.alive = True

    def move():
        pass
    
    def pickupGun(location):
        pass

    def useGun():
        pass
