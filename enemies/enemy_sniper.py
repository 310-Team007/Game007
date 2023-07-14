import pygame
from enemies.enemy import Enemy
import player_animation as animate

# spritesheet image
enemy_image_sniper = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_3_Spritelist.png').convert_alpha()
# Sniper: 2944 x 1536px
# frame size: 126 x 126px ? (Dosen't start on row 0)
spritesheet_sniper = animate.SpriteSheet(enemy_image_sniper)

Sprite = pygame.sprite.Sprite 

# uncommon, sneaky enemy
# spawns to the left and leaves after shot
# shoots to the right once (2 damage)
class Sniper(Enemy):
    def __init__(self, color, width, height):
        Enemy.set_health(Enemy.__init__,1)

