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
    
    def physics(self, player_pos):
        # move player by 1 pixle or the effect of gravity
        # player_pos.y += min(1, (self.fall_count / c.FPS) * c.GRAVITY)
        
        # anit gravity
        player_pos.y += max(1, (self.fall_count / c.FPS) * c.GRAVITY)
        
        
        # collsion
        if player_pos.y >= c.GROUND:
                player_pos.y = c.GROUND
        
        # tracker
        if player_pos.y == c.GROUND:
            self.fall_count = 0
            
        else:
            self.fall_count += 1