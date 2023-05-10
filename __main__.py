import pygame

import constants as c
import display



def main():
    pygame.init()
    clock = pygame.time.Clock()
    show = display.MovingBackground()
    
    running = True
    
    while running:
        
        clock.tick(c.FPS)
        
        show.move_background()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.update()

if __name__ == "__main__":
    main()  