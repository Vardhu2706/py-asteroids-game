# In pygame, base class 'Sprite' is used to represent visual objects.

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, x, y, radius):

        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Initializing position
        self.position = pygame.Vector2(x, y)

        # Initializing Velocity
        self.velocity = pygame.Vector2(0, 0)

        # Initializing Radius
        self.radius = radius

    # Draw method
    def draw(self, screen):
        # Sub-classes must override
        pass

    # Update method
    def update(self, dt):
        # Sub-classes must override
        pass

    
