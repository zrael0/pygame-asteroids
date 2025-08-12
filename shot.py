import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (50, 100, 200), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt