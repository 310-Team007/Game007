import pygame
import player_animation

# Agent_SpriteSheet_1 size: 320 X 620px
# frame size: 30 X 33px
spritesheet_image = pygame.image.load('images/Agent_SpriteSheet_1.png').convert_alpha()
spritesheet = player_animation.SpriteSheet(spritesheet_image)


# Agent_SpriteSheet_1.png will need to be modified to be horizontal per animation cycle used

# frame 0
idle_frame = spritesheet.get_image(0, 30, 33, 3, BLACK)
# frame_1 = spritesheet.get_image(1, 30, 33, 3, BLACK)
# frame_2 = spritesheet.get_image(2, 30, 33, 3, BLACK)

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

        # gets a frame along a horizontal sprite sheet
        def get_image(self, frame, width, height, scale, color):
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)

            return image