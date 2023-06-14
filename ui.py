import pygame

import constants as c


class UI():
    """ 
    This class creats and draws the UI
     - player health
     - player score
    
    Def: draw_ui: renders the ui
         ui_background: sets a solid color behind the player information
         health_ui: renders the health the player has
         score_ui: renders the score of the player
    
    Authors: Spencer Wigren, Kaleb Schauerhamer
    """
    def __init__(self, player_info):
        # self.text = "Hearts"
        self.text_font = pygame.font.SysFont("Arial", 30)
        self.text_color = (0, 0, 0) # RGB value
        
        # TODO may need to create this in main
        # TODO along with player class self.screen move to main
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        # getting player health
        self.player_health = player_info
        
        # temp score TODO remove once real score is created
        self.score = 100
    
    def draw_ui(self):
        """
        Calls all methods to create and render ui
        """    
    
        # self.ui_background()
        self.health_ui()
        self.score_ui()
    
    
    def ui_background(self):
        # Where it is drawing, (RBB value), (x_cord y_cord width height)
        # pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, 200, 50))
        pass

        
    def health_ui(self):
        """
        Creates simply ui text for the player health
        """
        # gets the player health
        health = str(self.player_health.health)
        
        # set the string for dispaly
        # TODO add hearts images for each health the player has
        health_text = "Health: " + health

        # health hearts
        # heart_img = pygame.image.load('images/pixel-heart.png')
        # heart_img = pygame.transform.scale(heart_img, (35, 35))

        # counter = 0
        # for x in range(self.player_health.health):
        #     self.screen.blit(heart_img, (c.HEALTH_X, c.HEALTH_Y))
        #     c.HEALTH_X += 35
        #     if counter >= 5:
        #         c.HEALTH_Y += 35
        #         c.HEALTH_X = c.HEALTH_X - (35 * 5)
        #         counter = 0

        health_img = self.text_font.render(health_text, True, self.text_color)
        self.screen.blit(health_img, (c.HEALTH_X, c.HEALTH_Y))
        
    def score_ui(self):
        """
        Create simply ui text for player score 
        """
        # TODO add score from player class later
        score_text = "Score: " + str(self.score)
        
        score_img = self.text_font.render(score_text, True, self.text_color)
        self.screen.blit(score_img, (c.SCORE_X, c.SCORE_Y))