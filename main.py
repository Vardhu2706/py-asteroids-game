import pygame
from constants import *

def main():
    # Initializing PyGame
    pygame.init()

    # Setting screen
    screen = pygame.display.set_mode((
        SCREEN_WIDTH, 
        SCREEN_HEIGHT
    ))

    # Game Loop
    while True:
        # Quit event interrupt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill
        pygame.Surface.fill(screen, (0,0,0))

        # Refresh / Update
        pygame.display.flip()

if __name__ == "__main__":
    main()