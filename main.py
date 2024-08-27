import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots

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

    # Creating groups
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add sprites to the groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shots.containers = (shots, updatable, drawable) 
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

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

        # Updating player
        for item in updatable:
            item.update(dt)

        # Check for collision
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        # Check for hit
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    # Kill shot
                    shot.kill()

                    # Split Asteroid
                    asteroid.split()
                    
        # Fill
        pygame.Surface.fill(screen, (0,0,0))

        # Render player
        for item in drawable:
            item.draw(screen)

        # Refresh / Update
        pygame.display.flip()

        # Pausing the game loop
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()