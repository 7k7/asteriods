from random import uniform

import pygame

from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt


    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = uniform(20, 50)

        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(int(self.position.x), int(self.position.y), new_radius)
        asteroid_2 = Asteroid(int(self.position.x), int(self.position.y), new_radius)
        asteroid_1.velocity = vector_1 * 1.2
        asteroid_2.velocity = vector_2 * 1.2
