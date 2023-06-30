from player import Player
import pygame
import player_animation as animate

"""
Authors: 
Kaleb Schauerhamer
"""

# create enemys from player class
class enemy(Player):
    Player.__init__()

    enemy_image_grunt = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_1_Spritelist.psd').convert_alpha()
    enemy_image_sniper = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_3_Spritelist.psd').convert_alpha()
    enemy_image_boss = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_2_Spritelist.psd').convert_alpha()

    # Grunts: 1234 x 1080px
    # frame size:
    spritesheet_grunt = SpriteSheet(enemy_image_grunt)

    # Sniper: 2944 x 1536px
    # frame size:
    spritesheet_sniper = SpriteSheet(enemy_image_sniper)
    
    # Boss: 2432 x 1280px
    # frame size:
    spritesheet_boss = SpriteSheet(enemy_image_boss)

    def grunt():
        pass

    def sniper():
        pass

    def boss():
        pass    