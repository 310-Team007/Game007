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
    player_sprite = player.Player((0, 255, 255), c.PLAYER_WIDTH, c.PLAYER_HEIGHT)
    obstacle_sprite = Obstacle.Obstacle(c.OBSTACLE_WIDTH, c.OBSTACLE_HEIGHT, 3)
    obstacles = []
    obstacle_height_index = 0

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
    
    # draws a screen to get player name input 
    user_input = "" 
    input_screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    text_font = pygame.font.SysFont("Arial", 30)
    
    
    running_input = True
    while running_input:
        clock.tick(c.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_input = False
                
            if event.type == pygame.KEYDOWN:
                # if event.type == pygame.K_BACKSPACE:
                #     user_input = user_input[:-1]
                # else:
                    user_input += event.unicode
                    
        text_surface = text_font.render(user_input, True, (255,255,255))
        input_screen.blit(text_surface, (c.SCREEN_WIDTH/2, c.SCREEN_HEIGHT/2))
                
        pygame.display.update()
     
    running = True
    while running:
        clock.tick(c.FPS)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
                
                      
        # draws, gets movement and apply movement
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
    player_health = player_sprite.health
    
    # gets player score at end of game
    player_score = user_inter.score
    
    # get player name
    name_of_player = str(user_input)
    
    # combining all values into a tuple
    player_stats = (name_of_player, player_health, player_score)
    
    # sql to put values into db
    sql = """INSERT INTO player(player_name, health, score)
            VALUES (?, ?, ?);"""      
    
    mod_db.execute(sql, player_stats)

    # save date to db
    conn.commit()
    # close connection to db
    conn.close()
    
    
if __name__ == "__main__":
    main()