import pygame
from pygame.sprite import Group
import constants as c

Sprite = pygame.sprite.Sprite 

class Obstacle(Sprite):
    """Creates and draws an obstacle"""

    def __init__(self, width, height, index):
        

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        # Fill entire image with one color, change for actual project
        # self.image.fill(c.PINK)

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = c.SCREEN_WIDTH
        self.rect.y = c.GROUND - c.OBSTACLE_HEIGHT - 15 - (c.PLAYER_HEIGHT * c.PLAYER_SCALE * c.OBSTACLE_VECTOR[index])

    # Return location
    def get_location(self):
        return (self.rect.x, self.rect.y)

    def move(self):
        self.rect.x-= c.BG_SPEED

    def stop_player(self, player_pos, clock_speed):

        if (player_pos.x <= self.rect.x + c.OBSTACLE_WIDTH and player_pos.x + c.PLAYER_WIDTH >= self.rect.x and player_pos.y - c.PLAYER_HEIGHT * c.PLAYER_SCALE <= self.rect.y + c.OBSTACLE_HEIGHT and player_pos.y >= self.rect.y):
            # walk on top
            if player_pos.y >= self.rect.y: 
                player_pos.y = self.rect.y

            #get stopped left
            elif player_pos.x + c.PLAYER_WIDTH >= self.rect.x:
                player_pos.x = self.rect.x - c.PLAYER_WIDTH
                # player_pos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
            # player_pos.x = self.rect.x

        return player_pos
    
# instantiate in a loop in main every x seconds


    # if right side of player == left side of obstacle and any part of player y is greater than top of obstacle and less than bottom of obstacle