import pygame
import sqlite3

import constants as c
import display
import player
import obstacle as Obstacle
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
    player_sprite = player.Player(c.PLAYER_WIDTH, c.PLAYER_HEIGHT)
    obstacle_sprite = Obstacle.Obstacle(c.OBSTACLE_WIDTH, c.OBSTACLE_HEIGHT, 3)
    obstacles = []
    obstacle_height_index = 0

    # for Animations
    last_update = pygame.time.get_ticks()
    frame = 0
    
    # see Pygame tutorial
    player_pos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.GROUND)
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
        
        # Show and move background
        show.display_background()
        show.move_background(c.BG_SPEED)

        # gets and applies movement
        movement = pygame.key.get_pressed()
        player_pos = player_sprite.move(player_pos, clock_speed, movement)
        gravity.physics(player_pos)

        # Create an obstacle every 2 seconds
        if (pygame.time.get_ticks() / 10) % 2 == 0:
            obstacle_height_index += 1
            if obstacle_height_index >= len(c.OBSTACLE_VECTOR):
                obstacle_height_index = 0
            if c.OBSTACLE_VECTOR[obstacle_height_index] != 0:
                an_obstacle = Obstacle.Obstacle(c.OBSTACLE_WIDTH, c.OBSTACLE_HEIGHT, obstacle_height_index)
                obstacles.append(an_obstacle)

        # Move and draw every obstacle
        for obstacle in obstacles:
            obstacle.move()
            player_pos = obstacle.stop_player(player_pos, clock_speed)
            show.draw_obstacle(obstacle)


        # Draw player
        show.draw_player(player_pos, frame, image_amount, row_number)
        
        # for animations
        current_time = pygame.time.get_ticks()
        frame, last_update = animate.ItterateTimedFrames(current_time, last_update, frame, image_amount)
        user_inter.draw_ui()
                
        pygame.display.update()

    # gets player health at end of game
    health = player_sprite.health
    # gets player score at end of game
    score = user_inter.score
    # puts player name, health, and score into db
    # TODO have player make name
    mod_db.execute(f"INSERT INTO player VALUES ('Bob', {health}, {score})")


    # save date to db
    conn.commit()
    # close connection to db
    conn.close()
    
if __name__ == "__main__":
    main()