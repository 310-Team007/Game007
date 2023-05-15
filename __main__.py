import pygame

import constants as c
import display
import player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    # show = display.MovingBackground()
    player_sprite = player.Player((0, 255, 255), 5, 10)
    
    
    # see Pygame tutorial
    player_pos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    clock_speed = clock.tick(c.FPS) / 10000
    
    # draws player

    running = True
    while running:
        clock.tick(c.FPS)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
        
        
        # draws, gets movement and apply movement
  
        movement = pygame.key.get_pressed()
        player_sprite.move(player_pos, clock_speed, movement)
        
        
        
                
        pygame.display.update()

if __name__ == "__main__":
    main()