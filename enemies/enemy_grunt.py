import pygame
from enemies.enemy import Enemy
import player_animation as animate
import __main__

# spritesheet image & animation stuff
enemy_image_grunt = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_1_Spritelist.png').convert_alpha()
# Grunts: 1234 x 1080px
# frame size: 128 x 128px ?
spritesheet_grunt = animate.SpriteSheet(enemy_image_grunt)

Sprite = pygame.sprite.Sprite 

# common enemy
# spawns to the right and stands still (carried off the screen by moving background)
# shoots to the left (1 damage)
class Grunt(Enemy):
    Enemy.set_health(Enemy.__init__, 10)

    def move(self, enemy_pos, clock_speed):
        enemy_pos.x -= 300 * clock_speed
        return enemy_pos
    
    def grunt_shoot(self, bullet):
         bullet.set_alive(self.rect.x, self.rect.y)

         return bullet
        # bullet.enemy_bullet_move(bullet, clock_speed)

    def get_status():
        Enemy.get_alive(Enemy.__init__)
    
    def get_shot(self):
        self.health -= 1
        print(self.health)

    def die(self, user_inter):
        if self.health <= 0:
            self.alive = False
            print(self.alive)
            
            user_inter.score += 10