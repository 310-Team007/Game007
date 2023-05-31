import pygame

import constants as c
import display
import player
import obstacle
import physics


def main():
    pygame.init()
    clock = pygame.time.Clock()
    show = display.MovingBackground()
    player_sprite = player.Player((0, 255, 255), 5, 10)
    obstacle_sprite = obstacle.Obstacle((150, 75, 0), 5, 5)
    obstacle_sprite.draw_obstacle(40)
    
    # see Pygame tutorial
    player_pos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    clock_speed = clock.tick(c.FPS) / 1000
    
    gravity = physics.Physics()
    
    # draws player

    running = True
    while running:
        clock.tick(c.FPS)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
        
        
        # draws, gets movement and apply movement
        show.display_background()
        show.move_background(c.BG_SPEED)
        movement = pygame.key.get_pressed()
        player_pos = player_sprite.move(player_pos, clock_speed, movement)
        gravity.physics(player_pos)
        show.draw_player(player_pos)
        
        
        
                
        pygame.display.update()

if __name__ == "__main__":
    main()