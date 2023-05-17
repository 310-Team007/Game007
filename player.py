import pygame
from pygame.sprite import Group
import display

import constants as c

Sprite = pygame.sprite.Sprite 

class  Player(Sprite):
    """Controls:
    drawing the play
    movement of the player
    
    Authors:
        Jacob Gunderson
        Spencer Wigren
    """
    def __init__(self, color, width, height):
        self.location = (0,0)
        self.health = 10
        self.alive = True

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        # Fill entire image with one color change for actual project
        self.image.fill(color)

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()
        
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.show = display.MovingBackground()  

    def draw_player(self, player_pos):
        """Draws player
        """
        pygame.draw.circle(self.screen, "red", player_pos, c.PLAYER_WIDTH)


    def move(self,player_pos, clock_speed, movement):     
        self.draw_player(player_pos)
           
        if movement[pygame.K_w]:
            player_pos.y -= 300 * clock_speed
            # self.show.move_background(0)
            self.draw_player(player_pos)
            
        if movement[pygame.K_s]:
            player_pos.y += 300 * clock_speed
            if player_pos.y >= c.GROUND:
                player_pos.y = c.GROUND
            # self.show.move_background(0)
            self.draw_player(player_pos)
            
        if movement[pygame.K_a]:
            player_pos.x -= 300 * clock_speed
            if player_pos.x <= 0:
                player_pos.x = 0
            # self.show.move_background(5)
            self.draw_player(player_pos)
            
        if movement[pygame.K_d]:
            player_pos.x += 300 * clock_speed
            if player_pos.x >= c.SCREEN_WIDTH:
                player_pos.x = c.SCREEN_WIDTH - 10
            # self.show.move_background(5)
            self.draw_player(player_pos)
            
        self.show.move_background(5)
        self.draw_player(player_pos)
            
        
    def pickupGun(location):
        pass

    def useGun():
        pass
