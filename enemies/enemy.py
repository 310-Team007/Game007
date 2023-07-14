import pygame
import player_animation as animate

"""
Authors: 
Kaleb Schauerhamer
Jacob Gunderson
"""

Sprite = pygame.sprite.Sprite 
class enemy(Sprite):

    enemy_image_grunt = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_1_Spritelist.png').convert_alpha()
    enemy_image_sniper = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_3_Spritelist.png').convert_alpha()
    enemy_image_boss = pygame.image.load('images/craftpix-soldiers/PSD/Soldier_2_Spritelist.png').convert_alpha()

# Grunts: 1234 x 1080px
# frame size: 126 x 126px ?
spritesheet_grunt = animate.SpriteSheet(enemy.enemy_image_grunt)

# common enemy
def grunt():

    def __init__(self, width, height):
        self.health = 1
        self.alive = True

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()

    # Grunts: 1234 x 1080px
    # frame size: 126 x 126px ?
    spritesheet_grunt = animate.SpriteSheet(enemy.enemy_image_grunt)


# uncommon, sneaky enemy
def sniper():

    def __init__(self, color, width, height):
        self.location = (0,0)
        self.health = 1
        self.alive = True

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        # Fill entire image with one color, change for actual project
        self.image.fill(color)

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()

    # Sniper: 2944 x 1536px
    # frame size: 126 x 126px ? (Dosen't start on row 0)
    spritesheet_sniper = animate.SpriteSheet(enemy.enemy_image_sniper)



# uncommon, big enemy
def boss():

    def __init__(self, color, width, height):
        self.location = (0,0)
        self.health = 7
        self.alive = True

        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        # Fill entire image with one color, change for actual project
        self.image.fill(color)

        # create a rectangle with dimensions of image
        # must update position with rect.x and rect.y
        self.rect = self.image.get_rect()

    # Boss: 2432 x 1280px
    # frame size: 126 x 126px ?
    spritesheet_boss = animate.SpriteSheet(enemy.enemy_image_boss)  






def EnemyShoot():
    pass

def EnemyMelee():
    pass