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

    spritesheet = SpriteSheet(enemy_image_grunt)
    spritesheet = SpriteSheet(enemy_image_sniper)
    spritesheet = SpriteSheet(enemy_image_boss)
    
    # Grunts:
    # 1234 x 1080px
    
    # Sniper:
    # 2944 x 1536px
    
    # Boss:
    # 2432 x 1280px
  