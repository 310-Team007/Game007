import pygame
import sqlite3

import constants as c
import display
import player
import obstacle
import physics
import player_animation as animate
import ui

#for animation changes
image_amount = 4
row_number = 1

def main():
    pygame.init()
    clock = pygame.time.Clock()
    show = display.MovingBackground()
    player_sprite = player.Player((0, 255, 255), c.PLAYER_WIDTH, c.PLAYER_HEIGHT)
    obstacle_sprite = obstacle.Obstacle((150, 75, 0), 5, 5)
    obstacle_sprite.draw_obstacle(40)

    # for Animations
    last_update = pygame.time.get_ticks()
    frame = 0
    
    # see Pygame tutorial
    player_pos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    clock_speed = clock.tick(c.FPS) / 1000
    
    gravity = physics.Physics()
    
    user_inter = ui.UI(player_sprite)
    
    # connects to database and var to modify database
    conn = sqlite3.connect("database/game_data.db")
    mod_db = conn.cursor()
    
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
        show.draw_player(player_pos, frame, image_amount, row_number)
        

        # for animations
        current_time = pygame.time.get_ticks()
        frame, last_update = animate.ItterateTimedFrames(current_time, last_update, frame, image_amount)
        
        user_inter.draw_ui()
                
        pygame.display.update()

    # save date to db
    conn.commit()
    # close connection to db
    conn.close()
    
if __name__ == "__main__":
    main()