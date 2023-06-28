from player import Player
import pygame

"""
Authors: 
Kaleb Schauerhamer
"""

# create enemys from player class
class enemy(Player):
    Player.__init__()

    enemy_image1 = pygame.image.load('images/Agent_SpriteSheet_1.png').convert_alpha()
    enemy_image2 = pygame.image.load('images/Agent_SpriteSheet_1.png').convert_alpha()
    enemy_image_boss = pygame.image.load('images/Agent_SpriteSheet_1.png').convert_alpha()