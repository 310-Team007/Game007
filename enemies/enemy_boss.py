import pygame
from enemies.enemy import Enemy
import player_animation as animate

# spritesheet image
enemy_image_boss = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_2_Spritelist.png').convert_alpha()
# Boss: 2432 x 1280px
# frame size: 128 x 128px ?
spritesheet_boss = animate.SpriteSheet(enemy_image_boss) 

Sprite = pygame.sprite.Sprite 

# uncommon, big enemy
# spawns to the right and wstays on the right side of the screen until defeated
# shoots to the left in a three shot burst (1 damage per bullet)
class Boss(Enemy):
    Enemy.set_health(Enemy.__init__,7)