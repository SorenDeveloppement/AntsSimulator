import math

import pygame

from constants import Default, Colors
from pheromone import Pheromone


class Ant:
    def __init__(self, x: int, y: int, pheromone: Pheromone) -> None:
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = Default.ANT_SPEED.value
        self.pheromone = pheromone
        self.pheromone_delay = Default.PHEROMONE_DELAY.value

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, Colors.WHITE.value, (self.x, self.y), 5)
        pygame.draw.line(screen, Colors.WHITE.value, (self.x, self.y),
                         (self.x + math.cos(math.radians(self.angle)) * 10,
                          self.y + math.sin(math.radians(self.angle)) * 10))

    def walk(self) -> None:
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def turn_left(self, angle: int = None) -> None:
        if angle is None:
            self.angle += Default.ANGLE_SPEED.value
        else:
            self.angle += angle

        if self.angle > 360:
            self.angle %= 360

    def turn_right(self, angle: int = None) -> None:
        if angle is None:
            self.angle -= Default.ANGLE_SPEED.value
        else:
            self.angle -= angle

        if self.angle > 360:
            self.angle %= 360

    def get_angle(self) -> int:
        return self.angle
