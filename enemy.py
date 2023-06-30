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

    spritesheet_grunt = SpriteSheet(enemy_image_grunt)
    spritesheet_sniper = SpriteSheet(enemy_image_sniper)
    spritesheet_boss = SpriteSheet(enemy_image_boss)

    def grunt():
        pass

    def sniper():
        pass

    def boss():
        pass