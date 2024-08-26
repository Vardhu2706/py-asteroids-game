# Player class, child of CircleShape
from circleshape import CircleShape
import pygame
from constants import *

# Player class
class Player(CircleShape):
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

        super().__init__(x, y, PLAYER_RADIUS)

        self.position = pygame.Vector2(x, y)
        self.rotation = 0

    # Triangle method - returns corner coordinates
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    # Rotate method
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    # Move method
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    # Overriding Draw method
    def draw(self, screen):
        # Getting the points
        points = self.triangle()
        
        # Drawing the player/triangle
        pygame.draw.polygon(
            surface=screen, 
            color="white", 
            points=points,
            width=2)
        
    # Overriding Update method
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Left and right
        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        
        # Up and down
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)