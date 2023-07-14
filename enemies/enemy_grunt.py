import pygame
from enemies.enemy import Enemy
import player_animation as animate

# spritesheet image & animation stuff
enemy_image_grunt = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_1_Spritelist.png').convert_alpha()
# Grunts: 1234 x 1080px
# frame size: 126 x 126px ?
spritesheet_grunt = animate.SpriteSheet(enemy_image_grunt)

Sprite = pygame.sprite.Sprite 

# common enemy
# spawns to the right and stands still (carried off the screen by moving background)
# shoots to the left (1 damage)
class Grunt(Enemy):
    Enemy.set_health(Enemy.__init__, 1)

    def move(self, enemy_pos, clock_speed):
        enemy_pos.x -= 300 * clock_speed
        return enemy_pos
    