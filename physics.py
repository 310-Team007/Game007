import constants as c
import pygame

class Physics():
    """
    Generats the physics for the player
    
    Authors:
        Spencer Wigren 
    """
    
    def __init__(self):
        
        # tracker
        self.fall_count = 0
    
    # def physics(self, player_pos, obstacle_pos):
    def physics(self, player_pos):
        # player_pos.y += min(1, (self.fall_count / c.FPS) * c.GRAVITY)
        
        # move player by 1 pixle or the effect of gravity
        player_pos.y += max(1, (self.fall_count / c.FPS) * c.GRAVITY)
        
        
        # collsion wth ground
        if player_pos.y >= c.GROUND:
                player_pos.y = c.GROUND
        
        # This helps keeps the playering falling look real
        # Along with keeping the player from flying away
        if player_pos.y == c.GROUND:
            self.fall_count = 0
        # elif player_pos.y == obstacle_pos.y - c.OBSTACLE_HEIGHT and player_pos.x <= self.rect.x + (c.OBSTACLE_WIDTH) and player_pos.x + c.PLAYER_WIDTH >= self.rect.x:
        #     self.fall_count = 0
        else:
            self.fall_count += 1

    def setFallCount(self, fall_count):
         self.fall_count = fall_count