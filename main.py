import pygame
from constants import *
from player import Player

def main():
    # Initializing PyGame
    pygame.init()

    # Setting screen
    screen = pygame.display.set_mode((
        SCREEN_WIDTH, 
        SCREEN_HEIGHT
    ))

    # Init game clock
    clock = pygame.time.Clock()

    # Init dt
    dt = 0

    # Init player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Game Loop
    while True:
        # Quit event interrupt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill
        pygame.Surface.fill(screen, (0,0,0))

        # Render player
        player.draw(screen=screen)

        # Refresh / Update
        pygame.display.flip()

        # Pausing the game loop
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()