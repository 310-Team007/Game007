import pygame
import constants as c


class Bullets(pygame.sprite.Sprite):
    def __init__(self, origin, width, height): 
        pygame.init()
               
        self.bullet = pygame.Rect(origin.x, origin.y -  c.PLAYER_HEIGHT/2 , width, height)
        self.bullet_alive = False
        
        
    def player_bullet_move(self, bullet, clock_speed):
        bullet = bullet.move(600 * clock_speed, 0)
        
        return bullet
    
    def bullet_collide(self, character_pos, player_pos):
        if (self.bullet.left <= character_pos.x + (c.PLAYER_WIDTH) and self.bullet.left + c.BULLET_WIDTH >= character_pos.x and self.bullet.top <= character_pos.y + c.PLAYER_HEIGHT * c.PLAYER_SCALE and self.bullet.top + c.BULLET_HEIGHT >= character_pos.y - c.PLAYER_HEIGHT):
            self.set_dead(player_pos)
        if self.bullet.left == c.SCREEN_WIDTH - 300:
            self.set_dead(player_pos)
        
        
    def set_alive(self):
        self.bullet_alive = True
        
    def set_dead(self, player_pos):
        self.bullet_alive = False
        self.bullet.left = player_pos.x
        self.bullet.top = player_pos.y

        
    
    
    def emeny_bullet(self):
        pass
        
        
        
        


