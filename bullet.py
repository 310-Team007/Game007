import pygame
import constants as c


class Bullets(pygame.sprite.Sprite):
    def __init__(self, origin, width, height): 
        pygame.init()
               
        self.bullet = pygame.Rect(origin.x, origin.y -  (c.PLAYER_HEIGHT * c.PLAYER_SCALE) / 2 , width, height)
        self.bullet_alive = False
        
        
    def player_bullet_move(self, bullet, clock_speed):
        bullet = bullet.move(600 * clock_speed, 0)
        
        return bullet
    
    def bullet_collide(self, character_pos, player_pos, character):
        if (self.bullet.left <= character_pos.x + (c.PLAYER_WIDTH) and self.bullet.left >= character_pos.x and self.bullet.top >= character_pos.y - c.PLAYER_HEIGHT * c.PLAYER_SCALE and self.bullet.top + c.BULLET_HEIGHT <= character_pos.y):
            self.set_dead(player_pos)
            character.get_shot()

            print("Hit")
        if self.bullet.left == c.SCREEN_WIDTH - c.BULLET_WIDTH:
            self.set_dead(player_pos)
            print("Miss")
        
    def set_alive(self):
        self.bullet_alive = True
        
    def set_dead(self, player_pos):
        self.bullet_alive = False
        self.bullet.left = player_pos.x + c.PLAYER_WIDTH
        self.bullet.top = player_pos.y - (c.PLAYER_HEIGHT * c.PLAYER_SCALE) / 2

        
    
    
    def emeny_bullet(self):
        pass
        
        
        
        


