import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20,50)
            new_velocity1 = self.velocity.rotate(split_angle)
            new_velocity2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ass1 = Asteroid(self.position.x, self.position.y, new_radius)
            ass2 = Asteroid(self.position.x, self.position.y, new_radius)
            ass1.velocity = new_velocity1
            ass2.velocity = new_velocity2