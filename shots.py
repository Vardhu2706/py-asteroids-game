from circleshape import CircleShape
import pygame
from constants import *

class Shots(CircleShape):

    # Contructor
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Overriding Draw method
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=SHOT_RADIUS,
            width=2
        )

    # Overriding Update method
    def update(self, dt):
        self.position += (self.velocity * dt)