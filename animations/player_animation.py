import pygame
import constants as c

"""
Author: Kaleb Schauerhamer
"""

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    # gets a frame along a horizontal sprite sheet
    def get_image(self, frame, row, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), (row * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
        

# Agent_SpriteSheet_1 size: 320 X 620px
# frame size: 28 X 32px
screen = pygame.display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
spritesheet_image = pygame.image.load('images/Agent_SpriteSheet_1.png').convert_alpha()
spritesheet = SpriteSheet(spritesheet_image)

# creates a list of images from any row in the spritesheet
def GetSpriteSeries(image_amount, row_number):
    animation_list = []
    for x in range(image_amount):
        animation_list.append(spritesheet.get_image(x, row_number, 32, 32, 3, c.PINK))

    return animation_list

# spritesheet GetSpriteSeries(image_amount, row_number) inputs
# idle: (1, 0)
# walk: (4, 1)
# run: (7, 2)
# jump: (5, 3)
# crawl: (4, 4)
# draw gun: (4, 5)
# gun walk: (4, 6)
# shoot: (5, 7)
# walk shoot: (2, 8)
# punch: (4, 9)
# kick: (4, 10)
# hurt: (4, 11)
# damage: (2, 12)
# fall: (3, 13)
# push: (4, 14)
# death: (5, 15)
# swim: (4, 16)
# tread water: (4, 17)
# climb: (7, 18)

animation_cooldown = 200

# itterateas through a series of images to create animation
def ItterateTimedFrames(current_time, last_update, frame_number, animated_list_length):
    if current_time - last_update >= animation_cooldown:
        frame_number += 1
        last_update = current_time
        if frame_number >= animated_list_length:
            frame_number = 0

    return (frame_number, current_time)

