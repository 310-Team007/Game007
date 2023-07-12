import pygame
import math
import player

import constants as c
import player_animation as animated

"""
followed this video for basic of getting the background to move
https://www.youtube.com/watch?v=ARt6DLP38-Y

"""

class MovingBackground(): 
    """
    This class controls the movement of the background
    mapping to the movement of the player
    
    Authors:
        Spencer Wigren
        Jacob Gunderson
    """
    
    def __init__(self):
        
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        
        self.bg = pygame.image.load(c.BACKGROUND).convert()
        self.bg_width = self.bg.get_width()
        self.bg_rect = self.bg.get_rect()

        self.scroll = 0
        self.tiles = math.ceil((c.SCREEN_WIDTH / self.bg_width)) + 1
     
     
    def display_background(self):
        self.screen
        
     
    def move_background(self, bg_speed):
        """
        Gets player movement (L,R,U,D)
        applies the background moving with the input
        """
        
        # moves the images
        for i in range(0, self.tiles):
            self.screen.blit(self.bg, (i * self.bg_width + self.scroll, 0))
            
        # scroll background
        self.scroll -= bg_speed

        # check to see if self.scroll needs to be reset
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0

    def draw_player(self, player_pos, frame, image_amount = 4, row_number = 1):
        """Draws player
        """
        # pygame.draw.circle(self.screen, "red", player_pos, c.PLAYER_WIDTH)

        # Shows player sprite & allows animation
        animated.ShowSprite(self, player_pos, frame, image_amount, row_number)

    def draw_obstacle(self, obstacle):
        # Image is 16 by 16
        obstacleImage = pygame.image.load("images/metal_blocks.png").convert_alpha()
        # obstacleSheet = animated.spritesheet(obstacleImage)
        # obstacle.blit(obstacle, (1, 1), (1, 1, 16, 16))

        pygame.draw.rect(self.screen, c.PINK, obstacle)
