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


# common enemy
def grunt():
    enemy()
    # Grunts: 1234 x 1080px
    # frame size: 126 x 126px ?
    spritesheet_grunt = animate.SpriteSheet(enemy.enemy_image_grunt)

    DrawEnemy()

# uncommon, sneaky enemy
def sniper():
    enemy()
    # Sniper: 2944 x 1536px
    # frame size: 126 x 126px ? (Dosen't start on row 0)
    spritesheet_sniper = animate.SpriteSheet(enemy.enemy_image_sniper)

    DrawEnemy()

# uncommon, big enemy
def boss():
    enemy()
    # Boss: 2432 x 1280px
    # frame size: 126 x 126px ?
    spritesheet_boss = animate.SpriteSheet(enemy.enemy_image_boss)  

    DrawEnemy()


def DrawEnemy(self, player_pos, frame, image_amount, row_number):
    animate.ShowSprite(self, player_pos, frame, image_amount, row_number)