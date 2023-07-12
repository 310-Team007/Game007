import pygame
from pygame.sprite import Group
import __main__
#import display

import constants as c

Sprite = pygame.sprite.Sprite 

class  Player(Sprite):
    """Controls:
    drawing the play
    movement of the player
    
    Authors:
        Jacob Gunderson
        Spencer Wigren
        Kaleb Schauerhamer
    """
    def __init__(self, width, height):
        self.location = (0,0)
        self.health = 10
        self.alive = True

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        
        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()
      
    def move(self, player_pos, clock_speed, movement):     
        # self.draw_player(player_pos)

        # default hitbox
        self.image = pygame.Surface([c.PLAYER_WIDTH, c.PLAYER_HEIGHT])

        # walking
        __main__.image_amount = 4
        __main__.row_number = 1
           
        if movement[pygame.K_w]:
            player_pos.y -= 300 * clock_speed
            # self.show.move_background(0)
            # self.draw_player(player_pos)

            # jumping
            __main__.image_amount = 5
            __main__.row_number = 3
            
        if movement[pygame.K_s]:
            player_pos.y += 300 * clock_speed
            if player_pos.y >= c.GROUND:
                player_pos.y = c.GROUND
            # self.show.move_background(0)
            # self.draw_player(player_pos)

            # Modify crawl hitbox
            self.image = pygame.Surface([c.PLAYER_HEIGHT, c.PLAYER_WIDTH])

            # crawling
            __main__.image_amount = 4
            __main__.row_number = 4
            
        if movement[pygame.K_a]:
            player_pos.x -= 300 * clock_speed
            if player_pos.x <= 0:
                player_pos.x = 0
            # self.show.move_background(5)
            # self.draw_player(player_pos)

            # idle/standing still
            __main__.image_amount = 1
            __main__.row_number = 0
            
        if movement[pygame.K_d]:
            player_pos.x += 300 * clock_speed
            if player_pos.x >= c.SCREEN_WIDTH:
                player_pos.x = c.SCREEN_WIDTH - 10
            # self.show.move_background(5)
            # self.draw_player(player_pos)

            # running
            __main__.image_amount = 7
            __main__.row_number = 2
            
        # self.show.move_background(5)
        # self.draw_player(player_pos)

        return player_pos           
        
    def pickupGun(location):
        pass

    def useGun():


        # walk shoot
        __main__.image_amount = 2
        __main__.row_number = 8
        pass
