# Player class, child of CircleShape
from circleshape import CircleShape
import pygame
from constants import *
import random

# Asteroid class
class Asteroid(CircleShape):

    # Contructor
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Split method
    def split(self):
        # Kill itself
        self.kill()

        # Check asteroid size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_vector_1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_vector_2 * 1.2

    # Overriding Draw method
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2
        )

    # Overriding Update method
    def update(self, dt):
        self.position += (self.velocity * dt)
