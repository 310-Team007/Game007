import pygame
import sqlite3

import constants as c
import display
import player
import obstacle as Obstacle
import physics
import player_animation as animate
import ui
import enemies.enemy_grunt as grunt
import bullet

#for animation changes
image_amount = 4
row_number = 1

def main():
    pygame.init()
    # general variables 
    clock = pygame.time.Clock()
    show = display.MovingBackground()
    player_sprite = player.Player(c.PLAYER_WIDTH, c.PLAYER_HEIGHT)

    grunt_enemy = grunt.Grunt(c.PLAYER_WIDTH, c.PLAYER_HEIGHT)
    grunts = []
    grunt_spawn_cooldown = 5000
    grunt_shoot_cooldown = 2000
    enemy_spawn_timer = pygame.time.get_ticks()
    enemy_attack_timer = pygame.time.get_ticks()
    
    obstacles = []
    obstacle_height_index = 0

    # for Animations
    last_update = pygame.time.get_ticks()
    frame = 0

    enemy_last_update = pygame.time.get_ticks()
    enemy_frame = 0
    enemy_image_amount = 7
    enemy_row_number = 0
    
    # for positions and movement
    player_pos = pygame.Vector2(c.SCREEN_WIDTH / 2, c.GROUND)
    clock_speed = clock.tick(c.FPS) / 1000
    
    gravity = physics.Physics()
    
    user_inter = ui.UI(player_sprite)
    points = 0
    
    # connects to database and var to modify database
    conn = sqlite3.connect("database/game_data.db")
    mod_db = conn.cursor()
    
    # bullet
    player_bullet_sprite = bullet.Bullets(player_pos, c.BULLET_WIDTH, c.BULLET_HEIGHT)
    enemy_bullet_sprite = bullet.Bullets(player_pos, c.BULLET_WIDTH, c.BULLET_HEIGHT)
    
    
    # draws a screen to get player name input 
    user_input = "" 
    start_screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    text_font = pygame.font.SysFont("Arial", 50)
    game_name_font = pygame.font.SysFont("Arial", 150, bold=True)
    
    
    running_input = True
    while running_input:
        clock.tick(c.FPS)
        
        for event in pygame.event.get():
            # Handles when use wants to start the game
            # if the quit button is press or the return key is press the game will start
            if event.type == pygame.QUIT:
              running_input = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running_input = False
                
            # gets user user input for username
            if event.type == pygame.KEYDOWN:
                # when the backspace is press
                # remove the last index in the str
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
        
        # rendering back ground         
        show.display_background()
        show.move_background(c.BG_SPEED)
        
        # setting strings to render 
        # gettig the color of the string
        user_hint = text_font.render("Enter User Name: ", True, (0,0,0))
        user_name = text_font.render(user_input, True, (0,0,0))
        game_name = game_name_font.render("GAME 007", True, (0,0,0))
        
        # rendering the strings on the screen
        start_screen.blit(user_hint, (c.SCREEN_WIDTH/2 + 50, c.SCREEN_HEIGHT/2 + 100))
        start_screen.blit(user_name, (c.SCREEN_WIDTH/2 + 400, c.SCREEN_HEIGHT/2 + 100))
        start_screen.blit(game_name, ((c.SCREEN_WIDTH/2) - 50, (c.SCREEN_HEIGHT/2) - 100))
         
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
            player_pos = obstacle.stop_player(player_pos, movement, gravity)
            show.draw_obstacle(obstacle)
            # gravity.physics(player_pos, obstacle.rect)


        # Draw player
        show.draw_player(player_pos, frame, image_amount, row_number)
        
        # Draw bullet
        player_sprite.useGun(movement, player_bullet_sprite, player_pos)
        
        if player_bullet_sprite.bullet_alive == True:
            show.draw_bullet(player_bullet_sprite.bullet)
            player_bullet_sprite.bullet = player_bullet_sprite.player_bullet_move(player_bullet_sprite.bullet, clock_speed)

        if enemy_bullet_sprite.bullet_alive == True:
            show.draw_bullet(enemy_bullet_sprite.bullet)
            enemy_bullet_sprite.bullet = enemy_bullet_sprite.enemy_bullet_move(enemy_bullet_sprite.bullet, clock_speed)
            
        
        # Enemy stuff
        # grunt spawn current_time - last_update >= animation_cooldown
        current_time = pygame.time.get_ticks()
        if(current_time - enemy_spawn_timer >= grunt_spawn_cooldown):
            grunt_enemy = grunt.Grunt(c.PLAYER_WIDTH, c.PLAYER_HEIGHT)
            grunts.append(grunt_enemy)
            enemy_spawn_timer = current_time

        # allows for multiple enemies at onces
        for grunt_enemy in grunts:
            if (grunt_enemy.alive == True):
                show.DrawEnemy(grunt_enemy.rect, enemy_frame, enemy_image_amount, enemy_row_number, grunt.spritesheet_grunt, sprite_width = 128, sprite_height = 128, scale = 1.3)
                grunt_enemy.rect = grunt_enemy.move(grunt_enemy.rect, clock_speed)
                player_bullet_sprite.bullet_collide(grunt_enemy.rect, player_pos, grunt_enemy)
                grunt_enemy.die(user_inter)

                # enemy shooting back
                bullet_time = pygame.time.get_ticks()
                if(bullet_time - enemy_attack_timer >= grunt_shoot_cooldown):
                    # player_sprite.useGun(movement, player_bullet_sprite, player_pos)
                    grunt_enemy.grunt_shoot(enemy_bullet_sprite)
                    enemy_attack_timer = bullet_time


        # for animations
        frame, last_update = animate.ItterateTimedFrames(current_time, last_update, frame, image_amount)
        enemy_frame, enemy_last_update  = animate.ItterateTimedFrames(current_time, enemy_last_update, enemy_frame, enemy_image_amount)
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